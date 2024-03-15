from ...wrapper import NWaves 


 

class MciAudioRecorder:

	def __init__(self, *args, **kwargs):
		self._MciAudioRecorder = NWaves.Audio.Mci.MciAudioRecorder(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._MciAudioRecorder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._MciAudioRecorder.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._MciAudioRecorder.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._MciAudioRecorder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._MciAudioRecorder.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._MciAudioRecorder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._MciAudioRecorder.ReferenceEquals(objA, objB)
 
	def start_recording(self, samplingRate: int=44100, channelCount: int=1, bitsPerSample: int=16):
		return self._MciAudioRecorder.StartRecording(samplingRate, channelCount, bitsPerSample)
 
	def stop_recording(self, destination):
		return self._MciAudioRecorder.StopRecording(destination)
 
	def to_string(self, *args, **kwargs):
		return self._MciAudioRecorder.ToString(*args, **kwargs)