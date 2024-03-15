from ..wrapper import NWaves 


 

class FastDct2:

	def __init__(self, dctSize):
		self._FastDct2 = NWaves.Transforms.FastDct2(dctSize)
		self.Size = self._FastDct2.Size
 
	def direct(self, input, output):
		return self._FastDct2.Direct(input, output)
 
	def direct_norm(self, input, output):
		return self._FastDct2.DirectNorm(input, output)
 
	def equals(self, *args, **kwargs):
		return self._FastDct2.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._FastDct2.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._FastDct2.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._FastDct2.GetType(*args, **kwargs)
 
	def inverse(self, input, output):
		return self._FastDct2.Inverse(input, output)
 
	def inverse_norm(self, input, output):
		return self._FastDct2.InverseNorm(input, output)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._FastDct2.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, dctSize):
		return self._FastDct2.Overloads(dctSize)
 
	def reference_equals(self, objA, objB):
		return self._FastDct2.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._FastDct2.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._FastDct2.get_Size(*args, **kwargs)