from ...wrapper import NWaves 


 

class LmsFilter:

	def __init__(self, o: int, mu: int=0.75, leakage: int=0.0):
		self._LmsFilter = NWaves.Filters.Adaptive.LmsFilter(order, mu, leakage)
 
	def process(self, *args, **kwargs):
		return self._LmsFilter.Process(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._LmsFilter.Overloads(self, *args, **kwargs)