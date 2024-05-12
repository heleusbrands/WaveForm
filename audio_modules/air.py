import pandas as pd
import numpy as np
import math
from scipy.signal import stft
from itertools import islice, repeat, chain, tee
from pydantic.v1 import dataclasses
from dataclasses import asdict, dataclass
from collections import deque
from enum import Enum
from .types import ValidTimeDomain, ValidFrequencyDomain, ValidDecibelDomain, ValidPitchDomain, ValidPascalDomain, DomainType, DOMtype
from audio_modules.core.configs import MethodDecoratorBase
from array import array


class DimensionalType:

	def __init__(self, array=None):
		self._a = array
		self._d1 = array.shape[0] if array is not None else None
		self._d2 = array.shape[1] if array is not None and (len(array.shape) > 1) else None

	def step_into(self, arr):
		if arr is None:
			return self._a[0] if self.ndimensions > 1 else None
		else:
			return arr[0] if len(arr.shape) > 1 else arr
	
	def __floor_level__(self, a):
		if len(a.shape) == 1:
			return a
		else:
			return self.__floor_level__(self.step_into(a))
	
	def __setup__(self, value):
		if not isinstance(value, np.ndarray):
			value = np.array(value)
		self._d1 = value.shape[0]
		self._d2 = value.shape[1] if len(value.shape) > 1 else None
		self._a = value
		return value
	
	def __eq__(self, __value: object) -> bool:
		pass

	def __matmul__(self, __value: object) -> bool:
		return self.__eq__(__value)

	@property
	def ndimensions(self):
		return len(self._a.shape)
	
	@property
	def height(self):
		return len(self._a) if self.ndimensions > 1 else 0
	
	@property
	def width(self):
		if self.ndimensions == 1:
			return len(self._a)
		else:
			return len(self.__floor_level__(self._a))
	
	@property
	def depth(self):
		if self.ndimensions == 1:
			return 0
		lvl = 0
		arr = self._a
		while len(arr.shape) > 1:
			if len(arr.shape) == 1: break
			arr = self.step_into(arr)
			lvl += 1
		return lvl

class Iso(DimensionalType):
	"""
	Describes a 1 dimensional array that has a single row. 
	"""
	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		value = self.__setup__(value)
		return True if self.ndimensions == 1 else False
		
	def __matmul__(self, __value: object) -> bool:
		return self.__eq__(__value)
	
class Uni(DimensionalType):
	"""
	Describes a 2 dimensional array that is rectangular and has 1 row and 1 column.

	Example useage might be to determine if an audio signal is mono or if an array needs to be squeezed.
	"""
	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		value = self.__setup__(value)
		return True if self.ndimensions == 2 and self.height == 1 else False
		
	def __matmul__(self, __value: object) -> bool:
		return self.__eq__(__value)

class Twin(DimensionalType):
	"""
	Describes a 2 dimensional array that has 2 rows and 1 column.
	
	Example useage might be to determine if an audio signal is stereo.
	"""
	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		value = self.__setup__(value)
		return True if (self.ndimensions == 2 and self.height == 2) else False
	
	def __matmul__(self, __value: object) -> bool:
		return self.__eq__(__value)

class Tri(DimensionalType):
	"""
	Describes a 2 dimensional array that is rectangular and has 3 rows and 1 column.

	Example useage might be to determine if an array has the right size to be plotted
	onto a 3D graph.
	"""
	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		value = self.__setup__(value)
		return True if (self.ndimensions == 2 and self.height == 3 and self.depth == 1) else False
	
	def __matmul__(self, __value: object) -> bool:
		return self.__eq__(__value)

class Eso(DimensionalType):
	"""
	Describes a 2 dimensional array that is rectangular and has > 3 rows and 1 column.

	Example Useaage might be to determine if an array is over the size limit to be plotted to a 3D graph. 
	"""
	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		value = self.__setup__(value)
		return True if (self.ndimensions == 2 and self.height > 3 and self.depth == 1) else False
	
	def __matmul__(self, __value: object) -> bool:
		return self.__eq__(__value)
	
class Elon(DimensionalType):
	"""
	Short for Echelon and describes an array that is multidimensional, arranged in a heirarchy of 3 or more levels.
	""" 
	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		value = self.__setup__(value)
		return True if (self.ndimensions == 2 and self.height > 3 and self.depth > 1) else False
	
	def __matmul__(self, __value: object) -> bool:
		return self.__eq__(__value)
	
