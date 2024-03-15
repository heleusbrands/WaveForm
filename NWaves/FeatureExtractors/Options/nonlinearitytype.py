from ...wrapper import NWaves 


 

class NonLinearityType:

	def __init__(self, *args, **kwargs):
		self._NonLinearityType = NWaves.FeatureExtractors.Options.NonLinearityType(*args, **kwargs)
		self.None = self._NonLinearityType.None
		self.CubicRoot = self._NonLinearityType.CubicRoot
		self.ToDecibel = self._NonLinearityType.ToDecibel
		self.Log10 = self._NonLinearityType.Log10
		self.LogE = self._NonLinearityType.LogE
		self.value__ = self._NonLinearityType.value__