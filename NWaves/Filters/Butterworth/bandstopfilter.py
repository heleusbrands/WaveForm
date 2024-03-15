from ...wrapper import NWaves 


 

class BandStopFilter:

	def __init__(self, frequencyLow, frequencyHigh, order):
		self._BandStopFilter = NWaves.Filters.Butterworth.BandStopFilter(frequencyLow, frequencyHigh, order)
		self.Order = self._BandStopFilter.Order
		self.FrequencyHigh = self._BandStopFilter.FrequencyHigh
		self.FrequencyLow = self._BandStopFilter.FrequencyLow
 
	def get_frequency_low(self, *args, **kwargs):
		return self._BandStopFilter.get_FrequencyLow(self, *args, **kwargs)
 
	def get_frequency_high(self, *args, **kwargs):
		return self._BandStopFilter.get_FrequencyHigh(self, *args, **kwargs)
 
	def get_order(self, *args, **kwargs):
		return self._BandStopFilter.get_Order(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._BandStopFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._BandStopFilter.Overloads(self, *args, **kwargs)