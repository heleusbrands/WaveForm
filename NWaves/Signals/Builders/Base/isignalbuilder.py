from ....wrapper import NWaves 


 

class ISignalBuilder:

	def __init__(self, /, *args, **kwargs):
		self._ISignalBuilder = NWaves.Signals.Builders.Base.ISignalBuilder(self, args, kwargs)
		self.Length = self._ISignalBuilder.Length
 
	def build(self, *args, **kwargs):
		return self._ISignalBuilder.Build(*args, **kwargs)
 
	def equals(self, obj):
		return self._ISignalBuilder.Equals(obj)
 
	def get_hash_code(self, *args, **kwargs):
		return self._ISignalBuilder.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._ISignalBuilder.GetType(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._ISignalBuilder.ToString(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._ISignalBuilder.get_Length(*args, **kwargs)