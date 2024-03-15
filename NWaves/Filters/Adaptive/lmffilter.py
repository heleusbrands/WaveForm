from ...wrapper import NWaves 


 

class LmfFilter:

	def __init__(self, o: int, mu: int=0.75, leakage: int=0.0):
		self._LmfFilter = NWaves.Filters.Adaptive.LmfFilter(order, mu, leakage)
 
	def process(self, *args, **kwargs):
		return self._LmfFilter.Process(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._LmfFilter.Overloads(self, *args, **kwargs)