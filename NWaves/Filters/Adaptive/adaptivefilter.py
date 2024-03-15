from ...wrapper import NWaves 


 

class AdaptiveFilter:

	def __init__(self, order):
		self._AdaptiveFilter = NWaves.Filters.Adaptive.AdaptiveFilter(order)
 
	def init(self, *args, **kwargs):
		return self._AdaptiveFilter.Init(self, *args, **kwargs)
 
	def process(self, *args, **kwargs):
		return self._AdaptiveFilter.Process(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._AdaptiveFilter.Overloads(self, *args, **kwargs)