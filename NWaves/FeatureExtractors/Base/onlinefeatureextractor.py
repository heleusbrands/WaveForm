from ...wrapper import NWaves 


 

class OnlineFeatureExtractor:

	def __init__(self, extractor, ignoreLastSamples: bool=False, maxDataSize: int=0):
		self._OnlineFeatureExtractor = NWaves.FeatureExtractors.Base.OnlineFeatureExtractor(extractor, ignoreLastSamples, maxDataSize)
		self.FeatureCount = self._OnlineFeatureExtractor.FeatureCount
		self.Extractor = self._OnlineFeatureExtractor.Extractor
 
	def compute_from(self, *args, **kwargs):
		return self._OnlineFeatureExtractor.ComputeFrom(*args, **kwargs)
 
	def ensure_size(self, dataSize):
		return self._OnlineFeatureExtractor.EnsureSize(dataSize)
 
	def ensure_size_from_seconds(self, seconds):
		return self._OnlineFeatureExtractor.EnsureSizeFromSeconds(seconds)
 
	def equals(self, *args, **kwargs):
		return self._OnlineFeatureExtractor.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._OnlineFeatureExtractor.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._OnlineFeatureExtractor.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._OnlineFeatureExtractor.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._OnlineFeatureExtractor.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, extractor, ignoreLastSamples: bool=False, maxDataSize: int=0):
		return self._OnlineFeatureExtractor.Overloads(extractor, ignoreLastSamples, maxDataSize)
 
	def reference_equals(self, objA, objB):
		return self._OnlineFeatureExtractor.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._OnlineFeatureExtractor.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._OnlineFeatureExtractor.ToString(*args, **kwargs)
 
	def vector_count(self, dataSize):
		return self._OnlineFeatureExtractor.VectorCount(dataSize)
 
	def vector_count_from_seconds(self, seconds):
		return self._OnlineFeatureExtractor.VectorCountFromSeconds(seconds)
 
	def get_extractor(self, *args, **kwargs):
		return self._OnlineFeatureExtractor.get_Extractor(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._OnlineFeatureExtractor.get_FeatureCount(*args, **kwargs)
 
	def set_extractor(self, value):
		return self._OnlineFeatureExtractor.set_Extractor(value)