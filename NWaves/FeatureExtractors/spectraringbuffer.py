from ...wrapper import NWaves 


 

class SpectraRingBuffer:

	def __init__(self, capacity, spectrumSize):
		self._SpectraRingBuffer = NWaves.FeatureExtractors.PnccExtractor.SpectraRingBuffer(capacity, spectrumSize)
		self.AverageSpectrum = self._SpectraRingBuffer.AverageSpectrum
		self.CentralSpectrum = self._SpectraRingBuffer.CentralSpectrum
 
	def add(self, *args, **kwargs):
		return self._SpectraRingBuffer.Add(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._SpectraRingBuffer.Reset(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._SpectraRingBuffer.Overloads(self, *args, **kwargs)