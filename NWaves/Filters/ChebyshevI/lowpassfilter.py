from ...wrapper import NWaves 


 

class LowPassFilter:

	def __init__(self, f: float, o: int, ripple=0.1):
		self._LowPassFilter = NWaves.Filters.ChebyshevI.LowPassFilter(frequency, order, ripple)
		self.Order = self._LowPassFilter.Order
		self.Ripple = self._LowPassFilter.Ripple
		self.Frequency = self._LowPassFilter.Frequency
 
	def get_frequency(self, *args, **kwargs):
		return self._LowPassFilter.get_Frequency(self, *args, **kwargs)
 
	def get_ripple(self, *args, **kwargs):
		return self._LowPassFilter.get_Ripple(self, *args, **kwargs)
 
	def get_order(self, *args, **kwargs):
		return self._LowPassFilter.get_Order(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._LowPassFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._LowPassFilter.Overloads(self, *args, **kwargs)