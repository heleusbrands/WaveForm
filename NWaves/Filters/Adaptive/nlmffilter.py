from ...wrapper import NWaves 


 

class NlmfFilter:

	def __init__(self, o: int, mu: int=0.75, eps: int=1.0, leakage: int=0.0):
		self._NlmfFilter = NWaves.Filters.Adaptive.NlmfFilter(order, mu, eps, leakage)
 
	def process(self, *args, **kwargs):
		return self._NlmfFilter.Process(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._NlmfFilter.Overloads(self, *args, **kwargs)