from ..wrapper import NWaves 


 

class HpsMasking:

	def __init__(self, *args, **kwargs):
		self._HpsMasking = NWaves.Operations.HpsMasking(*args, **kwargs)
		self.WienerOrder2 = self._HpsMasking.WienerOrder2
		self.WienerOrder1 = self._HpsMasking.WienerOrder1
		self.Binary = self._HpsMasking.Binary
		self.value__ = self._HpsMasking.value__