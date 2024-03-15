from ...wrapper import NWaves 


 

class SpectrumType:

	def __init__(self, *args, **kwargs):
		self._SpectrumType = NWaves.FeatureExtractors.Options.SpectrumType(*args, **kwargs)
		self.PowerNormalized = self._SpectrumType.PowerNormalized
		self.MagnitudeNormalized = self._SpectrumType.MagnitudeNormalized
		self.Power = self._SpectrumType.Power
		self.Magnitude = self._SpectrumType.Magnitude
		self.value__ = self._SpectrumType.value__