from ...wrapper import NWaves 


 

class OnePoleFilter:

	def __init__(self, b, a):
		self._OnePoleFilter = NWaves.Filters.OnePole.OnePoleFilter(b, a)
 
	def process(self, *args, **kwargs):
		return self._OnePoleFilter.Process(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._OnePoleFilter.Reset(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._OnePoleFilter.Overloads(self, *args, **kwargs)