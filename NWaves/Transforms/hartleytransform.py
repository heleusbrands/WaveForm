from ..wrapper import NWaves 


 

class HartleyTransform:

	def __init__(self, size):
		self._HartleyTransform = NWaves.Transforms.HartleyTransform(size)
		self.Size = self._HartleyTransform.Size
 
	def direct(self, *args, **kwargs):
		return self._HartleyTransform.Direct(*args, **kwargs)
 
	def direct_norm(self, input, output):
		return self._HartleyTransform.DirectNorm(input, output)
 
	def equals(self, *args, **kwargs):
		return self._HartleyTransform.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._HartleyTransform.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._HartleyTransform.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._HartleyTransform.GetType(*args, **kwargs)
 
	def inverse(self, *args, **kwargs):
		return self._HartleyTransform.Inverse(*args, **kwargs)
 
	def inverse_norm(self, *args, **kwargs):
		return self._HartleyTransform.InverseNorm(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._HartleyTransform.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, size):
		return self._HartleyTransform.Overloads(size)
 
	def reference_equals(self, objA, objB):
		return self._HartleyTransform.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._HartleyTransform.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._HartleyTransform.get_Size(*args, **kwargs)