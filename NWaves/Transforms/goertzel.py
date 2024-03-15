from ..wrapper import NWaves 


 

class Goertzel:

	def __init__(self, fftSize):
		self._Goertzel = NWaves.Transforms.Goertzel(fftSize)
 
	def direct(self, input, n):
		return self._Goertzel.Direct(input, n)
 
	def equals(self, *args, **kwargs):
		return self._Goertzel.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Goertzel.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Goertzel.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Goertzel.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Goertzel.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, fftSize):
		return self._Goertzel.Overloads(fftSize)
 
	def reference_equals(self, objA, objB):
		return self._Goertzel.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._Goertzel.ToString(*args, **kwargs)