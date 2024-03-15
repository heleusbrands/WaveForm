from ...wrapper import NWaves 


 

class BandPassFilter:

	def __init__(self, f: float, q=1.0):
		self._BandPassFilter = NWaves.Filters.BiQuad.BandPassFilter(frequency, q)
		self.Q = self._BandPassFilter.Q
		self.Frequency = self._BandPassFilter.Frequency
 
	def get_frequency(self, *args, **kwargs):
		return self._BandPassFilter.get_Frequency(self, *args, **kwargs)
 
	def set_frequency(self, *args, **kwargs):
		return self._BandPassFilter.set_Frequency(self, *args, **kwargs)
 
	def get_q(self, *args, **kwargs):
		return self._BandPassFilter.get_Q(self, *args, **kwargs)
 
	def set_q(self, *args, **kwargs):
		return self._BandPassFilter.set_Q(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._BandPassFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._BandPassFilter.Overloads(self, *args, **kwargs)