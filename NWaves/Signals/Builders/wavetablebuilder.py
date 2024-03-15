from ...wrapper import NWaves 


 

class WaveTableBuilder:

	def __init__(self, samples):
		self._WaveTableBuilder = NWaves.Signals.Builders.WaveTableBuilder(samples)
 
	def next_sample(self, *args, **kwargs):
		return self._WaveTableBuilder.NextSample(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._WaveTableBuilder.Reset(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._WaveTableBuilder.Overloads(self, *args, **kwargs)