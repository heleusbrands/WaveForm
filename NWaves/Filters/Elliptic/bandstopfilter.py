from ...wrapper import NWaves 


 

class BandStopFilter:

	def __init__(self, f: float, f: float, o: int, ripplePass=1.0, rippleStop=20.0):
		self._BandStopFilter = NWaves.Filters.Elliptic.BandStopFilter(frequencyLow, frequencyHigh, order, ripplePass, rippleStop)
		self.Order = self._BandStopFilter.Order
		self.RippleStopband = self._BandStopFilter.RippleStopband
		self.RipplePassband = self._BandStopFilter.RipplePassband
		self.FrequencyHigh = self._BandStopFilter.FrequencyHigh
		self.FrequencyLow = self._BandStopFilter.FrequencyLow
 
	def get_frequency_low(self, *args, **kwargs):
		return self._BandStopFilter.get_FrequencyLow(self, *args, **kwargs)
 
	def get_frequency_high(self, *args, **kwargs):
		return self._BandStopFilter.get_FrequencyHigh(self, *args, **kwargs)
 
	def get_ripple_passband(self, *args, **kwargs):
		return self._BandStopFilter.get_RipplePassband(self, *args, **kwargs)
 
	def get_ripple_stopband(self, *args, **kwargs):
		return self._BandStopFilter.get_RippleStopband(self, *args, **kwargs)
 
	def get_order(self, *args, **kwargs):
		return self._BandStopFilter.get_Order(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._BandStopFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._BandStopFilter.Overloads(self, *args, **kwargs)