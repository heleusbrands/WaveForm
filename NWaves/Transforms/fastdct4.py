from ..wrapper import NWaves 


 

class FastDct4:

	def __init__(self, dctSize):
		self._FastDct4 = NWaves.Transforms.FastDct4(dctSize)
		self.Size = self._FastDct4.Size
 
	def direct(self, input, output):
		return self._FastDct4.Direct(input, output)
 
	def direct_norm(self, input, output):
		return self._FastDct4.DirectNorm(input, output)
 
	def equals(self, *args, **kwargs):
		return self._FastDct4.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._FastDct4.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._FastDct4.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._FastDct4.GetType(*args, **kwargs)
 
	def inverse(self, input, output):
		return self._FastDct4.Inverse(input, output)
 
	def inverse_norm(self, input, output):
		return self._FastDct4.InverseNorm(input, output)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._FastDct4.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, dctSize):
		return self._FastDct4.Overloads(dctSize)
 
	def reference_equals(self, objA, objB):
		return self._FastDct4.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._FastDct4.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._FastDct4.get_Size(*args, **kwargs)