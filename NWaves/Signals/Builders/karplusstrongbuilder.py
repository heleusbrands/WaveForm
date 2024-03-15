from ...wrapper import NWaves 


 

class KarplusStrongBuilder:

	def __init__(self, samples):
		self._KarplusStrongBuilder = NWaves.Signals.Builders.KarplusStrongBuilder(samples)
 
	def generate_wave_table(self, *args, **kwargs):
		return self._KarplusStrongBuilder.GenerateWaveTable(self, *args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._KarplusStrongBuilder.NextSample(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._KarplusStrongBuilder.Reset(self, *args, **kwargs)
 
	def sampled_at(self, *args, **kwargs):
		return self._KarplusStrongBuilder.SampledAt(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._KarplusStrongBuilder.Overloads(self, *args, **kwargs)