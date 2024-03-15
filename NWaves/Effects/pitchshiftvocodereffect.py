from ..wrapper import NWaves 


 

class PitchShiftVocoderEffect:

	def __init__(self, s: int, s: float, fftSize: int=1024, hopSize: int=64):
		self._PitchShiftVocoderEffect = NWaves.Effects.PitchShiftVocoderEffect(samplingRate, shift, fftSize, hopSize)
		self.Shift = self._PitchShiftVocoderEffect.Shift
 
	def get_shift(self, *args, **kwargs):
		return self._PitchShiftVocoderEffect.get_Shift(self, *args, **kwargs)
 
	def set_shift(self, *args, **kwargs):
		return self._PitchShiftVocoderEffect.set_Shift(self, *args, **kwargs)
 
	def process_spectrum(self, *args, **kwargs):
		return self._PitchShiftVocoderEffect.ProcessSpectrum(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._PitchShiftVocoderEffect.Reset(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PitchShiftVocoderEffect.Overloads(self, *args, **kwargs)