from ...wrapper import NWaves 


 

class StereoFilter64:

	def __init__(self, filterLeft, filterRight):
		self._StereoFilter64 = NWaves.Filters.Base64.StereoFilter64(filterLeft, filterRight)
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._StereoFilter64.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._StereoFilter64.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._StereoFilter64.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._StereoFilter64.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._StereoFilter64.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._StereoFilter64.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, filterLeft, filterRight):
		return self._StereoFilter64.Overloads(filterLeft, filterRight)
 
	def process(self, sample):
		return self._StereoFilter64.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._StereoFilter64.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._StereoFilter64.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._StereoFilter64.ToString(*args, **kwargs)