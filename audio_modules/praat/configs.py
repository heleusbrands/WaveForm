import numpy as np
import pandas as pd
from parselmouth import Sound, SpectralAnalysisWindowShape
from parselmouth.praat import call
from enum import Enum
#from ..types import *

from pydantic.v1 import PositiveFloat, BaseModel, dataclasses
"""
class WaveDtype(Enum):
	sound = 'Sound'
	time = 'Time'
	frequency = 'Frequency'
	mfrequency = 'Multi-Frequency'
	db = 'Decibel'
	pascal = 'Pascal'
	unknown = 'Unknown'

class AirArray(np.ndarray):

	def __new__(cls, array=None, atype: WaveDtype = WaveDtype.sound, dtype=None):
		if array: obj = np.array(array).view(cls)
		else: obj = np.ndarray.__new__(dtype=dtype)
		obj.atype = atype
		obj.length = len(obj)
		return obj

	def __array_finalize__(self, obj):
		if obj is None: return
		self.length = len(obj)
		self.atype = getattr(obj, 'atype', None)

	def __repr__(self):
		return f"{self.__class__.__name__}(\n\tdtype = {self.atype} \n\tshape = {self.shape} \n\tlength = {self.length} \n\tData = {self}\n)"
		
	def __array__(self, dtype=None):
		return np.array(self.data, dtype=dtype)
	
	def series(self):
		return pd.Series(self.data, name=self.dtype.value)

class AudioDataArray(AirArray):
	def __new__(cls, array=None, atype: WaveDtype = None, dtype=None):
		if array: obj = np.array(array).view(cls)
		else: obj = np.ndarray.__new__(dtype=dtype)
		obj.length = len(obj)
		if atype is not None: 
			obj.atype = atype
		elif ValidTimeDomain @ obj:
			obj.atype = WaveDtype.time
		elif ValidFrequencyDomain @ obj:
			obj.atype = WaveDtype.frequency
		elif ValidDecibelDomain @ obj:
			obj.atype = WaveDtype.db
		elif ValidPascalDomain @ obj:
			obj.atype = WaveDtype.pascal
		else:
			obj.atype = WaveDtype.unknown
		return obj

class FrequencyArray(AirArray): 
	def __new__(cls, array=None, atype: WaveDtype = WaveDtype.frequency, dtype=None):
		if array: obj = np.array(array).view(cls)
		else: obj = np.ndarray.__new__(dtype=dtype)
		obj.atype = atype
		obj.length = len(obj)
		return obj

class TimeArray(AirArray):
	def __new__(cls, array=None, atype: WaveDtype = WaveDtype.time, dtype=None):
		if array: obj = np.array(array).view(cls)
		else: obj = np.ndarray.__new__(dtype=dtype)
		obj.atype = atype
		obj.length = len(obj)
		return obj

class MultiFrequencyArray(AirArray):
	def __new__(cls, array=None, atype: WaveDtype = WaveDtype.mfrequency, dtype=None):
		if array: obj = np.array(array).view(cls)
		else: obj = np.ndarray.__new__(dtype=dtype)
		obj.atype = atype
		obj.length = len(obj)
		return obj

class DecibelArray(AirArray):
	def __new__(cls, array=None, atype: WaveDtype = WaveDtype.db, dtype=None):
		if array: obj = np.array(array).view(cls)
		else: obj = np.ndarray.__new__(dtype=dtype)
		obj.atype = atype
		obj.length = len(obj)
		return obj

class PascalArray(AirArray):
	def __new__(cls, array=None, atype: WaveDtype = WaveDtype.pascal, dtype=None):
		if array: obj = np.array(array).view(cls)
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
	audio_data_array: AudioDataArray = AudioDataArray
"""

class SpectrogramBaseData:
	power: np.ndarray
	frequency: np.ndarray
	time: np.ndarray

	def dict(self): # BaseData classes need a dict method for dataframe conversion
		return {k: v for k, v in self.__dict__.items() if k.startswith('_') is False}

class BasicWindowData:
	def __init__(self, spec):
		self._spec = spec
	
		self.number_of_frames: int = call(self._spec, "Get number of frames")
		self.start_time: PositiveFloat = call(self._spec, "Get start time")
		self.end_time: PositiveFloat = call(self._spec, "Get end time")
		self.total_duration: PositiveFloat = call(self._spec, "Get total duration")

class WindowTypes(Enum):
	square: str = 'square (rectangular)'
	hamming: str = 'Hamming (raised sine-squared)'
	bartlett: str = 'Bartlett (triangular)'
	welch: str = 'Welch (parabolic)'
	hanning: str = 'Hanning (sine-squared)'
	gaussian: str = 'Gaussian'

_PMMAPPINGS = {
	'square (rectangular)': SpectralAnalysisWindowShape.SQUARE,
	'Hamming (raised sine-squared)': SpectralAnalysisWindowShape.HAMMING,
	'Bartlett (triangular)': SpectralAnalysisWindowShape.BARTLETT,
	'Welch (parabolic)': SpectralAnalysisWindowShape.WELCH,
	'Hanning (sine-squared)': SpectralAnalysisWindowShape.HANNING,
	'Gaussian': SpectralAnalysisWindowShape.GAUSSIAN
}

class WindowConfig:
	_pmtypes = _PMMAPPINGS
	window_length: PositiveFloat = 0.005
	time_step: PositiveFloat = 0.002
	max_frequency: PositiveFloat = 5500
	frequency_step: PositiveFloat = 20
	window_shape: WindowTypes = WindowTypes.gaussian


class PeakStatistics:
	relative_minima: np.ndarray
	relative_maxima: np.ndarray
	relative_extrema: np.ndarray
	prominence: np.ndarray
	left_bases: np.ndarray
	right_bases: np.ndarray
	widths: np.ndarray
	width_heights: np.ndarray
	left_ips: np.ndarray
	right_ips: np.ndarray
	
	def dict(self): # BaseData classes need a dict method for dataframe conversion
		return {k: v for k, v in self.__dict__.items() if k.startswith('_') is False}


class FormantGrid:
	stack: np.ndarray = None

	def as_dict(self):
		return {k: v for k, v in self.__dict__.items() if (not k.startswith('_') and k != 'stack')}


class FormantStats:
	min: float
	max: float
	mean: float
	min_max_range: float
	peaks: dict

	def as_dict(self):
		return {k: v for k, v in self.__dict__.items() if k.startswith('_') is False}


class Formant:
	formant_id: int
	data: np.ndarray
	stats: FormantStats = None

	def as_dict(self):
		return {k: v for k, v in self.__dict__.items() if k.startswith('_') is False}