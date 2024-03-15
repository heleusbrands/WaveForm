from ..wrapper import NWaves 


 

class SavitzkyGolayFilter:

	def __init__(self, s: int, deriv: int=0):
		self._SavitzkyGolayFilter = NWaves.Filters.SavitzkyGolayFilter(size, deriv)
		self.Size = self._SavitzkyGolayFilter.Size
 
	def get_size(self, *args, **kwargs):
		return self._SavitzkyGolayFilter.get_Size(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._SavitzkyGolayFilter.Overloads(self, *args, **kwargs)