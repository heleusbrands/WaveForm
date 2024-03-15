from ..wrapper import NWaves 


 

class RealFft:

	def __init__(self, size):
		self._RealFft = NWaves.Transforms.RealFft(size)
		self.Size = self._RealFft.Size
 
	def direct(self, *args, **kwargs):
		return self._RealFft.Direct(*args, **kwargs)
 
	def direct_norm(self, inRe, inIm, outRe, outIm):
		return self._RealFft.DirectNorm(inRe, inIm, outRe, outIm)
 
	def equals(self, *args, **kwargs):
		return self._RealFft.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._RealFft.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._RealFft.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._RealFft.GetType(*args, **kwargs)
 
	def inverse(self, *args, **kwargs):
		return self._RealFft.Inverse(*args, **kwargs)
 
	def inverse_norm(self, *args, **kwargs):
		return self._RealFft.InverseNorm(*args, **kwargs)
 
	def magnitude_spectrum(self, *args, **kwargs):
		return self._RealFft.MagnitudeSpectrum(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._RealFft.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, size):
		return self._RealFft.Overloads(size)
 
	def power_spectrum(self, *args, **kwargs):
		return self._RealFft.PowerSpectrum(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._RealFft.ReferenceEquals(objA, objB)
 
	def shift(self, samples):
		return self._RealFft.Shift(samples)
 
	def to_string(self, *args, **kwargs):
		return self._RealFft.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._RealFft.get_Size(*args, **kwargs)