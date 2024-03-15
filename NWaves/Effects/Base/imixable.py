from ...wrapper import NWaves 


 

class IMixable:

	def __init__(self, /, *args, **kwargs):
		self._IMixable = NWaves.Effects.Base.IMixable(self, args, kwargs)
		self.Wet = self._IMixable.Wet
		self.Dry = self._IMixable.Dry
 
	def equals(self, obj):
		return self._IMixable.Equals(obj)
 
	def get_hash_code(self, *args, **kwargs):
		return self._IMixable.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._IMixable.GetType(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._IMixable.ToString(*args, **kwargs)
 
	def get_dry(self, *args, **kwargs):
		return self._IMixable.get_Dry(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._IMixable.get_Wet(*args, **kwargs)
 
	def set_dry(self, value):
		return self._IMixable.set_Dry(value)
 
	def set_wet(self, value):
		return self._IMixable.set_Wet(value)