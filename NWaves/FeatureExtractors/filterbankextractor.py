from ..wrapper import NWaves 


 

class FilterbankExtractor:

	def __init__(self, options):
		self._FilterbankExtractor = NWaves.FeatureExtractors.FilterbankExtractor(options)
		self.FilterBank = self._FilterbankExtractor.FilterBank
		self.FeatureDescriptions = self._FilterbankExtractor.FeatureDescriptions
 
	def get_feature_descriptions(self, *args, **kwargs):
		return self._FilterbankExtractor.get_FeatureDescriptions(self, *args, **kwargs)
 
	def get_filter_bank(self, *args, **kwargs):
		return self._FilterbankExtractor.get_FilterBank(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._FilterbankExtractor.ProcessFrame(self, *args, **kwargs)
 
	def is_parallelizable(self, *args, **kwargs):
		return self._FilterbankExtractor.IsParallelizable(self, *args, **kwargs)
 
	def parallel_copy(self, *args, **kwargs):
		return self._FilterbankExtractor.ParallelCopy(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._FilterbankExtractor.Overloads(self, *args, **kwargs)