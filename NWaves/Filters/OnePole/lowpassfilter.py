from ...wrapper import NWaves 


 

class LowPassFilter:

	def __init__(self, frequency):
		self._LowPassFilter = NWaves.Filters.OnePole.LowPassFilter(frequency)
		self.Frequency = self._LowPassFilter.Frequency
 
	def get_frequency(self, *args, **kwargs):
		return self._LowPassFilter.get_Frequency(self, *args, **kwargs)
 
	def set_frequency(self, *args, **kwargs):
		return self._LowPassFilter.set_Frequency(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._LowPassFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._LowPassFilter.Overloads(self, *args, **kwargs)