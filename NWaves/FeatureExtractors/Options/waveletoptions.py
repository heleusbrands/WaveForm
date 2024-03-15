from ...wrapper import NWaves 


 

class WaveletOptions:

	def __init__(self, *args, **kwargs):
		self._WaveletOptions = NWaves.FeatureExtractors.Options.WaveletOptions(*args, **kwargs)
		self.Window = self._WaveletOptions.Window
		self.WaveletName = self._WaveletOptions.WaveletName
		self.SamplingRate = self._WaveletOptions.SamplingRate
		self.PreEmphasis = self._WaveletOptions.PreEmphasis
		self.HopSize = self._WaveletOptions.HopSize
		self.HopDuration = self._WaveletOptions.HopDuration
		self.FwtSize = self._WaveletOptions.FwtSize
		self.FwtLevel = self._WaveletOptions.FwtLevel
		self.FrameSize = self._WaveletOptions.FrameSize
		self.FrameDuration = self._WaveletOptions.FrameDuration
		self.FeatureCount = self._WaveletOptions.FeatureCount
		self.Errors = self._WaveletOptions.Errors
 
	def equals(self, *args, **kwargs):
		return self._WaveletOptions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._WaveletOptions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._WaveletOptions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._WaveletOptions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._WaveletOptions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._WaveletOptions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._WaveletOptions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._WaveletOptions.ToString(*args, **kwargs)
 
	def get_errors(self, *args, **kwargs):
		return self._WaveletOptions.get_Errors(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._WaveletOptions.get_FeatureCount(*args, **kwargs)
 
	def get_frame_duration(self, *args, **kwargs):
		return self._WaveletOptions.get_FrameDuration(*args, **kwargs)
 
	def get_frame_size(self, *args, **kwargs):
		return self._WaveletOptions.get_FrameSize(*args, **kwargs)
 
	def get_fwt_level(self, *args, **kwargs):
		return self._WaveletOptions.get_FwtLevel(*args, **kwargs)
 
	def get_fwt_size(self, *args, **kwargs):
		return self._WaveletOptions.get_FwtSize(*args, **kwargs)
 
	def get_hop_duration(self, *args, **kwargs):
		return self._WaveletOptions.get_HopDuration(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._WaveletOptions.get_HopSize(*args, **kwargs)
 
	def get_pre_emphasis(self, *args, **kwargs):
		return self._WaveletOptions.get_PreEmphasis(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._WaveletOptions.get_SamplingRate(*args, **kwargs)
 
	def get_wavelet_name(self, *args, **kwargs):
		return self._WaveletOptions.get_WaveletName(*args, **kwargs)
 
	def get_window(self, *args, **kwargs):
		return self._WaveletOptions.get_Window(*args, **kwargs)
 
	def set_feature_count(self, value):
		return self._WaveletOptions.set_FeatureCount(value)
 
	def set_frame_duration(self, value):
		return self._WaveletOptions.set_FrameDuration(value)
 
	def set_frame_size(self, value):
		return self._WaveletOptions.set_FrameSize(value)
 
	def set_fwt_level(self, value):
		return self._WaveletOptions.set_FwtLevel(value)
 
	def set_fwt_size(self, value):
		return self._WaveletOptions.set_FwtSize(value)
 
	def set_hop_duration(self, value):
		return self._WaveletOptions.set_HopDuration(value)
 
	def set_hop_size(self, value):
		return self._WaveletOptions.set_HopSize(value)
 
	def set_pre_emphasis(self, value):
		return self._WaveletOptions.set_PreEmphasis(value)
 
	def set_sampling_rate(self, value):
		return self._WaveletOptions.set_SamplingRate(value)
 
	def set_wavelet_name(self, value):
		return self._WaveletOptions.set_WaveletName(value)
 
	def set_window(self, value):
		return self._WaveletOptions.set_Window(value)