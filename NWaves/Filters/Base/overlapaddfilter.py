from ...wrapper import NWaves 


 

class OverlapAddFilter:

	def __init__(self, h: int, fftSize: int=0):
		self._OverlapAddFilter = NWaves.Filters.Base.OverlapAddFilter(hopSize, fftSize)
 
	def process(self, *args, **kwargs):
		return self._OverlapAddFilter.Process(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._OverlapAddFilter.ProcessFrame(self, *args, **kwargs)
 
	def process_spectrum(self, *args, **kwargs):
		return self._OverlapAddFilter.ProcessSpectrum(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._OverlapAddFilter.Reset(self, *args, **kwargs)
 
	def apply_to(self, *args, **kwargs):
		return self._OverlapAddFilter.ApplyTo(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._OverlapAddFilter.Overloads(self, *args, **kwargs)