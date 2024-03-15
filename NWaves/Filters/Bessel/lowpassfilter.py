from ...wrapper import NWaves 


 

class LowPassFilter:

	def __init__(self, frequency, order):
		self._LowPassFilter = NWaves.Filters.Bessel.LowPassFilter(frequency, order)
		self.Order = self._LowPassFilter.Order
		self.Frequency = self._LowPassFilter.Frequency
 
	def get_frequency(self, *args, **kwargs):
		return self._LowPassFilter.get_Frequency(self, *args, **kwargs)
 
	def get_order(self, *args, **kwargs):
		return self._LowPassFilter.get_Order(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._LowPassFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._LowPassFilter.Overloads(self, *args, **kwargs)