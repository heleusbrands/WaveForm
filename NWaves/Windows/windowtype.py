from ..wrapper import NWaves 


 

class WindowType:

	def __init__(self, *args, **kwargs):
		self._WindowType = NWaves.Windows.WindowType(*args, **kwargs)
		self.Liftering = self._WindowType.Liftering
		self.Flattop = self._WindowType.Flattop
		self.PowerOfSine = self._WindowType.PowerOfSine
		self.Lanczos = self._WindowType.Lanczos
		self.BartlettHann = self._WindowType.BartlettHann
		self.Kbd = self._WindowType.Kbd
		self.Kaiser = self._WindowType.Kaiser
		self.Gaussian = self._WindowType.Gaussian
		self.Hann = self._WindowType.Hann
		self.Blackman = self._WindowType.Blackman
		self.Hamming = self._WindowType.Hamming
		self.Triangular = self._WindowType.Triangular
		self.Rectangular = self._WindowType.Rectangular
		self.value__ = self._WindowType.value__