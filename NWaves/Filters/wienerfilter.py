from ..wrapper import NWaves 


 

class WienerFilter:

	def __init__(self, size: int=3, noise=0.0):
		self._WienerFilter = NWaves.Filters.WienerFilter(size, noise)
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._WienerFilter.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._WienerFilter.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._WienerFilter.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._WienerFilter.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._WienerFilter.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._WienerFilter.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, size: int=3, noise=0.0):
		return self._WienerFilter.Overloads(size, noise)
 
	def process(self, sample):
		return self._WienerFilter.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._WienerFilter.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._WienerFilter.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._WienerFilter.ToString(*args, **kwargs)