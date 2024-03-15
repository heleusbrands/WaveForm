from ..wrapper import NWaves 


 

class Dct1:

	def __init__(self, dctSize):
		self._Dct1 = NWaves.Transforms.Dct1(dctSize)
		self.Size = self._Dct1.Size
 
	def direct(self, input, output):
		return self._Dct1.Direct(input, output)
 
	def direct_norm(self, input, output):
		return self._Dct1.DirectNorm(input, output)
 
	def equals(self, *args, **kwargs):
		return self._Dct1.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Dct1.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Dct1.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Dct1.GetType(*args, **kwargs)
 
	def inverse(self, input, output):
		return self._Dct1.Inverse(input, output)
 
	def inverse_norm(self, input, output):
		return self._Dct1.InverseNorm(input, output)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Dct1.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, dctSize):
		return self._Dct1.Overloads(dctSize)
 
	def reference_equals(self, objA, objB):
		return self._Dct1.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._Dct1.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._Dct1.get_Size(*args, **kwargs)