from ...wrapper import NWaves 


 

class NotchFilter:

	def __init__(self, f: float, q=1.0):
		self._NotchFilter = NWaves.Filters.BiQuad.NotchFilter(frequency, q)
		self.Q = self._NotchFilter.Q
		self.Frequency = self._NotchFilter.Frequency
 
	def get_frequency(self, *args, **kwargs):
		return self._NotchFilter.get_Frequency(self, *args, **kwargs)
 
	def set_frequency(self, *args, **kwargs):
		return self._NotchFilter.set_Frequency(self, *args, **kwargs)
 
	def get_q(self, *args, **kwargs):
		return self._NotchFilter.get_Q(self, *args, **kwargs)
 
	def set_q(self, *args, **kwargs):
		return self._NotchFilter.set_Q(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._NotchFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._NotchFilter.Overloads(self, *args, **kwargs)