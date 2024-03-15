from ...wrapper import NWaves 


 

class LowPassFilter:

	def __init__(self, f: float, q=1.0):
		self._LowPassFilter = NWaves.Filters.BiQuad.LowPassFilter(frequency, q)
		self.Q = self._LowPassFilter.Q
		self.Frequency = self._LowPassFilter.Frequency
 
	def get_frequency(self, *args, **kwargs):
		return self._LowPassFilter.get_Frequency(self, *args, **kwargs)
 
	def set_frequency(self, *args, **kwargs):
		return self._LowPassFilter.set_Frequency(self, *args, **kwargs)
 
	def get_q(self, *args, **kwargs):
		return self._LowPassFilter.get_Q(self, *args, **kwargs)
 
	def set_q(self, *args, **kwargs):
		return self._LowPassFilter.set_Q(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._LowPassFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._LowPassFilter.Overloads(self, *args, **kwargs)