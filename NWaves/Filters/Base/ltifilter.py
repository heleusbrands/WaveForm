from ...wrapper import NWaves 


 

class LtiFilter:

	def __init__(self, *args, **kwargs):
		self._LtiFilter = NWaves.Filters.Base.LtiFilter(*args, **kwargs)
		self.Tf = self._LtiFilter.Tf
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._LtiFilter.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._LtiFilter.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._LtiFilter.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._LtiFilter.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._LtiFilter.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._LtiFilter.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._LtiFilter.Overloads(*args, **kwargs)
 
	def process(self, sample):
		return self._LtiFilter.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._LtiFilter.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._LtiFilter.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._LtiFilter.ToString(*args, **kwargs)
 
	def get_tf(self, *args, **kwargs):
		return self._LtiFilter.get_Tf(*args, **kwargs)
 
	def set_tf(self, value):
		return self._LtiFilter.set_Tf(value)