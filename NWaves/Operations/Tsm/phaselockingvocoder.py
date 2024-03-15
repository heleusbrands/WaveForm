from ...wrapper import NWaves 


 

class PhaseLockingVocoder:

	def __init__(self, s: float, h: int, fftSize: int=0):
		self._PhaseLockingVocoder = NWaves.Operations.Tsm.PhaseLockingVocoder(stretch, hopAnalysis, fftSize)
 
	def process_spectrum(self, *args, **kwargs):
		return self._PhaseLockingVocoder.ProcessSpectrum(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PhaseLockingVocoder.Overloads(self, *args, **kwargs)