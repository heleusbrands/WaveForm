from ...wrapper import NWaves 


 

class BandPassFilter:

	def __init__(self, f: float, f: float, o: int, ripplePass=1.0, rippleStop=20.0):
		self._BandPassFilter = NWaves.Filters.Elliptic.BandPassFilter(frequencyLow, frequencyHigh, order, ripplePass, rippleStop)
		self.Order = self._BandPassFilter.Order
		self.RippleStopband = self._BandPassFilter.RippleStopband
		self.RipplePassband = self._BandPassFilter.RipplePassband
		self.FrequencyHigh = self._BandPassFilter.FrequencyHigh
		self.FrequencyLow = self._BandPassFilter.FrequencyLow
 
	def get_frequency_low(self, *args, **kwargs):
		return self._BandPassFilter.get_FrequencyLow(self, *args, **kwargs)
 
	def get_frequency_high(self, *args, **kwargs):
		return self._BandPassFilter.get_FrequencyHigh(self, *args, **kwargs)
 
	def get_ripple_passband(self, *args, **kwargs):
		return self._BandPassFilter.get_RipplePassband(self, *args, **kwargs)
 
	def get_ripple_stopband(self, *args, **kwargs):
		return self._BandPassFilter.get_RippleStopband(self, *args, **kwargs)
 
	def get_order(self, *args, **kwargs):
		return self._BandPassFilter.get_Order(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._BandPassFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._BandPassFilter.Overloads(self, *args, **kwargs)