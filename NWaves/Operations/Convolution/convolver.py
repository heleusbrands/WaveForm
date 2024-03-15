from ...wrapper import NWaves 


 

class Convolver:

	def __init__(self, fftSize: int=0):
		self._Convolver = NWaves.Operations.Convolution.Convolver(fftSize)
 
	def convolve(self, *args, **kwargs):
		return self._Convolver.Convolve(*args, **kwargs)
 
	def cross_correlate(self, *args, **kwargs):
		return self._Convolver.CrossCorrelate(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._Convolver.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Convolver.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Convolver.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Convolver.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Convolver.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, fftSize: int=0):
		return self._Convolver.Overloads(fftSize)
 
	def reference_equals(self, objA, objB):
		return self._Convolver.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._Convolver.ToString(*args, **kwargs)