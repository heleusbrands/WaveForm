from ..wrapper import NWaves 


 

class IDct:

	def __init__(self, /, *args, **kwargs):
		self._IDct = NWaves.Transforms.IDct(self, args, kwargs)
		self.Size = self._IDct.Size
 
	def direct(self, input, output):
		return self._IDct.Direct(input, output)
 
	def direct_norm(self, input, output):
		return self._IDct.DirectNorm(input, output)
 
	def equals(self, obj):
		return self._IDct.Equals(obj)
 
	def get_hash_code(self, *args, **kwargs):
		return self._IDct.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._IDct.GetType(*args, **kwargs)
 
	def inverse(self, input, output):
		return self._IDct.Inverse(input, output)
 
	def inverse_norm(self, input, output):
		return self._IDct.InverseNorm(input, output)
 
	def to_string(self, *args, **kwargs):
		return self._IDct.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._IDct.get_Size(*args, **kwargs)