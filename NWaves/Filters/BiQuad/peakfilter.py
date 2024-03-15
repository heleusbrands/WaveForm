from ...wrapper import NWaves 


 

class PeakFilter:

	def __init__(self, f: float, q=1.0, gain=1.0):
		self._PeakFilter = NWaves.Filters.BiQuad.PeakFilter(frequency, q, gain)
		self.Gain = self._PeakFilter.Gain
		self.Q = self._PeakFilter.Q
		self.Frequency = self._PeakFilter.Frequency
 
	def get_frequency(self, *args, **kwargs):
		return self._PeakFilter.get_Frequency(self, *args, **kwargs)
 
	def set_frequency(self, *args, **kwargs):
		return self._PeakFilter.set_Frequency(self, *args, **kwargs)
 
	def get_q(self, *args, **kwargs):
		return self._PeakFilter.get_Q(self, *args, **kwargs)
 
	def set_q(self, *args, **kwargs):
		return self._PeakFilter.set_Q(self, *args, **kwargs)
 
	def get_gain(self, *args, **kwargs):
		return self._PeakFilter.get_Gain(self, *args, **kwargs)
 
	def set_gain(self, *args, **kwargs):
		return self._PeakFilter.set_Gain(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._PeakFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PeakFilter.Overloads(self, *args, **kwargs)