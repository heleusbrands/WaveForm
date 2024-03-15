from ..wrapper import NWaves 


 

class FastMdct:

	def __init__(self, dctSize):
		self._FastMdct = NWaves.Transforms.FastMdct(dctSize)
		self.Size = self._FastMdct.Size
 
	def direct(self, input, output):
		return self._FastMdct.Direct(input, output)
 
	def direct_norm(self, input, output):
		return self._FastMdct.DirectNorm(input, output)
 
	def equals(self, *args, **kwargs):
		return self._FastMdct.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._FastMdct.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._FastMdct.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._FastMdct.GetType(*args, **kwargs)
 
	def inverse(self, input, output):
		return self._FastMdct.Inverse(input, output)
 
	def inverse_norm(self, input, output):
		return self._FastMdct.InverseNorm(input, output)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._FastMdct.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, dctSize):
		return self._FastMdct.Overloads(dctSize)
 
	def reference_equals(self, objA, objB):
		return self._FastMdct.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._FastMdct.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._FastMdct.get_Size(*args, **kwargs)