from ...wrapper import NWaves 


 

class VariableStepLmsFilter:

	def __init__(self, o: int, mu=None, leakage: int=0.0):
		self._VariableStepLmsFilter = NWaves.Filters.Adaptive.VariableStepLmsFilter(order, mu, leakage)
 
	def process(self, *args, **kwargs):
		return self._VariableStepLmsFilter.Process(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._VariableStepLmsFilter.Overloads(self, *args, **kwargs)