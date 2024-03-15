from ...wrapper import NWaves 


 

class BandPassFilter:

	def __init__(self, f: float, f: float, o: int, ripple=0.1):
		self._BandPassFilter = NWaves.Filters.ChebyshevII.BandPassFilter(frequencyLow, frequencyHigh, order, ripple)
		self.Order = self._BandPassFilter.Order
		self.Ripple = self._BandPassFilter.Ripple
		self.FrequencyHigh = self._BandPassFilter.FrequencyHigh
		self.FrequencyLow = self._BandPassFilter.FrequencyLow
 
	def get_frequency_low(self, *args, **kwargs):
		return self._BandPassFilter.get_FrequencyLow(self, *args, **kwargs)
 
	def get_frequency_high(self, *args, **kwargs):
		return self._BandPassFilter.get_FrequencyHigh(self, *args, **kwargs)
 
	def get_ripple(self, *args, **kwargs):
		return self._BandPassFilter.get_Ripple(self, *args, **kwargs)
 
	def get_order(self, *args, **kwargs):
		return self._BandPassFilter.get_Order(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._BandPassFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._BandPassFilter.Overloads(self, *args, **kwargs)