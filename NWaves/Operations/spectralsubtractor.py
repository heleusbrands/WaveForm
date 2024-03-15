from ..wrapper import NWaves 


 

class SpectralSubtractor:

	def __init__(self, noise, fftSize: int=1024, hopSize: int=128):
		self._SpectralSubtractor = NWaves.Operations.SpectralSubtractor(noise, fftSize, hopSize)
		self.SnrMax = self._SpectralSubtractor.SnrMax
		self.SnrMin = self._SpectralSubtractor.SnrMin
		self.AlphaMax = self._SpectralSubtractor.AlphaMax
		self.AlphaMin = self._SpectralSubtractor.AlphaMin
		self.Beta = self._SpectralSubtractor.Beta
 
	def get_beta(self, *args, **kwargs):
		return self._SpectralSubtractor.get_Beta(self, *args, **kwargs)
 
	def set_beta(self, *args, **kwargs):
		return self._SpectralSubtractor.set_Beta(self, *args, **kwargs)
 
	def get_alpha_min(self, *args, **kwargs):
		return self._SpectralSubtractor.get_AlphaMin(self, *args, **kwargs)
 
	def set_alpha_min(self, *args, **kwargs):
		return self._SpectralSubtractor.set_AlphaMin(self, *args, **kwargs)
 
	def get_alpha_max(self, *args, **kwargs):
		return self._SpectralSubtractor.get_AlphaMax(self, *args, **kwargs)
 
	def set_alpha_max(self, *args, **kwargs):
		return self._SpectralSubtractor.set_AlphaMax(self, *args, **kwargs)
 
	def get_snr_min(self, *args, **kwargs):
		return self._SpectralSubtractor.get_SnrMin(self, *args, **kwargs)
 
	def set_snr_min(self, *args, **kwargs):
		return self._SpectralSubtractor.set_SnrMin(self, *args, **kwargs)
 
	def get_snr_max(self, *args, **kwargs):
		return self._SpectralSubtractor.get_SnrMax(self, *args, **kwargs)
 
	def set_snr_max(self, *args, **kwargs):
		return self._SpectralSubtractor.set_SnrMax(self, *args, **kwargs)
 
	def process_spectrum(self, *args, **kwargs):
		return self._SpectralSubtractor.ProcessSpectrum(self, *args, **kwargs)
 
	def estimate_noise(self, *args, **kwargs):
		return self._SpectralSubtractor.EstimateNoise(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._SpectralSubtractor.Overloads(self, *args, **kwargs)