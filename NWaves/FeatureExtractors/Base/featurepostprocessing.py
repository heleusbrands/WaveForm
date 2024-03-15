from ...wrapper import NWaves 


 

class FeaturePostProcessing:

	def __init__(self, *args, **kwargs):
		self._FeaturePostProcessing = NWaves.FeatureExtractors.Base.FeaturePostProcessing(*args, **kwargs)
 
	def add_deltas(self, vectors, previous=N: intone, next=N: intone, includeDeltaDelta: bool=True, N: int=2):
		return self._FeaturePostProcessing.AddDeltas(vectors, previous, next, includeDeltaDelta, N)
 
	def equals(self, *args, **kwargs):
		return self._FeaturePostProcessing.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._FeaturePostProcessing.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._FeaturePostProcessing.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._FeaturePostProcessing.GetType(*args, **kwargs)
 
	def join(self, vectors):
		return self._FeaturePostProcessing.Join(vectors)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._FeaturePostProcessing.MemberwiseClone(*args, **kwargs)
 
	def normalize_mean(self, vectors):
		return self._FeaturePostProcessing.NormalizeMean(vectors)
 
	def normalize_variance(self, vectors, bias: int=1):
		return self._FeaturePostProcessing.NormalizeVariance(vectors, bias)
 
	def overloads(self, *args, **kwargs):
		return self._FeaturePostProcessing.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._FeaturePostProcessing.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._FeaturePostProcessing.ToString(*args, **kwargs)