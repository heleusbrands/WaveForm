from ..wrapper import NWaves 


 

class RastaFilter:

	def __init__(self, pole=0.98):
		self._RastaFilter = NWaves.Filters.RastaFilter(pole)
 
	def overloads(self, *args, **kwargs):
		return self._RastaFilter.Overloads(self, *args, **kwargs)