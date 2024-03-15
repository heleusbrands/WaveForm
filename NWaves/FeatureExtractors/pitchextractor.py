from ..wrapper import NWaves 


 

class PitchExtractor:

	def __init__(self, options):
		self._PitchExtractor = NWaves.FeatureExtractors.PitchExtractor(options)
		self.FeatureDescriptions = self._PitchExtractor.FeatureDescriptions
 
	def get_feature_descriptions(self, *args, **kwargs):
		return self._PitchExtractor.get_FeatureDescriptions(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._PitchExtractor.ProcessFrame(self, *args, **kwargs)
 
	def is_parallelizable(self, *args, **kwargs):
		return self._PitchExtractor.IsParallelizable(self, *args, **kwargs)
 
	def parallel_copy(self, *args, **kwargs):
		return self._PitchExtractor.ParallelCopy(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PitchExtractor.Overloads(self, *args, **kwargs)