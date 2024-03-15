from ...wrapper import NWaves 


 

class WaveletFamily:

	def __init__(self, *args, **kwargs):
		self._WaveletFamily = NWaves.Transforms.Wavelets.WaveletFamily(*args, **kwargs)
		self.Symlet = self._WaveletFamily.Symlet
		self.Coiflet = self._WaveletFamily.Coiflet
		self.Daubechies = self._WaveletFamily.Daubechies
		self.Haar = self._WaveletFamily.Haar
		self.value__ = self._WaveletFamily.value__