from ...wrapper import NWaves 


 

class HighPassFilter:

	def __init__(self, f: float, q=1.0):
		self._HighPassFilter = NWaves.Filters.BiQuad.HighPassFilter(frequency, q)
		self.Q = self._HighPassFilter.Q
		self.Frequency = self._HighPassFilter.Frequency
 
	def get_frequency(self, *args, **kwargs):
		return self._HighPassFilter.get_Frequency(self, *args, **kwargs)
 
	def set_frequency(self, *args, **kwargs):
		return self._HighPassFilter.set_Frequency(self, *args, **kwargs)
 
	def get_q(self, *args, **kwargs):
		return self._HighPassFilter.get_Q(self, *args, **kwargs)
 
	def set_q(self, *args, **kwargs):
		return self._HighPassFilter.set_Q(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._HighPassFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._HighPassFilter.Overloads(self, *args, **kwargs)