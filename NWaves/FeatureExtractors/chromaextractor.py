from ..wrapper import NWaves 


 

class ChromaExtractor:

	def __init__(self, options):
		self._ChromaExtractor = NWaves.FeatureExtractors.ChromaExtractor(options)
		self.FilterBank = self._ChromaExtractor.FilterBank
		self.FeatureDescriptions = self._ChromaExtractor.FeatureDescriptions
 
	def get_feature_descriptions(self, *args, **kwargs):
		return self._ChromaExtractor.get_FeatureDescriptions(self, *args, **kwargs)
 
	def get_filter_bank(self, *args, **kwargs):
		return self._ChromaExtractor.get_FilterBank(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._ChromaExtractor.ProcessFrame(self, *args, **kwargs)
 
	def is_parallelizable(self, *args, **kwargs):
		return self._ChromaExtractor.IsParallelizable(self, *args, **kwargs)
 
	def parallel_copy(self, *args, **kwargs):
		return self._ChromaExtractor.ParallelCopy(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._ChromaExtractor.Overloads(self, *args, **kwargs)