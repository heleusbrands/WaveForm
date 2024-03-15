from ...wrapper import NWaves 


 

class BandPassFilter:

	def __init__(self, frequencyLow, frequencyHigh, order):
		self._BandPassFilter = NWaves.Filters.Bessel.BandPassFilter(frequencyLow, frequencyHigh, order)
		self.Order = self._BandPassFilter.Order
		self.FrequencyHigh = self._BandPassFilter.FrequencyHigh
		self.FrequencyLow = self._BandPassFilter.FrequencyLow
 
	def get_frequency_low(self, *args, **kwargs):
		return self._BandPassFilter.get_FrequencyLow(self, *args, **kwargs)
 
	def get_frequency_high(self, *args, **kwargs):
		return self._BandPassFilter.get_FrequencyHigh(self, *args, **kwargs)
 
	def get_order(self, *args, **kwargs):
		return self._BandPassFilter.get_Order(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._BandPassFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._BandPassFilter.Overloads(self, *args, **kwargs)