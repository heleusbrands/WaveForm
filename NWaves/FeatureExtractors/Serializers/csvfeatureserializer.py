from ...wrapper import NWaves 


 

class CsvFeatureSerializer:

	def __init__(self, featureVectors, timeMarkers=None, featureNames=None, delimiter=','):
		self._CsvFeatureSerializer = NWaves.FeatureExtractors.Serializers.CsvFeatureSerializer(featureVectors, timeMarkers, featureNames, delimiter)
 
	def equals(self, *args, **kwargs):
		return self._CsvFeatureSerializer.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._CsvFeatureSerializer.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._CsvFeatureSerializer.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._CsvFeatureSerializer.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._CsvFeatureSerializer.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, featureVectors, timeMarkers=None, featureNames=None, delimiter=','):
		return self._CsvFeatureSerializer.Overloads(featureVectors, timeMarkers, featureNames, delimiter)
 
	def reference_equals(self, objA, objB):
		return self._CsvFeatureSerializer.ReferenceEquals(objA, objB)
 
	def serialize_async(self, stream, format=0.00000, timeFormat='0.000'):
		return self._CsvFeatureSerializer.SerializeAsync(stream, format, timeFormat)
 
	def to_string(self, *args, **kwargs):
		return self._CsvFeatureSerializer.ToString(*args, **kwargs)