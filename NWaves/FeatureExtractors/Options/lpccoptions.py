from ...wrapper import NWaves 


 

class LpccOptions:

	def __init__(self, *args, **kwargs):
		self._LpccOptions = NWaves.FeatureExtractors.Options.LpccOptions(*args, **kwargs)
		self.Window = self._LpccOptions.Window
		self.SamplingRate = self._LpccOptions.SamplingRate
		self.PreEmphasis = self._LpccOptions.PreEmphasis
		self.LpcOrder = self._LpccOptions.LpcOrder
		self.LifterSize = self._LpccOptions.LifterSize
		self.HopSize = self._LpccOptions.HopSize
		self.HopDuration = self._LpccOptions.HopDuration
		self.FrameSize = self._LpccOptions.FrameSize
		self.FrameDuration = self._LpccOptions.FrameDuration
		self.FeatureCount = self._LpccOptions.FeatureCount
		self.Errors = self._LpccOptions.Errors
 
	def equals(self, *args, **kwargs):
		return self._LpccOptions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._LpccOptions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._LpccOptions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._LpccOptions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._LpccOptions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._LpccOptions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._LpccOptions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._LpccOptions.ToString(*args, **kwargs)
 
	def get_errors(self, *args, **kwargs):
		return self._LpccOptions.get_Errors(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._LpccOptions.get_FeatureCount(*args, **kwargs)
 
	def get_frame_duration(self, *args, **kwargs):
		return self._LpccOptions.get_FrameDuration(*args, **kwargs)
 
	def get_frame_size(self, *args, **kwargs):
		return self._LpccOptions.get_FrameSize(*args, **kwargs)
 
	def get_hop_duration(self, *args, **kwargs):
		return self._LpccOptions.get_HopDuration(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._LpccOptions.get_HopSize(*args, **kwargs)
 
	def get_lifter_size(self, *args, **kwargs):
		return self._LpccOptions.get_LifterSize(*args, **kwargs)
 
	def get_lpc_order(self, *args, **kwargs):
		return self._LpccOptions.get_LpcOrder(*args, **kwargs)
 
	def get_pre_emphasis(self, *args, **kwargs):
		return self._LpccOptions.get_PreEmphasis(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._LpccOptions.get_SamplingRate(*args, **kwargs)
 
	def get_window(self, *args, **kwargs):
		return self._LpccOptions.get_Window(*args, **kwargs)
 
	def set_feature_count(self, value):
		return self._LpccOptions.set_FeatureCount(value)
 
	def set_frame_duration(self, value):
		return self._LpccOptions.set_FrameDuration(value)
 
	def set_frame_size(self, value):
		return self._LpccOptions.set_FrameSize(value)
 
	def set_hop_duration(self, value):
		return self._LpccOptions.set_HopDuration(value)
 
	def set_hop_size(self, value):
		return self._LpccOptions.set_HopSize(value)
 
	def set_lifter_size(self, value):
		return self._LpccOptions.set_LifterSize(value)
 
	def set_lpc_order(self, value):
		return self._LpccOptions.set_LpcOrder(value)
 
	def set_pre_emphasis(self, value):
		return self._LpccOptions.set_PreEmphasis(value)
 
	def set_sampling_rate(self, value):
		return self._LpccOptions.set_SamplingRate(value)
 
	def set_window(self, value):
		return self._LpccOptions.set_Window(value)