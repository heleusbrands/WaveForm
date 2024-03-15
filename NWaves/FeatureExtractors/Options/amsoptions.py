from ...wrapper import NWaves 


 

class AmsOptions:

	def __init__(self, *args, **kwargs):
		self._AmsOptions = NWaves.FeatureExtractors.Options.AmsOptions(*args, **kwargs)
		self.Window = self._AmsOptions.Window
		self.SamplingRate = self._AmsOptions.SamplingRate
		self.PreEmphasis = self._AmsOptions.PreEmphasis
		self.ModulationHopSize = self._AmsOptions.ModulationHopSize
		self.ModulationFftSize = self._AmsOptions.ModulationFftSize
		self.HopSize = self._AmsOptions.HopSize
		self.HopDuration = self._AmsOptions.HopDuration
		self.FrameSize = self._AmsOptions.FrameSize
		self.FrameDuration = self._AmsOptions.FrameDuration
		self.FilterBank = self._AmsOptions.FilterBank
		self.FftSize = self._AmsOptions.FftSize
		self.Featuregram = self._AmsOptions.Featuregram
		self.FeatureCount = self._AmsOptions.FeatureCount
		self.Errors = self._AmsOptions.Errors
 
	def equals(self, *args, **kwargs):
		return self._AmsOptions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._AmsOptions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._AmsOptions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._AmsOptions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._AmsOptions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._AmsOptions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._AmsOptions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._AmsOptions.ToString(*args, **kwargs)
 
	def get_errors(self, *args, **kwargs):
		return self._AmsOptions.get_Errors(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._AmsOptions.get_FeatureCount(*args, **kwargs)
 
	def get_featuregram(self, *args, **kwargs):
		return self._AmsOptions.get_Featuregram(*args, **kwargs)
 
	def get_fft_size(self, *args, **kwargs):
		return self._AmsOptions.get_FftSize(*args, **kwargs)
 
	def get_filter_bank(self, *args, **kwargs):
		return self._AmsOptions.get_FilterBank(*args, **kwargs)
 
	def get_frame_duration(self, *args, **kwargs):
		return self._AmsOptions.get_FrameDuration(*args, **kwargs)
 
	def get_frame_size(self, *args, **kwargs):
		return self._AmsOptions.get_FrameSize(*args, **kwargs)
 
	def get_hop_duration(self, *args, **kwargs):
		return self._AmsOptions.get_HopDuration(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._AmsOptions.get_HopSize(*args, **kwargs)
 
	def get_modulation_fft_size(self, *args, **kwargs):
		return self._AmsOptions.get_ModulationFftSize(*args, **kwargs)
 
	def get_modulation_hop_size(self, *args, **kwargs):
		return self._AmsOptions.get_ModulationHopSize(*args, **kwargs)
 
	def get_pre_emphasis(self, *args, **kwargs):
		return self._AmsOptions.get_PreEmphasis(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._AmsOptions.get_SamplingRate(*args, **kwargs)
 
	def get_window(self, *args, **kwargs):
		return self._AmsOptions.get_Window(*args, **kwargs)
 
	def set_feature_count(self, value):
		return self._AmsOptions.set_FeatureCount(value)
 
	def set_featuregram(self, value):
		return self._AmsOptions.set_Featuregram(value)
 
	def set_fft_size(self, value):
		return self._AmsOptions.set_FftSize(value)
 
	def set_filter_bank(self, value):
		return self._AmsOptions.set_FilterBank(value)
 
	def set_frame_duration(self, value):
		return self._AmsOptions.set_FrameDuration(value)
 
	def set_frame_size(self, value):
		return self._AmsOptions.set_FrameSize(value)
 
	def set_hop_duration(self, value):
		return self._AmsOptions.set_HopDuration(value)
 
	def set_hop_size(self, value):
		return self._AmsOptions.set_HopSize(value)
 
	def set_modulation_fft_size(self, value):
		return self._AmsOptions.set_ModulationFftSize(value)
 
	def set_modulation_hop_size(self, value):
		return self._AmsOptions.set_ModulationHopSize(value)
 
	def set_pre_emphasis(self, value):
		return self._AmsOptions.set_PreEmphasis(value)
 
	def set_sampling_rate(self, value):
		return self._AmsOptions.set_SamplingRate(value)
 
	def set_window(self, value):
		return self._AmsOptions.set_Window(value)