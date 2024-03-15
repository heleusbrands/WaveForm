from ...wrapper import NWaves 


 

class Fwt:

	def __init__(self, size, wavelet):
		self._Fwt = NWaves.Transforms.Wavelets.Fwt(size, wavelet)
		self.Size = self._Fwt.Size
 
	def get_size(self, *args, **kwargs):
		return self._Fwt.get_Size(self, *args, **kwargs)
 
	def set_size(self, *args, **kwargs):
		return self._Fwt.set_Size(self, *args, **kwargs)
 
	def direct(self, *args, **kwargs):
		return self._Fwt.Direct(self, *args, **kwargs)
 
	def direct_norm(self, *args, **kwargs):
		return self._Fwt.DirectNorm(self, *args, **kwargs)
 
	def inverse(self, *args, **kwargs):
		return self._Fwt.Inverse(self, *args, **kwargs)
 
	def inverse_norm(self, *args, **kwargs):
		return self._Fwt.InverseNorm(self, *args, **kwargs)
 
	def max_level(self, *args, **kwargs):
		return self._Fwt.MaxLevel(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._Fwt.Overloads(self, *args, **kwargs)