from ..wrapper import NWaves 


 

class ThiranFilter:

	def __init__(self, order, delta):
		self._ThiranFilter = NWaves.Filters.ThiranFilter(order, delta)
 
	def overloads(self, *args, **kwargs):
		return self._ThiranFilter.Overloads(self, *args, **kwargs)