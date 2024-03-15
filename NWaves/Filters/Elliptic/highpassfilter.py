from ...wrapper import NWaves 


 

class HighPassFilter:

	def __init__(self, f: float, o: int, ripplePass=1.0, rippleStop=20.0):
		self._HighPassFilter = NWaves.Filters.Elliptic.HighPassFilter(frequency, order, ripplePass, rippleStop)
		self.Order = self._HighPassFilter.Order
		self.RippleStopband = self._HighPassFilter.RippleStopband
		self.RipplePassband = self._HighPassFilter.RipplePassband
		self.Frequency = self._HighPassFilter.Frequency
 
	def get_frequency(self, *args, **kwargs):
		return self._HighPassFilter.get_Frequency(self, *args, **kwargs)
 
	def get_ripple_passband(self, *args, **kwargs):
		return self._HighPassFilter.get_RipplePassband(self, *args, **kwargs)
 
	def get_ripple_stopband(self, *args, **kwargs):
		return self._HighPassFilter.get_RippleStopband(self, *args, **kwargs)
 
	def get_order(self, *args, **kwargs):
		return self._HighPassFilter.get_Order(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._HighPassFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._HighPassFilter.Overloads(self, *args, **kwargs)