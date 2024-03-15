from ..wrapper import NWaves 


 

class Fft64:

	def __init__(self, fftSize: int=512):
		self._Fft64 = NWaves.Transforms.Fft64(fftSize)
		self.Size = self._Fft64.Size
 
	def direct(self, *args, **kwargs):
		return self._Fft64.Direct(*args, **kwargs)
 
	def direct_norm(self, inRe, inIm, outRe, outIm):
		return self._Fft64.DirectNorm(inRe, inIm, outRe, outIm)
 
	def equals(self, *args, **kwargs):
		return self._Fft64.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Fft64.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Fft64.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Fft64.GetType(*args, **kwargs)
 
	def inverse(self, *args, **kwargs):
		return self._Fft64.Inverse(*args, **kwargs)
 
	def inverse_norm(self, *args, **kwargs):
		return self._Fft64.InverseNorm(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Fft64.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, fftSize: int=512):
		return self._Fft64.Overloads(fftSize)
 
	def reference_equals(self, objA, objB):
		return self._Fft64.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._Fft64.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._Fft64.get_Size(*args, **kwargs)