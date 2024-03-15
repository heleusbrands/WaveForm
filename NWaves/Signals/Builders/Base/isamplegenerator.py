from ....wrapper import NWaves 


 

class ISampleGenerator:

	def __init__(self, /, *args, **kwargs):
		self._ISampleGenerator = NWaves.Signals.Builders.Base.ISampleGenerator(self, args, kwargs)
 
	def equals(self, obj):
		return self._ISampleGenerator.Equals(obj)
 
	def get_hash_code(self, *args, **kwargs):
		return self._ISampleGenerator.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._ISampleGenerator.GetType(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._ISampleGenerator.NextSample(*args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._ISampleGenerator.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._ISampleGenerator.ToString(*args, **kwargs)