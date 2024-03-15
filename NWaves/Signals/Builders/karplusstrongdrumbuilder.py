from ...wrapper import NWaves 


 

class KarplusStrongDrumBuilder:

	def __init__(self, samples):
		self._KarplusStrongDrumBuilder = NWaves.Signals.Builders.KarplusStrongDrumBuilder(samples)
 
	def next_sample(self, *args, **kwargs):
		return self._KarplusStrongDrumBuilder.NextSample(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._KarplusStrongDrumBuilder.Overloads(self, *args, **kwargs)