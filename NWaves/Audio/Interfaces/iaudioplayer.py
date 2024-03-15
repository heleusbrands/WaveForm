from ...wrapper import NWaves 


 

class IAudioPlayer:

	def __init__(self, /, *args, **kwargs):
		self._IAudioPlayer = NWaves.Audio.Interfaces.IAudioPlayer(self, args, kwargs)
		self.Volume = self._IAudioPlayer.Volume
 
	def equals(self, obj):
		return self._IAudioPlayer.Equals(obj)
 
	def get_hash_code(self, *args, **kwargs):
		return self._IAudioPlayer.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._IAudioPlayer.GetType(*args, **kwargs)
 
	def pause(self, *args, **kwargs):
		return self._IAudioPlayer.Pause(*args, **kwargs)
 
	def play_async(self, *args, **kwargs):
		return self._IAudioPlayer.PlayAsync(*args, **kwargs)
 
	def resume(self, *args, **kwargs):
		return self._IAudioPlayer.Resume(*args, **kwargs)
 
	def stop(self, *args, **kwargs):
		return self._IAudioPlayer.Stop(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._IAudioPlayer.ToString(*args, **kwargs)
 
	def get_volume(self, *args, **kwargs):
		return self._IAudioPlayer.get_Volume(*args, **kwargs)
 
	def set_volume(self, value):
		return self._IAudioPlayer.set_Volume(value)