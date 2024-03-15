from ...wrapper import NWaves 


 

class HighPassFilter:

	def __init__(self, frequency, order):
		self._HighPassFilter = NWaves.Filters.Butterworth.HighPassFilter(frequency, order)
		self.Order = self._HighPassFilter.Order
		self.Frequency = self._HighPassFilter.Frequency
 
	def get_frequency(self, *args, **kwargs):
		return self._HighPassFilter.get_Frequency(self, *args, **kwargs)
 
	def get_order(self, *args, **kwargs):
		return self._HighPassFilter.get_Order(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._HighPassFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._HighPassFilter.Overloads(self, *args, **kwargs)