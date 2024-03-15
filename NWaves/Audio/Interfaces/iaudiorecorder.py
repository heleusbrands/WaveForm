from ...wrapper import NWaves 


 

class IAudioRecorder:

	def __init__(self, /, *args, **kwargs):
		self._IAudioRecorder = NWaves.Audio.Interfaces.IAudioRecorder(self, args, kwargs)
 
	def equals(self, obj):
		return self._IAudioRecorder.Equals(obj)
 
	def get_hash_code(self, *args, **kwargs):
		return self._IAudioRecorder.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._IAudioRecorder.GetType(*args, **kwargs)
 
	def start_recording(self, samplingRate, channelCount, bitsPerSample):
		return self._IAudioRecorder.StartRecording(samplingRate, channelCount, bitsPerSample)
 
	def stop_recording(self, destination):
		return self._IAudioRecorder.StopRecording(destination)
 
	def to_string(self, *args, **kwargs):
		return self._IAudioRecorder.ToString(*args, **kwargs)