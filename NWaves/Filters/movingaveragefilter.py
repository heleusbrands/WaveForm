from ..wrapper import NWaves 


 

class MovingAverageFilter:

	def __init__(self, size: int=9):
		self._MovingAverageFilter = NWaves.Filters.MovingAverageFilter(size)
		self.Size = self._MovingAverageFilter.Size
 
	def get_size(self, *args, **kwargs):
		return self._MovingAverageFilter.get_Size(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._MovingAverageFilter.Overloads(self, *args, **kwargs)