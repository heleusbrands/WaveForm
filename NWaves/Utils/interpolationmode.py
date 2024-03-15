from ..wrapper import NWaves 


 

class InterpolationMode:

	def __init__(self, *args, **kwargs):
		self._InterpolationMode = NWaves.Utils.InterpolationMode(*args, **kwargs)
		self.Nearest = self._InterpolationMode.Nearest
		self.Thiran = self._InterpolationMode.Thiran
		self.Cubic = self._InterpolationMode.Cubic
		self.Linear = self._InterpolationMode.Linear
		self.value__ = self._InterpolationMode.value__