from ..wrapper import NWaves 


 

class DistortionMode:

	def __init__(self, *args, **kwargs):
		self._DistortionMode = NWaves.Effects.DistortionMode(*args, **kwargs)
		self.HalfWaveRectify = self._DistortionMode.HalfWaveRectify
		self.FullWaveRectify = self._DistortionMode.FullWaveRectify
		self.Exponential = self._DistortionMode.Exponential
		self.HardClipping = self._DistortionMode.HardClipping
		self.SoftClipping = self._DistortionMode.SoftClipping
		self.value__ = self._DistortionMode.value__