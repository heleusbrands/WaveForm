from ...wrapper import NWaves 


 

class IOnlineFilter:

	def __init__(self, /, *args, **kwargs):
		self._IOnlineFilter = NWaves.Filters.Base.IOnlineFilter(self, args, kwargs)
 
	def equals(self, obj):
		return self._IOnlineFilter.Equals(obj)
 
	def get_hash_code(self, *args, **kwargs):
		return self._IOnlineFilter.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._IOnlineFilter.GetType(*args, **kwargs)
 
	def process(self, sample):
		return self._IOnlineFilter.Process(sample)
 
	def reset(self, *args, **kwargs):
		return self._IOnlineFilter.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._IOnlineFilter.ToString(*args, **kwargs)