from ..wrapper import NWaves 


 

class HilbertTransform64:

	def __init__(self, size: int=512):
		self._HilbertTransform64 = NWaves.Transforms.HilbertTransform64(size)
		self.Size = self._HilbertTransform64.Size
 
	def analytic_signal(self, input):
		return self._HilbertTransform64.AnalyticSignal(input)
 
	def direct(self, input, output):
		return self._HilbertTransform64.Direct(input, output)
 
	def direct_norm(self, input, output):
		return self._HilbertTransform64.DirectNorm(input, output)
 
	def equals(self, *args, **kwargs):
		return self._HilbertTransform64.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._HilbertTransform64.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._HilbertTransform64.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._HilbertTransform64.GetType(*args, **kwargs)
 
	def inverse(self, input, output):
		return self._HilbertTransform64.Inverse(input, output)
 
	def inverse_norm(self, input, output):
		return self._HilbertTransform64.InverseNorm(input, output)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._HilbertTransform64.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, size: int=512):
		return self._HilbertTransform64.Overloads(size)
 
	def reference_equals(self, objA, objB):
		return self._HilbertTransform64.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._HilbertTransform64.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._HilbertTransform64.get_Size(*args, **kwargs)