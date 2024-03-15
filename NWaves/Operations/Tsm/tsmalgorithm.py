from ...wrapper import NWaves 


 

class TsmAlgorithm:

	def __init__(self, *args, **kwargs):
		self._TsmAlgorithm = NWaves.Operations.Tsm.TsmAlgorithm(*args, **kwargs)
		self.PaulStretch = self._TsmAlgorithm.PaulStretch
		self.Wsola = self._TsmAlgorithm.Wsola
		self.PhaseVocoderPhaseLocking = self._TsmAlgorithm.PhaseVocoderPhaseLocking
		self.PhaseVocoder = self._TsmAlgorithm.PhaseVocoder
		self.value__ = self._TsmAlgorithm.value__