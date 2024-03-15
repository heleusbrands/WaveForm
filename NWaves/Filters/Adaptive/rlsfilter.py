from ...wrapper import NWaves 


 

class RlsFilter:

	def __init__(self, o: int, lambda: int=0.9900000095367432, initCorrMatrix: int=100.0):
		self._RlsFilter = NWaves.Filters.Adaptive.RlsFilter(order, lambda, initCorrMatrix)
 
	def process(self, *args, **kwargs):
		return self._RlsFilter.Process(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._RlsFilter.Overloads(self, *args, **kwargs)