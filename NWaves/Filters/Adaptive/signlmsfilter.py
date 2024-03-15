from ...wrapper import NWaves 


 

class SignLmsFilter:

	def __init__(self, o: int, mu: int=0.75, leakage: int=0.0):
		self._SignLmsFilter = NWaves.Filters.Adaptive.SignLmsFilter(order, mu, leakage)
 
	def process(self, *args, **kwargs):
		return self._SignLmsFilter.Process(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._SignLmsFilter.Overloads(self, *args, **kwargs)