from ...wrapper import NWaves 


 

class BandStopFilter:

	def __init__(self, f: float, f: float, o: int, ripple=0.1):
		self._BandStopFilter = NWaves.Filters.ChebyshevI.BandStopFilter(frequencyLow, frequencyHigh, order, ripple)
		self.Order = self._BandStopFilter.Order
		self.Ripple = self._BandStopFilter.Ripple
		self.FrequencyHigh = self._BandStopFilter.FrequencyHigh
		self.FrequencyLow = self._BandStopFilter.FrequencyLow
 
	def get_frequency_low(self, *args, **kwargs):
		return self._BandStopFilter.get_FrequencyLow(self, *args, **kwargs)
 
	def get_frequency_high(self, *args, **kwargs):
		return self._BandStopFilter.get_FrequencyHigh(self, *args, **kwargs)
 
	def get_ripple(self, *args, **kwargs):
		return self._BandStopFilter.get_Ripple(self, *args, **kwargs)
 
	def get_order(self, *args, **kwargs):
		return self._BandStopFilter.get_Order(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._BandStopFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._BandStopFilter.Overloads(self, *args, **kwargs)