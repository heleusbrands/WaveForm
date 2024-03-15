from ...wrapper import NWaves 


 

class HighShelfFilter:

	def __init__(self, f: float, q=1.0, gain=1.0):
		self._HighShelfFilter = NWaves.Filters.BiQuad.HighShelfFilter(frequency, q, gain)
		self.Gain = self._HighShelfFilter.Gain
		self.Q = self._HighShelfFilter.Q
		self.Frequency = self._HighShelfFilter.Frequency
 
	def get_frequency(self, *args, **kwargs):
		return self._HighShelfFilter.get_Frequency(self, *args, **kwargs)
 
	def set_frequency(self, *args, **kwargs):
		return self._HighShelfFilter.set_Frequency(self, *args, **kwargs)
 
	def get_q(self, *args, **kwargs):
		return self._HighShelfFilter.get_Q(self, *args, **kwargs)
 
	def set_q(self, *args, **kwargs):
		return self._HighShelfFilter.set_Q(self, *args, **kwargs)
 
	def get_gain(self, *args, **kwargs):
		return self._HighShelfFilter.get_Gain(self, *args, **kwargs)
 
	def set_gain(self, *args, **kwargs):
		return self._HighShelfFilter.set_Gain(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._HighShelfFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._HighShelfFilter.Overloads(self, *args, **kwargs)