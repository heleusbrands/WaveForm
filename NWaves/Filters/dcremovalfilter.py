from ..wrapper import NWaves 


 

class DcRemovalFilter:

	def __init__(self, r=0.995):
		self._DcRemovalFilter = NWaves.Filters.DcRemovalFilter(r)
 
	def process(self, *args, **kwargs):
		return self._DcRemovalFilter.Process(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._DcRemovalFilter.Reset(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._DcRemovalFilter.Overloads(self, *args, **kwargs)