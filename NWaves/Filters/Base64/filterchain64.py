from ...wrapper import NWaves 


 

class FilterChain64:

	def __init__(self, *args, **kwargs):
		self._FilterChain64 = NWaves.Filters.Base64.FilterChain64(*args, **kwargs)
 
	def add(self, filter):
		return self._FilterChain64.Add(filter)
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._FilterChain64.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._FilterChain64.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._FilterChain64.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._FilterChain64.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._FilterChain64.GetType(*args, **kwargs)
 
	def insert(self, index, filter):
		return self._FilterChain64.Insert(index, filter)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._FilterChain64.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._FilterChain64.Overloads(*args, **kwargs)
 
	def process(self, sample):
		return self._FilterChain64.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._FilterChain64.ReferenceEquals(objA, objB)
 
	def remove_at(self, index):
		return self._FilterChain64.RemoveAt(index)
 
	def reset(self, *args, **kwargs):
		return self._FilterChain64.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._FilterChain64.ToString(*args, **kwargs)