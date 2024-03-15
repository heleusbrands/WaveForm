from ...wrapper import NWaves 


 

class IOnlineFilter64:

	def __init__(self, /, *args, **kwargs):
		self._IOnlineFilter64 = NWaves.Filters.Base64.IOnlineFilter64(self, args, kwargs)
 
	def equals(self, obj):
		return self._IOnlineFilter64.Equals(obj)
 
	def get_hash_code(self, *args, **kwargs):
		return self._IOnlineFilter64.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._IOnlineFilter64.GetType(*args, **kwargs)
 
	def process(self, sample):
		return self._IOnlineFilter64.Process(sample)
 
	def reset(self, *args, **kwargs):
		return self._IOnlineFilter64.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._IOnlineFilter64.ToString(*args, **kwargs)