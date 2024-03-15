from ..wrapper import NWaves 


 

class Fft:

	def __init__(self, fftSize: int=512):
		self._Fft = NWaves.Transforms.Fft(fftSize)
		self.Size = self._Fft.Size
 
	def direct(self, *args, **kwargs):
		return self._Fft.Direct(*args, **kwargs)
 
	def direct_norm(self, inRe, inIm, outRe, outIm):
		return self._Fft.DirectNorm(inRe, inIm, outRe, outIm)
 
	def equals(self, *args, **kwargs):
		return self._Fft.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Fft.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Fft.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Fft.GetType(*args, **kwargs)
 
	def inverse(self, *args, **kwargs):
		return self._Fft.Inverse(*args, **kwargs)
 
	def inverse_norm(self, *args, **kwargs):
		return self._Fft.InverseNorm(*args, **kwargs)
 
	def magnitude_spectrum(self, *args, **kwargs):
		return self._Fft.MagnitudeSpectrum(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Fft.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, fftSize: int=512):
		return self._Fft.Overloads(fftSize)
 
	def power_spectrum(self, *args, **kwargs):
		return self._Fft.PowerSpectrum(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._Fft.ReferenceEquals(objA, objB)
 
	def shift(self, samples):
		return self._Fft.Shift(samples)
 
	def to_string(self, *args, **kwargs):
		return self._Fft.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._Fft.get_Size(*args, **kwargs)