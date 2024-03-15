from ...wrapper import NWaves 


 

class MultiFeatureOptions:

	def __init__(self, *args, **kwargs):
		self._MultiFeatureOptions = NWaves.FeatureExtractors.Options.MultiFeatureOptions(*args, **kwargs)
		self.Window = self._MultiFeatureOptions.Window
		self.SamplingRate = self._MultiFeatureOptions.SamplingRate
		self.PreEmphasis = self._MultiFeatureOptions.PreEmphasis
		self.Parameters = self._MultiFeatureOptions.Parameters
		self.HopSize = self._MultiFeatureOptions.HopSize
		self.HopDuration = self._MultiFeatureOptions.HopDuration
		self.FrequencyBands = self._MultiFeatureOptions.FrequencyBands
		self.Frequencies = self._MultiFeatureOptions.Frequencies
		self.FrameSize = self._MultiFeatureOptions.FrameSize
		self.FrameDuration = self._MultiFeatureOptions.FrameDuration
		self.FftSize = self._MultiFeatureOptions.FftSize
		self.FeatureList = self._MultiFeatureOptions.FeatureList
		self.FeatureCount = self._MultiFeatureOptions.FeatureCount
		self.Errors = self._MultiFeatureOptions.Errors
 
	def equals(self, *args, **kwargs):
		return self._MultiFeatureOptions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._MultiFeatureOptions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._MultiFeatureOptions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._MultiFeatureOptions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._MultiFeatureOptions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._MultiFeatureOptions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._MultiFeatureOptions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._MultiFeatureOptions.ToString(*args, **kwargs)
 
	def get_errors(self, *args, **kwargs):
		return self._MultiFeatureOptions.get_Errors(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._MultiFeatureOptions.get_FeatureCount(*args, **kwargs)
 
	def get_feature_list(self, *args, **kwargs):
		return self._MultiFeatureOptions.get_FeatureList(*args, **kwargs)
 
	def get_fft_size(self, *args, **kwargs):
		return self._MultiFeatureOptions.get_FftSize(*args, **kwargs)
 
	def get_frame_duration(self, *args, **kwargs):
		return self._MultiFeatureOptions.get_FrameDuration(*args, **kwargs)
 
	def get_frame_size(self, *args, **kwargs):
		return self._MultiFeatureOptions.get_FrameSize(*args, **kwargs)
 
	def get_frequencies(self, *args, **kwargs):
		return self._MultiFeatureOptions.get_Frequencies(*args, **kwargs)
 
	def get_frequency_bands(self, *args, **kwargs):
		return self._MultiFeatureOptions.get_FrequencyBands(*args, **kwargs)
 
	def get_hop_duration(self, *args, **kwargs):
		return self._MultiFeatureOptions.get_HopDuration(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._MultiFeatureOptions.get_HopSize(*args, **kwargs)
 
	def get_parameters(self, *args, **kwargs):
		return self._MultiFeatureOptions.get_Parameters(*args, **kwargs)
 
	def get_pre_emphasis(self, *args, **kwargs):
		return self._MultiFeatureOptions.get_PreEmphasis(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._MultiFeatureOptions.get_SamplingRate(*args, **kwargs)
 
	def get_window(self, *args, **kwargs):
		return self._MultiFeatureOptions.get_Window(*args, **kwargs)
 
	def set_feature_count(self, value):
		return self._MultiFeatureOptions.set_FeatureCount(value)
 
	def set_feature_list(self, value):
		return self._MultiFeatureOptions.set_FeatureList(value)
 
	def set_fft_size(self, value):
		return self._MultiFeatureOptions.set_FftSize(value)
 
	def set_frame_duration(self, value):
		return self._MultiFeatureOptions.set_FrameDuration(value)
 
	def set_frame_size(self, value):
		return self._MultiFeatureOptions.set_FrameSize(value)
 
	def set_frequencies(self, value):
		return self._MultiFeatureOptions.set_Frequencies(value)
 
	def set_frequency_bands(self, value):
		return self._MultiFeatureOptions.set_FrequencyBands(value)
 
	def set_hop_duration(self, value):
		return self._MultiFeatureOptions.set_HopDuration(value)
 
	def set_hop_size(self, value):
		return self._MultiFeatureOptions.set_HopSize(value)
 
	def set_parameters(self, value):
		return self._MultiFeatureOptions.set_Parameters(value)
 
	def set_pre_emphasis(self, value):
		return self._MultiFeatureOptions.set_PreEmphasis(value)
 
	def set_sampling_rate(self, value):
		return self._MultiFeatureOptions.set_SamplingRate(value)
 
	def set_window(self, value):
		return self._MultiFeatureOptions.set_Window(value)