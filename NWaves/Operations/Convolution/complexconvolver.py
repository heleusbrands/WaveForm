from ...wrapper import NWaves 


 

class ComplexConvolver:

	def __init__(self, *args, **kwargs):
		self._ComplexConvolver = NWaves.Operations.Convolution.ComplexConvolver(*args, **kwargs)
 
	def convolve(self, signal, kernel, fftSize: int=0):
		return self._ComplexConvolver.Convolve(signal, kernel, fftSize)
 
	def cross_correlate(self, signal, kernel, fftSize: int=0):
		return self._ComplexConvolver.CrossCorrelate(signal, kernel, fftSize)
 
	def deconvolve(self, signal, kernel, fftSize: int=0):
		return self._ComplexConvolver.Deconvolve(signal, kernel, fftSize)
 
	def equals(self, *args, **kwargs):
		return self._ComplexConvolver.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._ComplexConvolver.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._ComplexConvolver.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._ComplexConvolver.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._ComplexConvolver.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._ComplexConvolver.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._ComplexConvolver.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._ComplexConvolver.ToString(*args, **kwargs)