class Incompatible: pass

@dataclass
class NDtypes:
	Iso = Iso()
	Uni = Uni()
	Twin = Twin()
	Tri = Tri()
	Eso = Eso()
	Elon = Elon()

class NDtype:
	def __init__(self, data):
		self.data = data
		if NDtypes.Elon @data: self.ndtype = Elon
		elif NDtypes.Eso @data: self.ndtype = Eso
		elif NDtypes.Tri @data: self.ndtype = Tri
		elif NDtypes.Twin @data: self.ndtype = Twin
		elif NDtypes.Uni @data: self.ndtype = Uni
		elif NDtypes.Iso @data: self.ndtype = Iso
		else: self.ndtype = Incompatible

	def __repr__(self):
		return self.ndtype().__repr__()

@dataclass
class AirSpectrum:

	def dict(self):
		return asdict(self)

class UpdateOnChange(MethodDecoratorBase):

	def __init__(self, method):
		super().__init__(method)
		self.last_value = None

	def __call__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs
		if self.needs_update():
			self.reset_for_update()
		if type(self.method) == property:
			return self.method
		else:
			return self.method(*args, **kwargs)

	def get_updatables(self):
		return self.instance.updatable
	
	def needs_update(self):
		if self.last_value == None: 
			self.last_value = self.instance
			return False
		else:
			return self.last_value != self.instance
		
	def reset_for_update(self):
		self.last_value = self.instance
		for key in self.get_updatables():
			setattr(self.instance, key, None)

class AirLane:
	""" Takes an array and an optional threshold value as inputs. The class has various attributes that are calculated based on the input array and threshold value.

	If the threshold value is not provided, the class will automatically process the input array to calculate the attributes.

	If the threshold value is provided, the class will manually process the input array to calculate the same attributes as above, but with adjusted values for pmin and vmax based on the threshold value.

	Note that the code uses the numpy library, so it must be imported for this code to work correctly.

	Parameters
	----------
	array : array
		array of values.
	threshold : float
		value between 0 and 1 that determines the pmin and vmax values. If not provided, the class will automatically calculate the pmin and vmax values.

	Attributes
	----------
	pmax : float
		maximum value in the array.
	vmin : float
		minimum value in the array.
	mean : float
		mean value of the array.
	pmin : float
		mean value of the array where the values are greater than the mean.
	vmax : float
		mean value of the array where the values are less than the mean.
	peaklane : array
		array of values greater than pmin.
	valleylane : array
		array of values less than vmax.
	mainlane : array
		array of values between vmax and pmin.
	"""
	
	def __init__(self, array: np.ndarray, threshold=None):
		
		self._array = array
		self._threshold = threshold
		self.array = array
		self.pmax = None
		self.pmin = None
		self.vmax = None
		self.vmin = None
		self.mean = None
		self.peaklane = None
		self.valleylane = None
		self.mainlane = None
		if self._threshold is None:
			self._autoprocess()
		else:
			self._manualprocess()

	def _autoprocess(self):
		self.pmax = np.max(self._array)
		self.vmin = np.min(self._array)
		self.mean = np.mean(self._array)
		self.pmin = np.mean(self._array[self._array > self.mean])
		self.vmax = np.mean(self._array[self._array < self.mean])
		self.peaklane = self._array[self._array > self.pmin]
		self.valleylane = self._array[self._array < self.vmax]
		self.mainlane = self._array[(self._array > self.vmax) & (self._array < self.pmin)]

	def _manualprocess(self):
		self.pmax = np.max(self._array)
		self.vmin = np.min(self._array)
		self.mean = np.mean(self._array)
		self.pmin = self.pmax - (self.pmax * self._threshold)
		self.vmax = self.vmin + (self.vmin * self._threshold)
		self.peaklane = self._array[self._array > self.pmin]
		self.valleylane = self._array[self._array < self.vmax]
		self.mainlane = self._array[(self._array > self.vmax) & (self._array < self.pmin)]

	def raise_peaklane(self, factor=None, amount=None):
		if factor is not None:
			self.array[self.array > self.pmin] = self.array[self.array > self.pmin] * factor
		elif amount is not None:
			self.array[self.array > self.pmin] = self.array[self.array > self.pmin] + amount
	
	def raise_valleylane(self, factor=None, amount=None):
		if factor is not None:
			self.array[self.array < self.vmax] = self.array[self.array < self.vmax] * factor
		elif amount is not None:
			self.array[self.array < self.vmax] = self.array[self.array < self.vmax] + amount

	def decrease_peaklane(self, factor=None, amount=None):
		if factor is not None:
			self.array[self.array > self.pmin] = self.array[self.array > self.pmin] / factor
		elif amount is not None:
			self.array[self.array > self.pmin] = self.array[self.array > self.pmin] - amount

	def decrease_valleylane(self, factor=None, amount=None):
		if factor is not None:
			self.array[self.array < self.vmax] = self.array[self.array < self.vmax] / factor
		elif amount is not None:
			self.array[self.array < self.vmax] = self.array[self.array < self.vmax] - amount

	def restore_original(self):
		self.array = self._array

