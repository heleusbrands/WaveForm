from ...wrapper import NWaves 


 

class Wsola:

	def __init__(self, s: float, w: int, h: int, maxDelta: int=0):
		self._Wsola = NWaves.Operations.Tsm.Wsola(stretch, windowSize, hopAnalysis, maxDelta)
 
	def apply_to(self, *args, **kwargs):
		return self._Wsola.ApplyTo(self, *args, **kwargs)
 
	def waveform_similarity_pos(self, *args, **kwargs):
		return self._Wsola.WaveformSimilarityPos(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._Wsola.Overloads(self, *args, **kwargs)