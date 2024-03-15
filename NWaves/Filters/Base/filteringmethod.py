from ...wrapper import NWaves 


 

class FilteringMethod:

	def __init__(self, *args, **kwargs):
		self._FilteringMethod = NWaves.Filters.Base.FilteringMethod(*args, **kwargs)
		self.Custom = self._FilteringMethod.Custom
		self.OverlapSave = self._FilteringMethod.OverlapSave
		self.OverlapAdd = self._FilteringMethod.OverlapAdd
		self.DifferenceEquation = self._FilteringMethod.DifferenceEquation
		self.Auto = self._FilteringMethod.Auto
		self.value__ = self._FilteringMethod.value__