from ..wrapper import NWaves 


 

class WhisperEffect:

	def __init__(self, h: int, fftSize: int=0):
		self._WhisperEffect = NWaves.Effects.WhisperEffect(hopSize, fftSize)
 
	def process_spectrum(self, *args, **kwargs):
		return self._WhisperEffect.ProcessSpectrum(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._WhisperEffect.Overloads(self, *args, **kwargs)