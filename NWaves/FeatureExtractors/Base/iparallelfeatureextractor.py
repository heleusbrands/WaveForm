from ...wrapper import NWaves 


 

class IParallelFeatureExtractor:

	def __init__(self, /, *args, **kwargs):
		self._IParallelFeatureExtractor = NWaves.FeatureExtractors.Base.IParallelFeatureExtractor(self, args, kwargs)
 
	def equals(self, obj):
		return self._IParallelFeatureExtractor.Equals(obj)
 
	def get_hash_code(self, *args, **kwargs):
		return self._IParallelFeatureExtractor.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._IParallelFeatureExtractor.GetType(*args, **kwargs)
 
	def parallel_compute_from(self, *args, **kwargs):
		return self._IParallelFeatureExtractor.ParallelComputeFrom(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._IParallelFeatureExtractor.ToString(*args, **kwargs)