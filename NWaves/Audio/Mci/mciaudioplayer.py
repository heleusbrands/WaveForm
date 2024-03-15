from ...wrapper import NWaves 


 

class MciAudioPlayer:

	def __init__(self, *args, **kwargs):
		self._MciAudioPlayer = NWaves.Audio.Mci.MciAudioPlayer(*args, **kwargs)
		self.Volume = self._MciAudioPlayer.Volume
 
	def equals(self, *args, **kwargs):
		return self._MciAudioPlayer.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._MciAudioPlayer.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._MciAudioPlayer.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._MciAudioPlayer.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._MciAudioPlayer.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._MciAudioPlayer.Overloads(*args, **kwargs)
 
	def pause(self, *args, **kwargs):
		return self._MciAudioPlayer.Pause(*args, **kwargs)
 
	def play_async(self, *args, **kwargs):
		return self._MciAudioPlayer.PlayAsync(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._MciAudioPlayer.ReferenceEquals(objA, objB)
 
	def resume(self, *args, **kwargs):
		return self._MciAudioPlayer.Resume(*args, **kwargs)
 
	def stop(self, *args, **kwargs):
		return self._MciAudioPlayer.Stop(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._MciAudioPlayer.ToString(*args, **kwargs)
 
	def get_volume(self, *args, **kwargs):
		return self._MciAudioPlayer.get_Volume(*args, **kwargs)
 
	def set_volume(self, value):
		return self._MciAudioPlayer.set_Volume(value)