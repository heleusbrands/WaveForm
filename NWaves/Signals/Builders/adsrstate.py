from ....wrapper import NWaves 


 

class AdsrState:

	def __init__(self, *args, **kwargs):
		self._AdsrState = NWaves.Signals.Builders.AdsrBuilder.AdsrState(*args, **kwargs)
		self.Release = self._AdsrState.Release
		self.Sustain = self._AdsrState.Sustain
		self.Decay = self._AdsrState.Decay
		self.Attack = self._AdsrState.Attack
		self.value__ = self._AdsrState.value__