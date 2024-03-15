from ...wrapper import NWaves 


 

class FeatureExtractorOptions:

	def __init__(self, *args, **kwargs):
		self._FeatureExtractorOptions = NWaves.FeatureExtractors.Options.FeatureExtractorOptions(*args, **kwargs)
		self.Window = self._FeatureExtractorOptions.Window
		self.SamplingRate = self._FeatureExtractorOptions.SamplingRate
		self.PreEmphasis = self._FeatureExtractorOptions.PreEmphasis
		self.HopSize = self._FeatureExtractorOptions.HopSize
		self.HopDuration = self._FeatureExtractorOptions.HopDuration
		self.FrameSize = self._FeatureExtractorOptions.FrameSize
		self.FrameDuration = self._FeatureExtractorOptions.FrameDuration
		self.FeatureCount = self._FeatureExtractorOptions.FeatureCount
		self.Errors = self._FeatureExtractorOptions.Errors
 
	def equals(self, *args, **kwargs):
		return self._FeatureExtractorOptions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._FeatureExtractorOptions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._FeatureExtractorOptions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._FeatureExtractorOptions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._FeatureExtractorOptions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._FeatureExtractorOptions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._FeatureExtractorOptions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._FeatureExtractorOptions.ToString(*args, **kwargs)
 
	def get_errors(self, *args, **kwargs):
		return self._FeatureExtractorOptions.get_Errors(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._FeatureExtractorOptions.get_FeatureCount(*args, **kwargs)
 
	def get_frame_duration(self, *args, **kwargs):
		return self._FeatureExtractorOptions.get_FrameDuration(*args, **kwargs)
 
	def get_frame_size(self, *args, **kwargs):
		return self._FeatureExtractorOptions.get_FrameSize(*args, **kwargs)
 
	def get_hop_duration(self, *args, **kwargs):
		return self._FeatureExtractorOptions.get_HopDuration(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._FeatureExtractorOptions.get_HopSize(*args, **kwargs)
 
	def get_pre_emphasis(self, *args, **kwargs):
		return self._FeatureExtractorOptions.get_PreEmphasis(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._FeatureExtractorOptions.get_SamplingRate(*args, **kwargs)
 
	def get_window(self, *args, **kwargs):
		return self._FeatureExtractorOptions.get_Window(*args, **kwargs)
 
	def set_feature_count(self, value):
		return self._FeatureExtractorOptions.set_FeatureCount(value)
 
	def set_frame_duration(self, value):
		return self._FeatureExtractorOptions.set_FrameDuration(value)
 
	def set_frame_size(self, value):
		return self._FeatureExtractorOptions.set_FrameSize(value)
 
	def set_hop_duration(self, value):
		return self._FeatureExtractorOptions.set_HopDuration(value)
 
	def set_hop_size(self, value):
		return self._FeatureExtractorOptions.set_HopSize(value)
 
	def set_pre_emphasis(self, value):
		return self._FeatureExtractorOptions.set_PreEmphasis(value)
 
	def set_sampling_rate(self, value):
		return self._FeatureExtractorOptions.set_SamplingRate(value)
 
	def set_window(self, value):
		return self._FeatureExtractorOptions.set_Window(value)