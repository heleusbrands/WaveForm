from ...wrapper import NWaves 


 

class PhaseVocoder:

	def __init__(self, s: float, h: int, fftSize: int=0):
		self._PhaseVocoder = NWaves.Operations.Tsm.PhaseVocoder(stretch, hopAnalysis, fftSize)
 
	def apply_to(self, *args, **kwargs):
		return self._PhaseVocoder.ApplyTo(self, *args, **kwargs)
 
	def process_spectrum(self, *args, **kwargs):
		return self._PhaseVocoder.ProcessSpectrum(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._PhaseVocoder.Reset(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PhaseVocoder.Overloads(self, *args, **kwargs)