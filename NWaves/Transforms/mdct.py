from ..wrapper import NWaves 


 

class Mdct:

	def __init__(self, dctSize, dct=None):
		self._Mdct = NWaves.Transforms.Mdct(dctSize, dct)
		self.Size = self._Mdct.Size
 
	def direct(self, input, output):
		return self._Mdct.Direct(input, output)
 
	def direct_norm(self, input, output):
		return self._Mdct.DirectNorm(input, output)
 
	def equals(self, *args, **kwargs):
		return self._Mdct.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Mdct.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Mdct.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Mdct.GetType(*args, **kwargs)
 
	def inverse(self, input, output):
		return self._Mdct.Inverse(input, output)
 
	def inverse_norm(self, input, output):
		return self._Mdct.InverseNorm(input, output)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Mdct.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, dctSize, dct=None):
		return self._Mdct.Overloads(dctSize, dct)
 
	def reference_equals(self, objA, objB):
		return self._Mdct.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._Mdct.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._Mdct.get_Size(*args, **kwargs)