from ...wrapper import NWaves 


 

class FilterChain:

	def __init__(self, *args, **kwargs):
		self._FilterChain = NWaves.Filters.Base.FilterChain(*args, **kwargs)
 
	def add(self, filter):
		return self._FilterChain.Add(filter)
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._FilterChain.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._FilterChain.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._FilterChain.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._FilterChain.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._FilterChain.GetType(*args, **kwargs)
 
	def insert(self, index, filter):
		return self._FilterChain.Insert(index, filter)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._FilterChain.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._FilterChain.Overloads(*args, **kwargs)
 
	def process(self, sample):
		return self._FilterChain.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._FilterChain.ReferenceEquals(objA, objB)
 
	def remove_at(self, index):
		return self._FilterChain.RemoveAt(index)
 
	def reset(self, *args, **kwargs):
		return self._FilterChain.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._FilterChain.ToString(*args, **kwargs)