def batched(iterable, n):
	"Batch data into tuples of length n. The last batch may be shorter."
	# batched('ABCDEFG', 3) --> ABC DEF G
	if n < 1:
		raise ValueError('n must be at least one')
	it = iter(iterable)
	while batch := tuple(islice(it, n)):
		yield batch

def abatched(iterable, n):
	"Batch data into arrays of length n. The last batch may be shorter."
	# batched('ABCDEFG', 3) --> ABC DEF G
	if n < 1:
		raise ValueError('n must be at least one')
	it = iter(iterable)
	while batch := tuple(islice(it, n)):
		yield np.array(batch)

def batch(iterable, n):
	return list(batched(iterable, n))

def abatch(iterable, n):
	return list(abatched(iterable, n))

def adimindex(iterable):
	return [list(repeat(i, len(x))) for i, x in enumerate(iterable)]

def apair(iterable: np.ndarray):
	"Pair side by side values into another dimension."
	if len(iterable) % 2 != 0:
		iterable = np.pad(iterable, (0, 1), 'constant', constant_values=(0, 0))
	ibatch = abatched(iterable, 2)
	for b in ibatch:
		yield b

def blur(array: np.ndarray):
	"Blur an array by averaging adjacent values."
	if len(array) % 2 != 0:
		array = np.pad(array, (0, 1), 'constant', constant_values=(0, 0))
	pair = apair(array)
	blurred = np.array([np.mean(i) for i in pair])
	return blurred

def flatten(list_of_lists):
	"Flatten one level of nesting"
	if not hasattr(list_of_lists, '__iter__'):
		return list_of_lists
	return list(chain.from_iterable(list_of_lists))

def slots_filled(iterables: list[list[bool]]):
	"""
	Checks first to make sure there is a unique True value in each iterable,
	then checks to make sure that the position of each True value is unique.

	It has a very niche use case, but it was created to allow an element to be
	checked against multiple conditions, and ensure that there all conditions 
	are matched and each condition is only matched once. 
	i.e. All positions are filled. 

	Example:
	>>> x = [-4, 5, 7, 4, 3, -1]
	>>> y = [43.5, 2.3, 4.5, 6.7, 8.9, 9.0]
	>>> z = [121, 131, 77, 42, 91, 89]
	>>> condition1 = lambda x: x > -100 and x < 100
	>>> condition2 = lambda y: y > 0 and y < 100
	>>> condition3 = lambda z: z > 40 and z < 6000
	>>> xpass = [all([condition1(i)]), all([condition2(i)]), all([condition3(i)]) for i in x]
	[True, False, False]
	>>> ypass = [all([condition1(i)]), all([condition2(i)]), all([condition3(i)]) for i in y]
	[False, True, False]
	>>> zpass = [all([condition1(i)]), all([condition2(i)]), all([condition3(i)]) for i in z]
	[False, False, True]
	>>> slots_filled([xpass, ypass, zpass]) 
	True
	# If True appears more than once in any of the passes, or Trues position is not unique, it will return False.
	
	"""
	truevals = [x.count(True) for x in iterables]
	if truevals != len(iterables):
		return False
	truepos = [x.index(True) for x in iterables]
	if len(set(truepos)) != len(truepos):
		return False
	return True

def isperfectsegment(iterable, n):
	"Check if n is a perfect segment of iterable."
	return len(iterable) % n == 0

def isblockable(iterable, n):
	"Alias of isperfectsegment."
	return isperfectsegment(iterable, n)

def makeblockable(array: np.ndarray, n):
	"Checks if an n can split an array into even chunks, and if not pads the array with zeros."
	if not isperfectsegment(array, n):
		array = np.pad(array, (0, n - len(array) % n), 'constant', constant_values=(0, 0))
	return array

