from ...wrapper import NWaves 


 

class IFeatureExtractor:

	def __init__(self, /, *args, **kwargs):
		self._IFeatureExtractor = NWaves.FeatureExtractors.Base.IFeatureExtractor(self, args, kwargs)
		self.FeatureCount = self._IFeatureExtractor.FeatureCount
 
	def compute_from(self, *args, **kwargs):
		return self._IFeatureExtractor.ComputeFrom(*args, **kwargs)
 
	def equals(self, obj):
		return self._IFeatureExtractor.Equals(obj)
 
	def get_hash_code(self, *args, **kwargs):
		return self._IFeatureExtractor.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._IFeatureExtractor.GetType(*args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._IFeatureExtractor.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._IFeatureExtractor.ToString(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._IFeatureExtractor.get_FeatureCount(*args, **kwargs)