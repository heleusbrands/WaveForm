from ..wrapper import NWaves 


 

class WaveFile:

	def __init__(self, *args, **kwargs):
		self._WaveFile = NWaves.Audio.WaveFile(*args, **kwargs)
		self.SupportedBitDepths = self._WaveFile.SupportedBitDepths
		self.WaveFmt = self._WaveFile.WaveFmt
		self.Signals = self._WaveFile.Signals
 
	def get_signals(self, *args, **kwargs):
		return self._WaveFile.get_Signals(self, *args, **kwargs)
 
	def set_signals(self, *args, **kwargs):
		return self._WaveFile.set_Signals(self, *args, **kwargs)
 
	def get_wave_fmt(self, *args, **kwargs):
		return self._WaveFile.get_WaveFmt(self, *args, **kwargs)
 
	def set_wave_fmt(self, *args, **kwargs):
		return self._WaveFile.set_WaveFmt(self, *args, **kwargs)
 
	def read_wave_stream(self, *args, **kwargs):
		return self._WaveFile.ReadWaveStream(self, *args, **kwargs)
 
	def get_bytes(self, *args, **kwargs):
		return self._WaveFile.GetBytes(self, *args, **kwargs)
 
	def save_to(self, *args, **kwargs):
		return self._WaveFile.SaveTo(self, *args, **kwargs)
 
	def get_item(self, *args, **kwargs):
		return self._WaveFile.get_Item(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._WaveFile.Overloads(self, *args, **kwargs)