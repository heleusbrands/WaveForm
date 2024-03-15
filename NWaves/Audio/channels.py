from ..wrapper import NWaves 


 

class Channels:

	def __init__(self, *args, **kwargs):
		self._Channels = NWaves.Audio.Channels(*args, **kwargs)
		self.Interleave = self._Channels.Interleave
		self.Average = self._Channels.Average
		self.Sum = self._Channels.Sum
		self.Right = self._Channels.Right
		self.Left = self._Channels.Left
		self.value__ = self._Channels.value__