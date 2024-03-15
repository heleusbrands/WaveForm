from ..wrapper import NWaves 


 

class DeEmphasisFilter:

	def __init__(self, a=0.97, normalize: bool=False):
		self._DeEmphasisFilter = NWaves.Filters.DeEmphasisFilter(a, normalize)
 
	def overloads(self, *args, **kwargs):
		return self._DeEmphasisFilter.Overloads(self, *args, **kwargs)