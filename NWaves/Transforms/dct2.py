from ..wrapper import NWaves 


 

class Dct2:

	def __init__(self, dctSize):
		self._Dct2 = NWaves.Transforms.Dct2(dctSize)
		self.Size = self._Dct2.Size
 
	def direct(self, input, output):
		return self._Dct2.Direct(input, output)
 
	def direct_norm(self, input, output):
		return self._Dct2.DirectNorm(input, output)
 
	def equals(self, *args, **kwargs):
		return self._Dct2.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Dct2.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Dct2.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Dct2.GetType(*args, **kwargs)
 
	def inverse(self, input, output):
		return self._Dct2.Inverse(input, output)
 
	def inverse_norm(self, input, output):
		return self._Dct2.InverseNorm(input, output)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Dct2.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, dctSize):
		return self._Dct2.Overloads(dctSize)
 
	def reference_equals(self, objA, objB):
		return self._Dct2.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._Dct2.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._Dct2.get_Size(*args, **kwargs)