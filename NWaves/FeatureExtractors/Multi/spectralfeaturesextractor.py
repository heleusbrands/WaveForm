from ...wrapper import NWaves 


 

class SpectralFeaturesExtractor:

	def __init__(self, options):
		self._SpectralFeaturesExtractor = NWaves.FeatureExtractors.Multi.SpectralFeaturesExtractor(options)
		self.FeatureSet = self._SpectralFeaturesExtractor.FeatureSet
		self.FeatureDescriptions = self._SpectralFeaturesExtractor.FeatureDescriptions
 
	def get_feature_descriptions(self, *args, **kwargs):
		return self._SpectralFeaturesExtractor.get_FeatureDescriptions(self, *args, **kwargs)
 
	def add_feature(self, *args, **kwargs):
		return self._SpectralFeaturesExtractor.AddFeature(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._SpectralFeaturesExtractor.ProcessFrame(self, *args, **kwargs)
 
	def is_parallelizable(self, *args, **kwargs):
		return self._SpectralFeaturesExtractor.IsParallelizable(self, *args, **kwargs)
 
	def parallel_copy(self, *args, **kwargs):
		return self._SpectralFeaturesExtractor.ParallelCopy(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._SpectralFeaturesExtractor.Overloads(self, *args, **kwargs)