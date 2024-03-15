from ..wrapper import NWaves 


 

class Perceptual:

	def __init__(self, *args, **kwargs):
		self._Perceptual = NWaves.Features.Perceptual(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._Perceptual.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Perceptual.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Perceptual.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Perceptual.GetType(*args, **kwargs)
 
	def loudness(self, spectralBands):
		return self._Perceptual.Loudness(spectralBands)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Perceptual.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._Perceptual.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._Perceptual.ReferenceEquals(objA, objB)
 
	def sharpness(self, spectralBands):
		return self._Perceptual.Sharpness(spectralBands)
 
	def to_string(self, *args, **kwargs):
		return self._Perceptual.ToString(*args, **kwargs)