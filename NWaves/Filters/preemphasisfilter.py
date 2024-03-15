from ..wrapper import NWaves 


 

class PreEmphasisFilter:

	def __init__(self, a=0.97, normalize: bool=False):
		self._PreEmphasisFilter = NWaves.Filters.PreEmphasisFilter(a, normalize)
 
	def process(self, *args, **kwargs):
		return self._PreEmphasisFilter.Process(self, *args, **kwargs)
 
	def apply_to(self, *args, **kwargs):
		return self._PreEmphasisFilter.ApplyTo(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._PreEmphasisFilter.Reset(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PreEmphasisFilter.Overloads(self, *args, **kwargs)