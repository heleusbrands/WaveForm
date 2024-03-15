from ..wrapper import NWaves 


 

class CombFeedbackFilter:

	def __init__(self, m: int, b0=1.0, am: int=0.6):
		self._CombFeedbackFilter = NWaves.Filters.CombFeedbackFilter(m, b0, am)
 
	def process(self, *args, **kwargs):
		return self._CombFeedbackFilter.Process(self, *args, **kwargs)
 
	def apply_to(self, *args, **kwargs):
		return self._CombFeedbackFilter.ApplyTo(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._CombFeedbackFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._CombFeedbackFilter.Overloads(self, *args, **kwargs)