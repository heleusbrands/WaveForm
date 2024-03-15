from ...wrapper import NWaves 


 

class StereoFilter:

	def __init__(self, filterLeft, filterRight):
		self._StereoFilter = NWaves.Filters.Base.StereoFilter(filterLeft, filterRight)
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._StereoFilter.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._StereoFilter.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._StereoFilter.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._StereoFilter.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._StereoFilter.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._StereoFilter.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, filterLeft, filterRight):
		return self._StereoFilter.Overloads(filterLeft, filterRight)
 
	def process(self, sample):
		return self._StereoFilter.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._StereoFilter.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._StereoFilter.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._StereoFilter.ToString(*args, **kwargs)