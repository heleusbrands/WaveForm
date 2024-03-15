from ..wrapper import NWaves 


 

class WaveFormat:

	def __init__(self, *args, **kwargs):
		self._WaveFormat = NWaves.Audio.WaveFormat(*args, **kwargs)
		self.BitsPerSample = self._WaveFormat.BitsPerSample
		self.Align = self._WaveFormat.Align
		self.ByteRate = self._WaveFormat.ByteRate
		self.SamplingRate = self._WaveFormat.SamplingRate
		self.ChannelCount = self._WaveFormat.ChannelCount
		self.AudioFormat = self._WaveFormat.AudioFormat