from ...wrapper import NWaves 


 

class FilterbankOptions:

	def __init__(self, *args, **kwargs):
		self._FilterbankOptions = NWaves.FeatureExtractors.Options.FilterbankOptions(*args, **kwargs)
		self.Window = self._FilterbankOptions.Window
		self.SpectrumType = self._FilterbankOptions.SpectrumType
		self.SamplingRate = self._FilterbankOptions.SamplingRate
		self.PreEmphasis = self._FilterbankOptions.PreEmphasis
		self.NonLinearity = self._FilterbankOptions.NonLinearity
		self.LowFrequency = self._FilterbankOptions.LowFrequency
		self.LogFloor = self._FilterbankOptions.LogFloor
		self.HopSize = self._FilterbankOptions.HopSize
		self.HopDuration = self._FilterbankOptions.HopDuration
		self.HighFrequency = self._FilterbankOptions.HighFrequency
		self.FrameSize = self._FilterbankOptions.FrameSize
		self.FrameDuration = self._FilterbankOptions.FrameDuration
		self.FilterBankSize = self._FilterbankOptions.FilterBankSize
		self.FilterBank = self._FilterbankOptions.FilterBank
		self.FftSize = self._FilterbankOptions.FftSize
		self.FeatureCount = self._FilterbankOptions.FeatureCount
		self.Errors = self._FilterbankOptions.Errors
 
	def equals(self, *args, **kwargs):
		return self._FilterbankOptions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._FilterbankOptions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._FilterbankOptions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._FilterbankOptions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._FilterbankOptions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._FilterbankOptions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._FilterbankOptions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._FilterbankOptions.ToString(*args, **kwargs)
 
	def get_errors(self, *args, **kwargs):
		return self._FilterbankOptions.get_Errors(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._FilterbankOptions.get_FeatureCount(*args, **kwargs)
 
	def get_fft_size(self, *args, **kwargs):
		return self._FilterbankOptions.get_FftSize(*args, **kwargs)
 
	def get_filter_bank(self, *args, **kwargs):
		return self._FilterbankOptions.get_FilterBank(*args, **kwargs)
 
	def get_filter_bank_size(self, *args, **kwargs):
		return self._FilterbankOptions.get_FilterBankSize(*args, **kwargs)
 
	def get_frame_duration(self, *args, **kwargs):
		return self._FilterbankOptions.get_FrameDuration(*args, **kwargs)
 
	def get_frame_size(self, *args, **kwargs):
		return self._FilterbankOptions.get_FrameSize(*args, **kwargs)
 
	def get_high_frequency(self, *args, **kwargs):
		return self._FilterbankOptions.get_HighFrequency(*args, **kwargs)
 
	def get_hop_duration(self, *args, **kwargs):
		return self._FilterbankOptions.get_HopDuration(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._FilterbankOptions.get_HopSize(*args, **kwargs)
 
	def get_log_floor(self, *args, **kwargs):
		return self._FilterbankOptions.get_LogFloor(*args, **kwargs)
 
	def get_low_frequency(self, *args, **kwargs):
		return self._FilterbankOptions.get_LowFrequency(*args, **kwargs)
 
	def get_non_linearity(self, *args, **kwargs):
		return self._FilterbankOptions.get_NonLinearity(*args, **kwargs)
 
	def get_pre_emphasis(self, *args, **kwargs):
		return self._FilterbankOptions.get_PreEmphasis(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._FilterbankOptions.get_SamplingRate(*args, **kwargs)
 
	def get_spectrum_type(self, *args, **kwargs):
		return self._FilterbankOptions.get_SpectrumType(*args, **kwargs)
 
	def get_window(self, *args, **kwargs):
		return self._FilterbankOptions.get_Window(*args, **kwargs)
 
	def set_feature_count(self, value):
		return self._FilterbankOptions.set_FeatureCount(value)
 
	def set_fft_size(self, value):
		return self._FilterbankOptions.set_FftSize(value)
 
	def set_filter_bank(self, value):
		return self._FilterbankOptions.set_FilterBank(value)
 
	def set_filter_bank_size(self, value):
		return self._FilterbankOptions.set_FilterBankSize(value)
 
	def set_frame_duration(self, value):
		return self._FilterbankOptions.set_FrameDuration(value)
 
	def set_frame_size(self, value):
		return self._FilterbankOptions.set_FrameSize(value)
 
	def set_high_frequency(self, value):
		return self._FilterbankOptions.set_HighFrequency(value)
 
	def set_hop_duration(self, value):
		return self._FilterbankOptions.set_HopDuration(value)
 
	def set_hop_size(self, value):
		return self._FilterbankOptions.set_HopSize(value)
 
	def set_log_floor(self, value):
		return self._FilterbankOptions.set_LogFloor(value)
 
	def set_low_frequency(self, value):
		return self._FilterbankOptions.set_LowFrequency(value)
 
	def set_non_linearity(self, value):
		return self._FilterbankOptions.set_NonLinearity(value)
 
	def set_pre_emphasis(self, value):
		return self._FilterbankOptions.set_PreEmphasis(value)
 
	def set_sampling_rate(self, value):
		return self._FilterbankOptions.set_SamplingRate(value)
 
	def set_spectrum_type(self, value):
		return self._FilterbankOptions.set_SpectrumType(value)
 
	def set_window(self, value):
		return self._FilterbankOptions.set_Window(value)