def backsliderange(array: np.ndarray, stride): # God I'm funny.
	return range(
		(len(array)//stride) - (stride - 1)
		)

def backslidewindow(array: np.ndarray, windim, stride): # The window of opportunity to backslide obviously. XD
	array = makeblockable(array, stride)
	cycle = deque(array)
	for _ in backsliderange(array, stride):
		yield np.array(list(cycle)[:windim])
		cycle.rotate(-stride)

def dumpwindow(window): # I'd like to use the toilet please. -- Sorry you've missed your dump window.
	return [i for i in window]

def adumpwindow(window):
	return np.array([i for i in window])

def pairwise(iterable):
	# pairwise('ABCDEFG') --> AB BC CD DE EF FG
	a, b = tee(iterable)
	next(b, None)
	return zip(a, b)

class ADtypes(Enum):
	sound = 'Sound'
	time = 'Time'
	hertz = 'Hertz'
	frequency = 'Frequency'
	mfrequency = 'Multi-Frequency'
	db = 'Decibel'
	pascal = 'Pascal'
	unknown = 'Unknown'

class AirArray(np.lib.mixins.NDArrayOperatorsMixin, np.ndarray):
	"""
	Audio Information Reflection Array

	A subclass of numpy.ndarray that acts as a base class for subclasses specifically designed to represent and handle different types of audio data.
	"""

	def __new__(cls, array=None, atype: ADtypes = ADtypes.sound, dtype=None):
		subtype = None
		for i in array:
			if issubclass(type(i), AirArray):
				subtype = i.__class__
				break
		if isinstance(array, AirArray) or subtype is not None:
			if hasattr(array, 'view'): data = array
			else: data = np.array(array)
			if dtype is None and hasattr(data, 'dtype'): intype = data.dtype
			elif dtype is None: intype = np.dtype(object)
			else: intype = np.dtype(dtype)
			new = data.view(subtype)
			if intype != data.dtype: return new.astype(intype)	   
			new.atype = atype
			new.length = len(new)
			new._carryover = []
			return new
		if not dtype: dtype = np.object_
		if array is not None: obj = np.array(array, dtype=dtype).view(cls)
		else: obj = np.ndarray.__new__(dtype=dtype)
		obj.atype = atype
		obj.length = len(obj)
		obj._carryover = []
		return obj

	def __array_finalize__(self, obj):
		if obj is None: return
		self.length = len(obj)
		self.atype = getattr(obj, 'atype', None)
		self._carryover = getattr(obj, '_carryover', [])
		self.__carryover__(obj)

	def __carryover__(self, other):
		for i in self._carryover:
			old = getattr(other, i, None)
			if old is None: continue
			setattr(self, i, old)

	def __repr__(self):
		return f"{self.__class__.__name__}(\n\tdtype = {self.atype} \n\tshape = {self.shape} \n\tlength = {self.length} \n\tData = {self}\n)"
		
	def __array__(self, dtype=None):
		return np.array(self.Data, dtype=dtype, subok=True)
	
	@property
	def Data(self):
		return self.data
	
	@Data.setter
	def Data(self, value):
		self.data = value.data

	def series(self):
		return pd.Series(self, name=self.dtype.value)
	
	def airlane(self, threshold = None):
		return AirLane(self, threshold)
	
	def airspectrum(self, range_start=50, range_end = 1000):
		AirSpectrum()
		
	def batched(self, n):
		"Batch data into tuples of length n. The last batch may be shorter."
		# batched('ABCDEFG', 3) --> ABC DEF G
		if n < 1:
			raise ValueError('n must be at least one')
		it = iter(self)
		while batch := tuple(islice(it, n)):
			yield batch

	def abatched(self, n):
		"Batch data into arrays of length n. The last batch may be shorter."
		# batched('ABCDEFG', 3) --> ABC DEF G
		if n < 1:
			raise ValueError('n must be at least one')
		it = iter(self)
		while batch := tuple(islice(it, n)):
			yield np.array(batch)
	
	def batch(self, n):
		return list(self.batched(n))
	
	def abatch(self, n):
		return list(self.abatched(n))
	
	def adimindex(self):
		return self.__new__([list(repeat(i, len(x))) for i, x in enumerate(self)])
	
	def apair(self):
		"Pair side by side values into another dimension."
		padded = self
		if len(self.A) % 2 != 0:
			padded = np.pad(self, (0, 1), 'constant', constant_values=(0, 0))
		ibatch = abatched(padded, 2)
		for b in ibatch:
			yield b

	def blur(self):
		"Blur an array by averaging adjacent values."
		padded = self
		if len(self.A) % 2 != 0:
			padded = np.pad(self, (0, 1), 'constant', constant_values=(0, 0))
		pair = apair(padded)
		blurred = self.__new__([np.mean(i) for i in pair])
		return blurred
	
	def deviation_from_mean(self):
		"Deviation from mean."
		return self - self.mean()
	
	def amplify_deviation_from_mean(self, factor=None, amount=None):
		upper = self[self > self.mean()]
		lower = self[self < self.mean()]
		if factor:
			self[self > self.mean()] = upper * factor
			self[self < self.mean()] = lower / factor
		elif amount:
			self[self > self.mean()] = upper + amount
			self[self < self.mean()] = lower - amount

	def relative_amplify_dfm(self, factor=None, amount=None):
		if factor: dev = self.deviation_from_mean() * factor
		elif amount: 
			dev = self.deviation_from_mean()
			dev = dev[dev > 0] + amount
			dev = dev[dev < 0] - amount
		self += dev

	def flatten(self):
		"Flatten one level of nesting"
		if not hasattr(self, '__iter__'):
			return self
		return self.__new__(list(chain.from_iterable(self)), atype=self.atype)
	
	def isperfectsegment(self, n):
		"Check if n is a perfect segment of iterable."
		return len(self) % n == 0
	
	def isblockable(self, n):
		"Alias of isperfectsegment."
		return self.isperfectsegment(n)
	
	def makeblockable(self, n):
		"Pad array to be blockable."
		if self.isblockable(n):
			return self
		else:
			return np.pad(self, (0, n - (len(self) % n)), 'constant', constant_values=(0, 0))
		
	def backsliderange(self, windowlen, stride):
		"Range of indices to slide back."
		return range(0, (
			(len(self) // stride) - (windowlen // stride)) - 1)
	
	def backslidewindow(self, windowlen, stride):
		"Slide back window."
		array = self.makeblockable(stride)
		for _ in self.backsliderange(windowlen, stride):
			array = np.roll(array, -stride)
			yield array[:windowlen]   

	def dumpwindow(self, window):
		"Dump window into array."
		return [i for i in window]
	
	def adumpwindow(self, window):
		"Dump window into array."
		return np.array([i for i in window])
	
	def sliding_window(self, window_size, stride=1):
		'''Create a sliding window on the AirArray instance.
		Args:
			window_size (int): The size of the sliding window.
			stride (int): The stride between each window (default is 1).
		Returns:
			generator: A generator that yields each window as an AirArray object.
		'''
		if window_size < 1 or stride < 1:
			raise ValueError('window_size and stride must be at least 1')
		if len(self) < window_size:
			raise ValueError('window_size must be smaller than or equal to the length of the array')
		block_size = window_size - stride
		self.makeblockable(block_size)
		blocks = self.backslidewindow(window_size, stride)
		for block in blocks:
			yield type(self)(block)

	def valid_timedomain(self):
		return ValidTimeDomain @ self
	
	def valid_freqdomain(self):
		return ValidFrequencyDomain @ self
	
	def valid_dbdomain(self):
		return ValidDecibelDomain @ self
	
	def valid_pascaldomain(self):
		return ValidPascalDomain @ self
	
class AudioDataArray(AirArray):
	def __new__(cls, array=None, atype: ADtypes = None, dtype=None):
		if array is not None: obj = np.array(array).view(cls)
		else: obj = np.ndarray.__new__(dtype=dtype)
		obj.length = len(obj)
		if atype is not None: 
			obj.atype = atype
		elif ValidTimeDomain @ obj:
			obj.atype = ADtypes.time
		elif ValidFrequencyDomain @ obj:
			obj.atype = ADtypes.frequency
		elif ValidDecibelDomain @ obj:
			obj.atype = ADtypes.db
		elif ValidPascalDomain @ obj:
			obj.atype = ADtypes.pascal
		else:
			obj.atype = ADtypes.unknown
		return obj
	
class SoundArray(AirArray):
	def __new__(cls, array=None, atype: ADtypes = ADtypes.sound, dtype=None, rate=None):
		if array is not None: obj = np.array(array).view(cls)
		else: obj = np.ndarray.__new__(dtype=dtype)
		if obj.ndim > 1 and obj.shape[0] == 1: obj = obj.flatten() # Remove the extra outer dimension
		elif obj.shape[0] > 1 and obj.ndim >1: obj = obj.mean(axis=0) # average the channels out, into a 1D array
		obj.atype = atype
		obj._fft = None
		obj._freq = None
		obj._stft = None
		obj.rate = rate
		obj.length = len(obj)
		return obj
	
	@property
	def duration(self):
		return self.length / self.rate
	
	@property
	def duration_ms(self):
		return self.duration * 1000
	
	@property
	def time(self):
		"""Return the time of each frame in milliseconds."""
		return (np.arange(len(np.squeeze(self))) / 48000) * 1000

	@property
	def fft(self):
		if self._fft is None:
			self._fft = np.fft.rfft(self)
		return self._fft
	
	@property
	def fft_amplitudes(self):
		"""Returns the amplitudes (absolute value) of the fft run on this array"""
		if self._freq is None:
			self._freq = np.abs(self.fft)
		return self._freq
	
	@property
	def fft_hertz(self):
		"""Returns the hertz of each frame in the signal array"""
		return np.fft.rfftfreq(self.size, 1) * self.rate
	
	@property
	def stft(self):
		if self._stft is None:
			self._stft = stft(self, self.rate)
		return self._stft
	
	@property
	def stft_amplitudes(self) -> 'PascalArray':
		_, _, amplitudes = self.stft
		return PascalArray(np.abs(amplitudes))
	
	@property
	def stft_hertz(self) -> 'FrequencyArray':
		hertz, _, _ = self.stft
		return FrequencyArray(hertz, rate=self.rate)
	
	@property
	def stft_time(self) -> 'TimeArray':
		_, time, _ = self.stft
		return TimeArray(time, rate=self.rate)

	@property
	def multifrequency(self) -> 'MultiFrequencyArray':
		return MultiFrequencyArray
	
	@property
	def mfreq(self) -> 'MultiFrequencyArray':
		return MultiFrequencyArray
	
	def stft_to_mfreq_hertz(self, win_type='hann', win_size=256, freq_min=None, freq_max=None) -> 'MultiFrequencyArray':
		hertz, time, amplitudes = stft(self, self.rate, window=win_type, nperseg=win_size)
		amplitudes = np.abs(amplitudes)
		if freq_min is not None:
			adjusted_hertz = hertz[hertz >= freq_min]
			i = len(hertz) - len(adjusted_hertz)
			hertz = adjusted_hertz
			amplitudes = amplitudes[i:]
		if freq_max is not None:
			adjusted_hertz = hertz[hertz <= freq_max]
			hertz = adjusted_hertz
			amplitudes = amplitudes[:len(hertz)]
		return MultiFrequencyArray(amplitudes, hertz_freqs = hertz, time_array=time, rate=self.rate, subtype=ADtypes.hertz)

	@property
	def power(self):
		"""
		Returns the power of each frame in the signal array
		∫@time y(t)dt = ∫t y(t) ( dx÷dt ) |x=x(t) dt
		"""
		return np.abs(self.freq) ** 2

	def __array_finalize__(self, obj):
		if obj is None: return
		self.length = len(obj)
		self.rate = getattr(obj, 'rate', None)
		self._fft = None
		self._freq = None
		self._stft = None
		self.atype = getattr(obj, 'atype', None)
		
	def __repr__(self):
		return f"{self.__class__.__name__}(\n\tdtype = {self.atype} \n\tshape = {self.shape} \n\tlength = {self.length} \n\tData = {self}\n)"
		
	def __array__(self, dtype=None):
		return np.array(self.data, dtype=dtype, subok=True)

class FrequencyArray(AirArray): 
	def __new__(cls, array=None, atype: ADtypes = ADtypes.frequency, dtype=None, rate=None, index=None):
		if array is not None: obj = np.array(array).view(cls)
		else: obj = np.ndarray.__new__(dtype=dtype)
		obj.atype = atype
		obj.length = len(obj)
		obj.rate = rate
		obj.index = index
		return obj
	
	def __array_finalize__(self, obj):
		if obj is None: return
		self.length = len(obj)
		self.rate = getattr(obj, 'rate', None)
		self.index = getattr(obj, 'index', None)
		self.atype = getattr(obj, 'atype', None)

	def __repr__(self):
		return f"{self.__class__.__name__}(\n\tatype = {self.atype}, \n\tindex = {self.index} \n\tshape = {self.shape} \n\tlength = {self.length} \n\tFrequency Data = {self}\n)"
	
class HzArray(AirArray):
	def __new__(cls, array=None, time_array=None, atype: ADtypes = ADtypes.frequency, dtype=None, hertz: int=None):
		if dtype is None: dtype = np.object_
		if array is not None: obj = np.array(array, dtype=dtype, subok=True).view(cls)
		else: obj = np.ndarray.__new__(dtype=dtype)
		obj.atype = atype
		obj.hertz = hertz
		obj.length = len(obj)
		obj.amplitudes = obj
		obj.times = time_array
		return obj
	
	def __repr__(self):
		return f"{self.__class__.__name__}(\n\tatype = {self.atype}, \n\thertz = {self.hertz} \n\tshape = {self.shape} \n\tlength = {self.length} \n\tamplitudes = {self}\n)"
	
	def __array_finalize__(self, obj):
		if obj is None: return
		self.length = len(obj)
		self.hertz = getattr(obj, 'hertz', None)
		self.atype = getattr(obj, 'atype', None)
		self.amplitudes = self
		self.times = getattr(obj, 'times', None)

	@property
	def power(self) -> 'float':
		return math.sqrt((1/len(self)) * sum([x**2 for x in self]))

class TimeArray(AirArray):
	def __new__(cls, array=None, atype: ADtypes = ADtypes.time, dtype=None, rate=None):
		if array is not None: obj = np.array(array, subok=True).view(cls)
		else: obj = np.ndarray.__new__(dtype=dtype)
		obj.atype = atype
		obj.length = len(obj)
		obj.rate = rate
		obj.seconds = len(obj) / rate
		obj.milliseconds = obj.seconds * 1000
		obj._ms_array = None
		obj._s_array = None
		return obj
	
	def __array_finalize__(self, obj):
		if obj is None: return
		self.length = len(obj)
		self.rate = getattr(obj, 'rate', None)
		self.atype = getattr(obj, 'atype', None)
		self.seconds = getattr(obj, 'seconds', None)
		self.milliseconds = getattr(obj, 'milliseconds', None)
		self._ms_array = getattr(obj, '_ms_array', None)
		self._s_array = getattr(obj, '_s_array', None)

	@property
	def milliseconds_ts_array(self):
		if self._ms_array is None:
			self._ms_array = np.arange(len(self)) / (self.rate / 1000)
		return self._ms_array
	
	@property
	def seconds_ts_array(self):
		if self._s_array is None:
			self._s_array = np.arange(len(self)) / self.rate
		return self._s_array

	def get_frame_time_ms(self, frame_number):
		return frame_number / (self.rate / 1000)
	
	def TOFm(self, frame_number):
		return self.get_frame_time_ms(frame_number)
	
	def get_frame_time_s(self, frame_number):
		return frame_number / self.rate
	
	def TOFs(self, frame_number):
		return self.get_frame_time_s(frame_number)

class MultiFrequencyArray(AirArray):

	def __new__(
			cls, 
			array=None, 
			time_array: TimeArray=None,
			hertz_freqs: np.ndarray=None,
			atype: ADtypes = ADtypes.mfrequency, 
			dtype=None,
			subtype=ADtypes.hertz,
			frange: tuple=None,
			rate=None
			):
		
		if frange is None and array is None:
			start = 0
			end = 1000
		elif frange is None: 
			start = 0
			end = len(array)
		else: 
			start = frange[0]
			end = frange[1]

		frange = (start, end)

		if array is not None and time_array is not None and hertz_freqs is not None: 
			obj = np.array([HzArray(array[i], hertz=hertz_freqs[i]) for i in range(len(array))], dtype=dtype, subok=True).view(cls)
			obj.subok = True
			obj.time = TimeArray(time_array, rate=rate)
		elif array is not None and time_array is not None:
			obj = np.array([FrequencyArray(array[i], index=i) for i in range(len(array))], dtype=dtype, subok=True).view(cls)
		elif array is not None and hertz_freqs is not None:
			obj = np.array([HzArray(array[i], hertz=hertz_freqs[i]) for i in range(len(array))], dtype=dtype, subok=True).view(cls)
		elif array is not None:
			obj = np.array(array, dtype=dtype, subok=True).view(cls)
		elif time_array is not None:
			obj = np.zeros((frange[1], len(time_array)), dtype=dtype).view(cls)
		else: 
			obj = np.zeros(frange[1], dtype=dtype).view(cls)

		obj.atype = atype
		obj.length = len(obj)
		obj.frange = frange
		obj.frequency_times = TimeArray(time_array, rate=rate) if time_array is not None else None
		obj.rate = rate
		obj.subtype = subtype

		obj._hzdata = hertz_freqs
		obj._data = array
		obj._timedata = time_array
		return obj
	
	def __array_finalize__(self, obj):
		if obj is None: return
		self.length = len(self)
		self.frange = getattr(obj, 'frange', None)
		self.atype = getattr(obj, 'atype', None)
		self.frequency_times = getattr(obj, 'TimeArray', None)
		self.rate = getattr(obj, 'rate', None)
		self.subtype = getattr(obj, 'subtype', None)
		self._hzdata = getattr(obj, '_hzdata', None)
		self._data = getattr(obj, '_data', None)
		self._timedata = getattr(obj, '_timedata', None)
		
		

	def __getitem__(self, index):
		self._getitem = True
		try:
			idx = np.digitize([index], self._hzdata, right=True)[0]
			out = np.ndarray.__getitem__(self, idx)
			if self.subtype == ADtypes.hertz:
				out = np.array(out).view(HzArray)
				out.hertz = self._hzdata[idx]
				out.atype = ADtypes.hertz
			elif self.subtype == ADtypes.frequency:
				out = np.array(out).view(FrequencyArray)
		except:
			out = np.ndarray.__getitem__(self, index)
			"""
			if type(out) == HzArray: return out
			out = HzArray(out, hertz=index+1, atype=ADtypes.frequency)
			setattr(out, 'hertz', index)
			setattr(out, 'atype', ADtypes.frequency)
			setattr(out, 'length', len(out))	
			"""
		finally:
			self._getitem = False

		return out

	def add_frequency(self, hz_frequency: int):
		if self.shape[0] < hz_frequency:
			new_shape = (hz_frequency + 1, self.shape[1]) if len(self.shape) > 1 else (hz_frequency + 1,)
			self.resize(new_shape)

		self[hz_frequency] = HzArray(hertz=hz_frequency, dtype=self.dtype, shape=self.shape[1:])

	def add_frequencies(self, hz_frequencies: list):
		for hz_frequency in hz_frequencies:
			self.add_frequency(hz_frequency)
	
	def add_to_frequency(self, hz: float, value: float, frame: int = None, ms: float = None):
		if frame is None and ms is None:
			self.resize((self.shape[0], self.shape[1] + 1))
			frame = len(self[hz])
		elif frame is None:
			frame = int(ms * (self.frequency_times.rate / 1000))
		frame = frame - 1
		if self.shape[1] < frame:
			new_shape = (self.shape[0], frame + 1)
			self.resize(new_shape)
		self[hz][frame] = value

class DecibelArray(AirArray):

	def __new__(cls, array=None, atype: ADtypes = ADtypes.db, dtype=None):
		if array is not None: obj = np.array(array).view(cls)
		else: obj = np.ndarray.__new__(dtype=dtype)
		obj.atype = atype
		obj.length = len(obj)
		return obj

class PascalArray(AirArray):

	def __new__(cls, array=None, atype: ADtypes = ADtypes.pascal, dtype=None):
		if array is not None: obj = np.array(array).view(cls)
		else: obj = np.ndarray.__new__(dtype=dtype)
		obj.atype = atype
		obj.length = len(obj)
		return obj

class WaveArray:
	audio_array: AirArray = AirArray
	time_array: TimeArray = TimeArray
	frequency_array: FrequencyArray = FrequencyArray
	multi_frequency_array: MultiFrequencyArray = MultiFrequencyArray
	decibel_array: DecibelArray = DecibelArray
	pascal_array: PascalArray = PascalArray
	audioData_array: AudioDataArray = AudioDataArray

@dataclass
class AirMatrix:
	x: AirArray
	y: AirArray
	z: AirArray

	def dict(self):
		return asdict(self)
	
	def __repr__(self):
		return f"AirMatrix(\n\nx={self.x}, \n\ny={self.y}, \n\nz={self.z}\n\n)"
	