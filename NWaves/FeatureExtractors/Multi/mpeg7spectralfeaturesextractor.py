from ...wrapper import NWaves 


 

class Mpeg7SpectralFeaturesExtractor:

	def __init__(self, options):
		self._Mpeg7SpectralFeaturesExtractor = NWaves.FeatureExtractors.Multi.Mpeg7SpectralFeaturesExtractor(options)
		self.HarmonicSet = self._Mpeg7SpectralFeaturesExtractor.HarmonicSet
		self.FeatureSet = self._Mpeg7SpectralFeaturesExtractor.FeatureSet
		self.FeatureDescriptions = self._Mpeg7SpectralFeaturesExtractor.FeatureDescriptions
 
	def get_feature_descriptions(self, *args, **kwargs):
		return self._Mpeg7SpectralFeaturesExtractor.get_FeatureDescriptions(self, *args, **kwargs)
 
	def include_harmonic_features(self, *args, **kwargs):
		return self._Mpeg7SpectralFeaturesExtractor.IncludeHarmonicFeatures(self, *args, **kwargs)
 
	def add_harmonic_feature(self, *args, **kwargs):
		return self._Mpeg7SpectralFeaturesExtractor.AddHarmonicFeature(self, *args, **kwargs)
 
	def set_pitch_track(self, *args, **kwargs):
		return self._Mpeg7SpectralFeaturesExtractor.SetPitchTrack(self, *args, **kwargs)
 
	def compute_from(self, *args, **kwargs):
		return self._Mpeg7SpectralFeaturesExtractor.ComputeFrom(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._Mpeg7SpectralFeaturesExtractor.ProcessFrame(self, *args, **kwargs)
 
	def is_parallelizable(self, *args, **kwargs):
		return self._Mpeg7SpectralFeaturesExtractor.IsParallelizable(self, *args, **kwargs)
 
	def parallel_copy(self, *args, **kwargs):
		return self._Mpeg7SpectralFeaturesExtractor.ParallelCopy(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._Mpeg7SpectralFeaturesExtractor.Overloads(self, *args, **kwargs)