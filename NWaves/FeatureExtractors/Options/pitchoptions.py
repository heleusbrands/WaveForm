from ...wrapper import NWaves 


 

class PitchOptions:

	def __init__(self, *args, **kwargs):
		self._PitchOptions = NWaves.FeatureExtractors.Options.PitchOptions(*args, **kwargs)
		self.Window = self._PitchOptions.Window
		self.SamplingRate = self._PitchOptions.SamplingRate
		self.PreEmphasis = self._PitchOptions.PreEmphasis
		self.LowFrequency = self._PitchOptions.LowFrequency
		self.HopSize = self._PitchOptions.HopSize
		self.HopDuration = self._PitchOptions.HopDuration
		self.HighFrequency = self._PitchOptions.HighFrequency
		self.FrameSize = self._PitchOptions.FrameSize
		self.FrameDuration = self._PitchOptions.FrameDuration
		self.FeatureCount = self._PitchOptions.FeatureCount
		self.Errors = self._PitchOptions.Errors
 
	def equals(self, *args, **kwargs):
		return self._PitchOptions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._PitchOptions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._PitchOptions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._PitchOptions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._PitchOptions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PitchOptions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._PitchOptions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._PitchOptions.ToString(*args, **kwargs)
 
	def get_errors(self, *args, **kwargs):
		return self._PitchOptions.get_Errors(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._PitchOptions.get_FeatureCount(*args, **kwargs)
 
	def get_frame_duration(self, *args, **kwargs):
		return self._PitchOptions.get_FrameDuration(*args, **kwargs)
 
	def get_frame_size(self, *args, **kwargs):
		return self._PitchOptions.get_FrameSize(*args, **kwargs)
 
	def get_high_frequency(self, *args, **kwargs):
		return self._PitchOptions.get_HighFrequency(*args, **kwargs)
 
	def get_hop_duration(self, *args, **kwargs):
		return self._PitchOptions.get_HopDuration(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._PitchOptions.get_HopSize(*args, **kwargs)
 
	def get_low_frequency(self, *args, **kwargs):
		return self._PitchOptions.get_LowFrequency(*args, **kwargs)
 
	def get_pre_emphasis(self, *args, **kwargs):
		return self._PitchOptions.get_PreEmphasis(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._PitchOptions.get_SamplingRate(*args, **kwargs)
 
	def get_window(self, *args, **kwargs):
		return self._PitchOptions.get_Window(*args, **kwargs)
 
	def set_feature_count(self, value):
		return self._PitchOptions.set_FeatureCount(value)
 
	def set_frame_duration(self, value):
		return self._PitchOptions.set_FrameDuration(value)
 
	def set_frame_size(self, value):
		return self._PitchOptions.set_FrameSize(value)
 
	def set_high_frequency(self, value):
		return self._PitchOptions.set_HighFrequency(value)
 
	def set_hop_duration(self, value):
		return self._PitchOptions.set_HopDuration(value)
 
	def set_hop_size(self, value):
		return self._PitchOptions.set_HopSize(value)
 
	def set_low_frequency(self, value):
		return self._PitchOptions.set_LowFrequency(value)
 
	def set_pre_emphasis(self, value):
		return self._PitchOptions.set_PreEmphasis(value)
 
	def set_sampling_rate(self, value):
		return self._PitchOptions.set_SamplingRate(value)
 
	def set_window(self, value):
		return self._PitchOptions.set_Window(value)