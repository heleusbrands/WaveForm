from ...wrapper import NWaves 


 

class MfccOptions:

	def __init__(self, *args, **kwargs):
		self._MfccOptions = NWaves.FeatureExtractors.Options.MfccOptions(*args, **kwargs)
		self.Window = self._MfccOptions.Window
		self.SpectrumType = self._MfccOptions.SpectrumType
		self.SamplingRate = self._MfccOptions.SamplingRate
		self.PreEmphasis = self._MfccOptions.PreEmphasis
		self.NonLinearity = self._MfccOptions.NonLinearity
		self.LowFrequency = self._MfccOptions.LowFrequency
		self.LogFloor = self._MfccOptions.LogFloor
		self.LogEnergyFloor = self._MfccOptions.LogEnergyFloor
		self.LifterSize = self._MfccOptions.LifterSize
		self.IncludeEnergy = self._MfccOptions.IncludeEnergy
		self.HopSize = self._MfccOptions.HopSize
		self.HopDuration = self._MfccOptions.HopDuration
		self.HighFrequency = self._MfccOptions.HighFrequency
		self.FrameSize = self._MfccOptions.FrameSize
		self.FrameDuration = self._MfccOptions.FrameDuration
		self.FilterBankSize = self._MfccOptions.FilterBankSize
		self.FilterBank = self._MfccOptions.FilterBank
		self.FftSize = self._MfccOptions.FftSize
		self.FeatureCount = self._MfccOptions.FeatureCount
		self.Errors = self._MfccOptions.Errors
		self.DctType = self._MfccOptions.DctType
 
	def equals(self, *args, **kwargs):
		return self._MfccOptions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._MfccOptions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._MfccOptions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._MfccOptions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._MfccOptions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._MfccOptions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._MfccOptions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._MfccOptions.ToString(*args, **kwargs)
 
	def get_dct_type(self, *args, **kwargs):
		return self._MfccOptions.get_DctType(*args, **kwargs)
 
	def get_errors(self, *args, **kwargs):
		return self._MfccOptions.get_Errors(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._MfccOptions.get_FeatureCount(*args, **kwargs)
 
	def get_fft_size(self, *args, **kwargs):
		return self._MfccOptions.get_FftSize(*args, **kwargs)
 
	def get_filter_bank(self, *args, **kwargs):
		return self._MfccOptions.get_FilterBank(*args, **kwargs)
 
	def get_filter_bank_size(self, *args, **kwargs):
		return self._MfccOptions.get_FilterBankSize(*args, **kwargs)
 
	def get_frame_duration(self, *args, **kwargs):
		return self._MfccOptions.get_FrameDuration(*args, **kwargs)
 
	def get_frame_size(self, *args, **kwargs):
		return self._MfccOptions.get_FrameSize(*args, **kwargs)
 
	def get_high_frequency(self, *args, **kwargs):
		return self._MfccOptions.get_HighFrequency(*args, **kwargs)
 
	def get_hop_duration(self, *args, **kwargs):
		return self._MfccOptions.get_HopDuration(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._MfccOptions.get_HopSize(*args, **kwargs)
 
	def get_include_energy(self, *args, **kwargs):
		return self._MfccOptions.get_IncludeEnergy(*args, **kwargs)
 
	def get_lifter_size(self, *args, **kwargs):
		return self._MfccOptions.get_LifterSize(*args, **kwargs)
 
	def get_log_energy_floor(self, *args, **kwargs):
		return self._MfccOptions.get_LogEnergyFloor(*args, **kwargs)
 
	def get_log_floor(self, *args, **kwargs):
		return self._MfccOptions.get_LogFloor(*args, **kwargs)
 
	def get_low_frequency(self, *args, **kwargs):
		return self._MfccOptions.get_LowFrequency(*args, **kwargs)
 
	def get_non_linearity(self, *args, **kwargs):
		return self._MfccOptions.get_NonLinearity(*args, **kwargs)
 
	def get_pre_emphasis(self, *args, **kwargs):
		return self._MfccOptions.get_PreEmphasis(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._MfccOptions.get_SamplingRate(*args, **kwargs)
 
	def get_spectrum_type(self, *args, **kwargs):
		return self._MfccOptions.get_SpectrumType(*args, **kwargs)
 
	def get_window(self, *args, **kwargs):
		return self._MfccOptions.get_Window(*args, **kwargs)
 
	def set_dct_type(self, value):
		return self._MfccOptions.set_DctType(value)
 
	def set_feature_count(self, value):
		return self._MfccOptions.set_FeatureCount(value)
 
	def set_fft_size(self, value):
		return self._MfccOptions.set_FftSize(value)
 
	def set_filter_bank(self, value):
		return self._MfccOptions.set_FilterBank(value)
 
	def set_filter_bank_size(self, value):
		return self._MfccOptions.set_FilterBankSize(value)
 
	def set_frame_duration(self, value):
		return self._MfccOptions.set_FrameDuration(value)
 
	def set_frame_size(self, value):
		return self._MfccOptions.set_FrameSize(value)
 
	def set_high_frequency(self, value):
		return self._MfccOptions.set_HighFrequency(value)
 
	def set_hop_duration(self, value):
		return self._MfccOptions.set_HopDuration(value)
 
	def set_hop_size(self, value):
		return self._MfccOptions.set_HopSize(value)
 
	def set_include_energy(self, value):
		return self._MfccOptions.set_IncludeEnergy(value)
 
	def set_lifter_size(self, value):
		return self._MfccOptions.set_LifterSize(value)
 
	def set_log_energy_floor(self, value):
		return self._MfccOptions.set_LogEnergyFloor(value)
 
	def set_log_floor(self, value):
		return self._MfccOptions.set_LogFloor(value)
 
	def set_low_frequency(self, value):
		return self._MfccOptions.set_LowFrequency(value)
 
	def set_non_linearity(self, value):
		return self._MfccOptions.set_NonLinearity(value)
 
	def set_pre_emphasis(self, value):
		return self._MfccOptions.set_PreEmphasis(value)
 
	def set_sampling_rate(self, value):
		return self._MfccOptions.set_SamplingRate(value)
 
	def set_spectrum_type(self, value):
		return self._MfccOptions.set_SpectrumType(value)
 
	def set_window(self, value):
		return self._MfccOptions.set_Window(value)