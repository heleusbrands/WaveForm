from ..wrapper import NWaves 


 

class PlpExtractor:

	def __init__(self, options):
		self._PlpExtractor = NWaves.FeatureExtractors.PlpExtractor(options)
		self.FilterBank = self._PlpExtractor.FilterBank
		self.FeatureDescriptions = self._PlpExtractor.FeatureDescriptions
 
	def get_feature_descriptions(self, *args, **kwargs):
		return self._PlpExtractor.get_FeatureDescriptions(self, *args, **kwargs)
 
	def get_filter_bank(self, *args, **kwargs):
		return self._PlpExtractor.get_FilterBank(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._PlpExtractor.ProcessFrame(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._PlpExtractor.Reset(self, *args, **kwargs)
 
	def is_parallelizable(self, *args, **kwargs):
		return self._PlpExtractor.IsParallelizable(self, *args, **kwargs)
 
	def parallel_copy(self, *args, **kwargs):
		return self._PlpExtractor.ParallelCopy(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PlpExtractor.Overloads(self, *args, **kwargs)