from ..wrapper import NWaves 


 

class Window:

	def __init__(self, *args, **kwargs):
		self._Window = NWaves.Windows.Window(*args, **kwargs)
 
	def bartlett_hann(self, length):
		return self._Window.BartlettHann(length)
 
	def blackman(self, length):
		return self._Window.Blackman(length)
 
	def equals(self, *args, **kwargs):
		return self._Window.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Window.Finalize(*args, **kwargs)
 
	def flattop(self, length):
		return self._Window.Flattop(length)
 
	def gaussian(self, length):
		return self._Window.Gaussian(length)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Window.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Window.GetType(*args, **kwargs)
 
	def hamming(self, length):
		return self._Window.Hamming(length)
 
	def hann(self, length):
		return self._Window.Hann(length)
 
	def kaiser(self, l: int, alpha=12.0):
		return self._Window.Kaiser(length, alpha)
 
	def kbd(self, l: int, alpha=4.0):
		return self._Window.Kbd(length, alpha)
 
	def lanczos(self, length):
		return self._Window.Lanczos(length)
 
	def liftering(self, l: int: int, l: int=22):
		return self._Window.Liftering(length, l)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Window.MemberwiseClone(*args, **kwargs)
 
	def of_type(self, type, length, parameters):
		return self._Window.OfType(type, length, parameters)
 
	def overloads(self, *args, **kwargs):
		return self._Window.Overloads(*args, **kwargs)
 
	def power_of_sine(self, l: int, alpha=1.5):
		return self._Window.PowerOfSine(length, alpha)
 
	def rectangular(self, length):
		return self._Window.Rectangular(length)
 
	def reference_equals(self, objA, objB):
		return self._Window.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._Window.ToString(*args, **kwargs)
 
	def triangular(self, length):
		return self._Window.Triangular(length)