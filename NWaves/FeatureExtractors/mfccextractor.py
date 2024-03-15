from ..wrapper import NWaves 


 

class MfccExtractor:

	def __init__(self, options):
		self._MfccExtractor = NWaves.FeatureExtractors.MfccExtractor(options)
		self.FilterBank = self._MfccExtractor.FilterBank
		self.FeatureDescriptions = self._MfccExtractor.FeatureDescriptions
 
	def get_feature_descriptions(self, *args, **kwargs):
		return self._MfccExtractor.get_FeatureDescriptions(self, *args, **kwargs)
 
	def get_filter_bank(self, *args, **kwargs):
		return self._MfccExtractor.get_FilterBank(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._MfccExtractor.ProcessFrame(self, *args, **kwargs)
 
	def is_parallelizable(self, *args, **kwargs):
		return self._MfccExtractor.IsParallelizable(self, *args, **kwargs)
 
	def parallel_copy(self, *args, **kwargs):
		return self._MfccExtractor.ParallelCopy(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._MfccExtractor.Overloads(self, *args, **kwargs)