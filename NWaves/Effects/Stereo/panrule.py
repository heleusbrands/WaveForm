from ...wrapper import NWaves 


 

class PanRule:

	def __init__(self, *args, **kwargs):
		self._PanRule = NWaves.Effects.Stereo.PanRule(*args, **kwargs)
		self.SqRoot4_5Db = self._PanRule.SqRoot4_5Db
		self.SqRoot3Db = self._PanRule.SqRoot3Db
		self.Sin6Db = self._PanRule.Sin6Db
		self.Sin4_5Db = self._PanRule.Sin4_5Db
		self.Sin3Db = self._PanRule.Sin3Db
		self.ConstantPower = self._PanRule.ConstantPower
		self.Balanced = self._PanRule.Balanced
		self.Linear = self._PanRule.Linear
		self.value__ = self._PanRule.value__