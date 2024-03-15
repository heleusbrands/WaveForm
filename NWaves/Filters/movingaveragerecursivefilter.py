from ..wrapper import NWaves 


 

class MovingAverageRecursiveFilter:

	def __init__(self, size: int=9):
		self._MovingAverageRecursiveFilter = NWaves.Filters.MovingAverageRecursiveFilter(size)
		self.Size = self._MovingAverageRecursiveFilter.Size
 
	def get_size(self, *args, **kwargs):
		return self._MovingAverageRecursiveFilter.get_Size(self, *args, **kwargs)
 
	def apply_to(self, *args, **kwargs):
		return self._MovingAverageRecursiveFilter.ApplyTo(self, *args, **kwargs)
 
	def process(self, *args, **kwargs):
		return self._MovingAverageRecursiveFilter.Process(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._MovingAverageRecursiveFilter.Reset(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._MovingAverageRecursiveFilter.Overloads(self, *args, **kwargs)