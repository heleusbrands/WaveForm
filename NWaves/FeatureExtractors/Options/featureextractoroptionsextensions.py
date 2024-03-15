from ...wrapper import NWaves 


 

class FeatureExtractorOptionsExtensions:

	def __init__(self, *args, **kwargs):
		self._FeatureExtractorOptionsExtensions = NWaves.FeatureExtractors.Options.FeatureExtractorOptionsExtensions(*args, **kwargs)
 
	def cast(self, options):
		return self._FeatureExtractorOptionsExtensions.Cast(options)
 
	def equals(self, *args, **kwargs):
		return self._FeatureExtractorOptionsExtensions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._FeatureExtractorOptionsExtensions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._FeatureExtractorOptionsExtensions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._FeatureExtractorOptionsExtensions.GetType(*args, **kwargs)
 
	def load_options(self, stream):
		return self._FeatureExtractorOptionsExtensions.LoadOptions(stream)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._FeatureExtractorOptionsExtensions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._FeatureExtractorOptionsExtensions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._FeatureExtractorOptionsExtensions.ReferenceEquals(objA, objB)
 
	def save_options(self, stream, options):
		return self._FeatureExtractorOptionsExtensions.SaveOptions(stream, options)
 
	def to_string(self, *args, **kwargs):
		return self._FeatureExtractorOptionsExtensions.ToString(*args, **kwargs)