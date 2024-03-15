from ...wrapper import NWaves 


 

class LpcOptions:

	def __init__(self, *args, **kwargs):
		self._LpcOptions = NWaves.FeatureExtractors.Options.LpcOptions(*args, **kwargs)
		self.Window = self._LpcOptions.Window
		self.SamplingRate = self._LpcOptions.SamplingRate
		self.PreEmphasis = self._LpcOptions.PreEmphasis
		self.LpcOrder = self._LpcOptions.LpcOrder
		self.HopSize = self._LpcOptions.HopSize
		self.HopDuration = self._LpcOptions.HopDuration
		self.FrameSize = self._LpcOptions.FrameSize
		self.FrameDuration = self._LpcOptions.FrameDuration
		self.FeatureCount = self._LpcOptions.FeatureCount
		self.Errors = self._LpcOptions.Errors
 
	def equals(self, *args, **kwargs):
		return self._LpcOptions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._LpcOptions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._LpcOptions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._LpcOptions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._LpcOptions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._LpcOptions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._LpcOptions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._LpcOptions.ToString(*args, **kwargs)
 
	def get_errors(self, *args, **kwargs):
		return self._LpcOptions.get_Errors(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._LpcOptions.get_FeatureCount(*args, **kwargs)
 
	def get_frame_duration(self, *args, **kwargs):
		return self._LpcOptions.get_FrameDuration(*args, **kwargs)
 
	def get_frame_size(self, *args, **kwargs):
		return self._LpcOptions.get_FrameSize(*args, **kwargs)
 
	def get_hop_duration(self, *args, **kwargs):
		return self._LpcOptions.get_HopDuration(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._LpcOptions.get_HopSize(*args, **kwargs)
 
	def get_lpc_order(self, *args, **kwargs):
		return self._LpcOptions.get_LpcOrder(*args, **kwargs)
 
	def get_pre_emphasis(self, *args, **kwargs):
		return self._LpcOptions.get_PreEmphasis(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._LpcOptions.get_SamplingRate(*args, **kwargs)
 
	def get_window(self, *args, **kwargs):
		return self._LpcOptions.get_Window(*args, **kwargs)
 
	def set_feature_count(self, value):
		return self._LpcOptions.set_FeatureCount(value)
 
	def set_frame_duration(self, value):
		return self._LpcOptions.set_FrameDuration(value)
 
	def set_frame_size(self, value):
		return self._LpcOptions.set_FrameSize(value)
 
	def set_hop_duration(self, value):
		return self._LpcOptions.set_HopDuration(value)
 
	def set_hop_size(self, value):
		return self._LpcOptions.set_HopSize(value)
 
	def set_lpc_order(self, value):
		return self._LpcOptions.set_LpcOrder(value)
 
	def set_pre_emphasis(self, value):
		return self._LpcOptions.set_PreEmphasis(value)
 
	def set_sampling_rate(self, value):
		return self._LpcOptions.set_SamplingRate(value)
 
	def set_window(self, value):
		return self._LpcOptions.set_Window(value)