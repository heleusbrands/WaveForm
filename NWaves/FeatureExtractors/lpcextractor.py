from ..wrapper import NWaves 


 

class LpcExtractor:

	def __init__(self, options):
		self._LpcExtractor = NWaves.FeatureExtractors.LpcExtractor(options)
		self.FeatureDescriptions = self._LpcExtractor.FeatureDescriptions
 
	def get_feature_descriptions(self, *args, **kwargs):
		return self._LpcExtractor.get_FeatureDescriptions(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._LpcExtractor.ProcessFrame(self, *args, **kwargs)
 
	def is_parallelizable(self, *args, **kwargs):
		return self._LpcExtractor.IsParallelizable(self, *args, **kwargs)
 
	def parallel_copy(self, *args, **kwargs):
		return self._LpcExtractor.ParallelCopy(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._LpcExtractor.Overloads(self, *args, **kwargs)