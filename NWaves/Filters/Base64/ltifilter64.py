from ...wrapper import NWaves 


 

class LtiFilter64:

	def __init__(self, *args, **kwargs):
		self._LtiFilter64 = NWaves.Filters.Base64.LtiFilter64(*args, **kwargs)
		self.Tf = self._LtiFilter64.Tf
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._LtiFilter64.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._LtiFilter64.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._LtiFilter64.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._LtiFilter64.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._LtiFilter64.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._LtiFilter64.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._LtiFilter64.Overloads(*args, **kwargs)
 
	def process(self, sample):
		return self._LtiFilter64.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._LtiFilter64.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._LtiFilter64.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._LtiFilter64.ToString(*args, **kwargs)
 
	def get_tf(self, *args, **kwargs):
		return self._LtiFilter64.get_Tf(*args, **kwargs)
 
	def set_tf(self, value):
		return self._LtiFilter64.set_Tf(value)