from ...wrapper import NWaves 


 

class LowPassFilter:

	def __init__(self, f: float, o: int, ripplePass=1.0, rippleStop=20.0):
		self._LowPassFilter = NWaves.Filters.Elliptic.LowPassFilter(frequency, order, ripplePass, rippleStop)
		self.Order = self._LowPassFilter.Order
		self.RippleStopband = self._LowPassFilter.RippleStopband
		self.RipplePassband = self._LowPassFilter.RipplePassband
		self.Frequency = self._LowPassFilter.Frequency
 
	def get_frequency(self, *args, **kwargs):
		return self._LowPassFilter.get_Frequency(self, *args, **kwargs)
 
	def get_ripple_passband(self, *args, **kwargs):
		return self._LowPassFilter.get_RipplePassband(self, *args, **kwargs)
 
	def get_ripple_stopband(self, *args, **kwargs):
		return self._LowPassFilter.get_RippleStopband(self, *args, **kwargs)
 
	def get_order(self, *args, **kwargs):
		return self._LowPassFilter.get_Order(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._LowPassFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._LowPassFilter.Overloads(self, *args, **kwargs)