from ..wrapper import NWaves 


 

class WaveletExtractor:

	def __init__(self, options):
		self._WaveletExtractor = NWaves.FeatureExtractors.WaveletExtractor(options)
		self.FeatureDescriptions = self._WaveletExtractor.FeatureDescriptions
 
	def get_feature_descriptions(self, *args, **kwargs):
		return self._WaveletExtractor.get_FeatureDescriptions(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._WaveletExtractor.ProcessFrame(self, *args, **kwargs)
 
	def is_parallelizable(self, *args, **kwargs):
		return self._WaveletExtractor.IsParallelizable(self, *args, **kwargs)
 
	def parallel_copy(self, *args, **kwargs):
		return self._WaveletExtractor.ParallelCopy(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._WaveletExtractor.Overloads(self, *args, **kwargs)