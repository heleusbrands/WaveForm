from ...wrapper import NWaves 


 

class IFilter:

	def __init__(self, /, *args, **kwargs):
		self._IFilter = NWaves.Filters.Base.IFilter(self, args, kwargs)
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._IFilter.ApplyTo(signal, method)
 
	def equals(self, obj):
		return self._IFilter.Equals(obj)
 
	def get_hash_code(self, *args, **kwargs):
		return self._IFilter.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._IFilter.GetType(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._IFilter.ToString(*args, **kwargs)