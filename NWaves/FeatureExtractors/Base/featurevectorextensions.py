from ...wrapper import NWaves 


 

class FeatureVectorExtensions:

	def __init__(self, *args, **kwargs):
		self._FeatureVectorExtensions = NWaves.FeatureExtractors.Base.FeatureVectorExtensions(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._FeatureVectorExtensions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._FeatureVectorExtensions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._FeatureVectorExtensions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._FeatureVectorExtensions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._FeatureVectorExtensions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._FeatureVectorExtensions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._FeatureVectorExtensions.ReferenceEquals(objA, objB)
 
	def statistics(self, vector):
		return self._FeatureVectorExtensions.Statistics(vector)
 
	def to_string(self, *args, **kwargs):
		return self._FeatureVectorExtensions.ToString(*args, **kwargs)