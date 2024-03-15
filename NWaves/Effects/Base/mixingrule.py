from ...wrapper import NWaves 


 

class MixingRule:

	def __init__(self, *args, **kwargs):
		self._MixingRule = NWaves.Effects.Base.MixingRule(*args, **kwargs)
		self.SqRoot4_5Db = self._MixingRule.SqRoot4_5Db
		self.SqRoot3Db = self._MixingRule.SqRoot3Db
		self.Sin6Db = self._MixingRule.Sin6Db
		self.Sin4_5Db = self._MixingRule.Sin4_5Db
		self.Sin3Db = self._MixingRule.Sin3Db
		self.Balanced = self._MixingRule.Balanced
		self.Linear = self._MixingRule.Linear
		self.value__ = self._MixingRule.value__