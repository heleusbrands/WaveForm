from ...wrapper import NWaves 


 

class LowShelfFilter:

	def __init__(self, f: float, q=1.0, gain=1.0):
		self._LowShelfFilter = NWaves.Filters.BiQuad.LowShelfFilter(frequency, q, gain)
		self.Gain = self._LowShelfFilter.Gain
		self.Q = self._LowShelfFilter.Q
		self.Frequency = self._LowShelfFilter.Frequency
 
	def get_frequency(self, *args, **kwargs):
		return self._LowShelfFilter.get_Frequency(self, *args, **kwargs)
 
	def set_frequency(self, *args, **kwargs):
		return self._LowShelfFilter.set_Frequency(self, *args, **kwargs)
 
	def get_q(self, *args, **kwargs):
		return self._LowShelfFilter.get_Q(self, *args, **kwargs)
 
	def set_q(self, *args, **kwargs):
		return self._LowShelfFilter.set_Q(self, *args, **kwargs)
 
	def get_gain(self, *args, **kwargs):
		return self._LowShelfFilter.get_Gain(self, *args, **kwargs)
 
	def set_gain(self, *args, **kwargs):
		return self._LowShelfFilter.set_Gain(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._LowShelfFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._LowShelfFilter.Overloads(self, *args, **kwargs)