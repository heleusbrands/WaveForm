from ...wrapper import NWaves 


 

class ITransform:

	def __init__(self, /, *args, **kwargs):
		self._ITransform = NWaves.Transforms.Base.ITransform(self, args, kwargs)
		self.Size = self._ITransform.Size
 
	def direct(self, input, output):
		return self._ITransform.Direct(input, output)
 
	def direct_norm(self, input, output):
		return self._ITransform.DirectNorm(input, output)
 
	def equals(self, obj):
		return self._ITransform.Equals(obj)
 
	def get_hash_code(self, *args, **kwargs):
		return self._ITransform.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._ITransform.GetType(*args, **kwargs)
 
	def inverse(self, input, output):
		return self._ITransform.Inverse(input, output)
 
	def inverse_norm(self, input, output):
		return self._ITransform.InverseNorm(input, output)
 
	def to_string(self, *args, **kwargs):
		return self._ITransform.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._ITransform.get_Size(*args, **kwargs)