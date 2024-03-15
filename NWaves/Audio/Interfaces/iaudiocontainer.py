from ...wrapper import NWaves 


 

class IAudioContainer:

	def __init__(self, /, *args, **kwargs):
		self._IAudioContainer = NWaves.Audio.Interfaces.IAudioContainer(self, args, kwargs)
		self.Signals = self._IAudioContainer.Signals
 
	def equals(self, obj):
		return self._IAudioContainer.Equals(obj)
 
	def get_hash_code(self, *args, **kwargs):
		return self._IAudioContainer.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._IAudioContainer.GetType(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._IAudioContainer.ToString(*args, **kwargs)
 
	def get_item(self, channel):
		return self._IAudioContainer.get_Item(channel)
 
	def get_signals(self, *args, **kwargs):
		return self._IAudioContainer.get_Signals(*args, **kwargs)