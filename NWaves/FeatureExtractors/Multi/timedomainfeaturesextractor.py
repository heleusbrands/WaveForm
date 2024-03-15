from ...wrapper import NWaves 


 

class TimeDomainFeaturesExtractor:

	def __init__(self, options):
		self._TimeDomainFeaturesExtractor = NWaves.FeatureExtractors.Multi.TimeDomainFeaturesExtractor(options)
		self.FeatureSet = self._TimeDomainFeaturesExtractor.FeatureSet
		self.FeatureDescriptions = self._TimeDomainFeaturesExtractor.FeatureDescriptions
 
	def get_feature_descriptions(self, *args, **kwargs):
		return self._TimeDomainFeaturesExtractor.get_FeatureDescriptions(self, *args, **kwargs)
 
	def add_feature(self, *args, **kwargs):
		return self._TimeDomainFeaturesExtractor.AddFeature(self, *args, **kwargs)
 
	def compute_from(self, *args, **kwargs):
		return self._TimeDomainFeaturesExtractor.ComputeFrom(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._TimeDomainFeaturesExtractor.ProcessFrame(self, *args, **kwargs)
 
	def is_parallelizable(self, *args, **kwargs):
		return self._TimeDomainFeaturesExtractor.IsParallelizable(self, *args, **kwargs)
 
	def parallel_copy(self, *args, **kwargs):
		return self._TimeDomainFeaturesExtractor.ParallelCopy(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._TimeDomainFeaturesExtractor.Overloads(self, *args, **kwargs)