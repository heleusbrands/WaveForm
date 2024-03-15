from ..wrapper import NWaves 


 

class HilbertTransform:

	def __init__(self, size: int=512):
		self._HilbertTransform = NWaves.Transforms.HilbertTransform(size)
		self.Size = self._HilbertTransform.Size
 
	def analytic_signal(self, input):
		return self._HilbertTransform.AnalyticSignal(input)
 
	def direct(self, input, output):
		return self._HilbertTransform.Direct(input, output)
 
	def direct_norm(self, input, output):
		return self._HilbertTransform.DirectNorm(input, output)
 
	def equals(self, *args, **kwargs):
		return self._HilbertTransform.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._HilbertTransform.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._HilbertTransform.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._HilbertTransform.GetType(*args, **kwargs)
 
	def inverse(self, input, output):
		return self._HilbertTransform.Inverse(input, output)
 
	def inverse_norm(self, input, output):
		return self._HilbertTransform.InverseNorm(input, output)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._HilbertTransform.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, size: int=512):
		return self._HilbertTransform.Overloads(size)
 
	def reference_equals(self, objA, objB):
		return self._HilbertTransform.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._HilbertTransform.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._HilbertTransform.get_Size(*args, **kwargs)