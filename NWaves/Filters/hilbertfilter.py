from ..wrapper import NWaves 


 

class HilbertFilter:

	def __init__(self, size: int=128):
		self._HilbertFilter = NWaves.Filters.HilbertFilter(size)
		self.Size = self._HilbertFilter.Size
 
	def get_size(self, *args, **kwargs):
		return self._HilbertFilter.get_Size(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._HilbertFilter.Overloads(self, *args, **kwargs)