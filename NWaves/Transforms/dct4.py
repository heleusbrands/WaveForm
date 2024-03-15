from ..wrapper import NWaves 


 

class Dct4:

	def __init__(self, dctSize):
		self._Dct4 = NWaves.Transforms.Dct4(dctSize)
		self.Size = self._Dct4.Size
 
	def direct(self, input, output):
		return self._Dct4.Direct(input, output)
 
	def direct_norm(self, input, output):
		return self._Dct4.DirectNorm(input, output)
 
	def equals(self, *args, **kwargs):
		return self._Dct4.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Dct4.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Dct4.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Dct4.GetType(*args, **kwargs)
 
	def inverse(self, input, output):
		return self._Dct4.Inverse(input, output)
 
	def inverse_norm(self, input, output):
		return self._Dct4.InverseNorm(input, output)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Dct4.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, dctSize):
		return self._Dct4.Overloads(dctSize)
 
	def reference_equals(self, objA, objB):
		return self._Dct4.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._Dct4.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._Dct4.get_Size(*args, **kwargs)