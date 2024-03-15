from ...wrapper import NWaves 


 

class AllPassFilter:

	def __init__(self, f: float, q=1.0):
		self._AllPassFilter = NWaves.Filters.BiQuad.AllPassFilter(frequency, q)
		self.Q = self._AllPassFilter.Q
		self.Frequency = self._AllPassFilter.Frequency
 
	def get_frequency(self, *args, **kwargs):
		return self._AllPassFilter.get_Frequency(self, *args, **kwargs)
 
	def set_frequency(self, *args, **kwargs):
		return self._AllPassFilter.set_Frequency(self, *args, **kwargs)
 
	def get_q(self, *args, **kwargs):
		return self._AllPassFilter.get_Q(self, *args, **kwargs)
 
	def set_q(self, *args, **kwargs):
		return self._AllPassFilter.set_Q(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._AllPassFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._AllPassFilter.Overloads(self, *args, **kwargs)