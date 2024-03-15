from ...wrapper import NWaves 


 

class IFilter64:

	def __init__(self, /, *args, **kwargs):
		self._IFilter64 = NWaves.Filters.Base64.IFilter64(self, args, kwargs)
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._IFilter64.ApplyTo(signal, method)
 
	def equals(self, obj):
		return self._IFilter64.Equals(obj)
 
	def get_hash_code(self, *args, **kwargs):
		return self._IFilter64.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._IFilter64.GetType(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._IFilter64.ToString(*args, **kwargs)