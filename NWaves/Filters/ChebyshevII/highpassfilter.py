from ...wrapper import NWaves 


 

class HighPassFilter:

	def __init__(self, f: float, o: int, ripple=0.1):
		self._HighPassFilter = NWaves.Filters.ChebyshevII.HighPassFilter(frequency, order, ripple)
		self.Order = self._HighPassFilter.Order
		self.Ripple = self._HighPassFilter.Ripple
		self.Frequency = self._HighPassFilter.Frequency
 
	def get_frequency(self, *args, **kwargs):
		return self._HighPassFilter.get_Frequency(self, *args, **kwargs)
 
	def get_ripple(self, *args, **kwargs):
		return self._HighPassFilter.get_Ripple(self, *args, **kwargs)
 
	def get_order(self, *args, **kwargs):
		return self._HighPassFilter.get_Order(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._HighPassFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._HighPassFilter.Overloads(self, *args, **kwargs)