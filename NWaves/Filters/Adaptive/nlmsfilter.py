from ...wrapper import NWaves 


 

class NlmsFilter:

	def __init__(self, o: int, mu: int=0.75, eps: int=1.0, leakage: int=0.0):
		self._NlmsFilter = NWaves.Filters.Adaptive.NlmsFilter(order, mu, eps, leakage)
 
	def process(self, *args, **kwargs):
		return self._NlmsFilter.Process(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._NlmsFilter.Overloads(self, *args, **kwargs)