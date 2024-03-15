from ..wrapper import NWaves 


 

class FastDct3:

	def __init__(self, dctSize):
		self._FastDct3 = NWaves.Transforms.FastDct3(dctSize)
		self.Size = self._FastDct3.Size
 
	def direct(self, input, output):
		return self._FastDct3.Direct(input, output)
 
	def direct_norm(self, input, output):
		return self._FastDct3.DirectNorm(input, output)
 
	def equals(self, *args, **kwargs):
		return self._FastDct3.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._FastDct3.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._FastDct3.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._FastDct3.GetType(*args, **kwargs)
 
	def inverse(self, input, output):
		return self._FastDct3.Inverse(input, output)
 
	def inverse_norm(self, input, output):
		return self._FastDct3.InverseNorm(input, output)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._FastDct3.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, dctSize):
		return self._FastDct3.Overloads(dctSize)
 
	def reference_equals(self, objA, objB):
		return self._FastDct3.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._FastDct3.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._FastDct3.get_Size(*args, **kwargs)