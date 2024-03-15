from ...wrapper import NWaves 


 

class PadSynthBuilder:

	def __init__(self, *args, **kwargs):
		self._PadSynthBuilder = NWaves.Signals.Builders.PadSynthBuilder(*args, **kwargs)
 
	def set_frequency(self, *args, **kwargs):
		return self._PadSynthBuilder.SetFrequency(self, *args, **kwargs)
 
	def set_fft_size(self, *args, **kwargs):
		return self._PadSynthBuilder.SetFftSize(self, *args, **kwargs)
 
	def set_bandwidth(self, *args, **kwargs):
		return self._PadSynthBuilder.SetBandwidth(self, *args, **kwargs)
 
	def set_scale(self, *args, **kwargs):
		return self._PadSynthBuilder.SetScale(self, *args, **kwargs)
 
	def set_amplitudes(self, *args, **kwargs):
		return self._PadSynthBuilder.SetAmplitudes(self, *args, **kwargs)
 
	def generate_wavetable(self, *args, **kwargs):
		return self._PadSynthBuilder.GenerateWavetable(self, *args, **kwargs)
 
	def profile(self, *args, **kwargs):
		return self._PadSynthBuilder.Profile(self, *args, **kwargs)
 
	def sampled_at(self, *args, **kwargs):
		return self._PadSynthBuilder.SampledAt(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PadSynthBuilder.Overloads(self, *args, **kwargs)