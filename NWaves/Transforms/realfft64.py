from ..wrapper import NWaves 


 

class RealFft64:

	def __init__(self, size):
		self._RealFft64 = NWaves.Transforms.RealFft64(size)
		self.Size = self._RealFft64.Size
 
	def direct(self, *args, **kwargs):
		return self._RealFft64.Direct(*args, **kwargs)
 
	def direct_norm(self, inRe, inIm, outRe, outIm):
		return self._RealFft64.DirectNorm(inRe, inIm, outRe, outIm)
 
	def equals(self, *args, **kwargs):
		return self._RealFft64.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._RealFft64.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._RealFft64.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._RealFft64.GetType(*args, **kwargs)
 
	def inverse(self, *args, **kwargs):
		return self._RealFft64.Inverse(*args, **kwargs)
 
	def inverse_norm(self, *args, **kwargs):
		return self._RealFft64.InverseNorm(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._RealFft64.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, size):
		return self._RealFft64.Overloads(size)
 
	def reference_equals(self, objA, objB):
		return self._RealFft64.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._RealFft64.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._RealFft64.get_Size(*args, **kwargs)