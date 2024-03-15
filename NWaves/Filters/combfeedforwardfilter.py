from ..wrapper import NWaves 


 

class CombFeedforwardFilter:

	def __init__(self, m: int, b0=1.0, bm: int=0.5, norm: intalize=True):
		self._CombFeedforwardFilter = NWaves.Filters.CombFeedforwardFilter(m, b0, bm, normalize)
 
	def process(self, *args, **kwargs):
		return self._CombFeedforwardFilter.Process(self, *args, **kwargs)
 
	def apply_to(self, *args, **kwargs):
		return self._CombFeedforwardFilter.ApplyTo(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._CombFeedforwardFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._CombFeedforwardFilter.Overloads(self, *args, **kwargs)