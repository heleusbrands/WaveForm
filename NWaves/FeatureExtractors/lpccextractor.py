from ..wrapper import NWaves 


 

class LpccExtractor:

	def __init__(self, options):
		self._LpccExtractor = NWaves.FeatureExtractors.LpccExtractor(options)
		self.FeatureDescriptions = self._LpccExtractor.FeatureDescriptions
 
	def get_feature_descriptions(self, *args, **kwargs):
		return self._LpccExtractor.get_FeatureDescriptions(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._LpccExtractor.ProcessFrame(self, *args, **kwargs)
 
	def is_parallelizable(self, *args, **kwargs):
		return self._LpccExtractor.IsParallelizable(self, *args, **kwargs)
 
	def parallel_copy(self, *args, **kwargs):
		return self._LpccExtractor.ParallelCopy(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._LpccExtractor.Overloads(self, *args, **kwargs)