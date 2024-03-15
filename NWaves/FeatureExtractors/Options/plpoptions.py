from ...wrapper import NWaves 


 

class PlpOptions:

	def __init__(self, *args, **kwargs):
		self._PlpOptions = NWaves.FeatureExtractors.Options.PlpOptions(*args, **kwargs)
		self.Window = self._PlpOptions.Window
		self.SpectrumType = self._PlpOptions.SpectrumType
		self.SamplingRate = self._PlpOptions.SamplingRate
		self.Rasta = self._PlpOptions.Rasta
		self.PreEmphasis = self._PlpOptions.PreEmphasis
		self.NonLinearity = self._PlpOptions.NonLinearity
		self.LpcOrder = self._PlpOptions.LpcOrder
		self.LowFrequency = self._PlpOptions.LowFrequency
		self.LogFloor = self._PlpOptions.LogFloor
		self.LogEnergyFloor = self._PlpOptions.LogEnergyFloor
		self.LifterSize = self._PlpOptions.LifterSize
		self.IncludeEnergy = self._PlpOptions.IncludeEnergy
		self.HopSize = self._PlpOptions.HopSize
		self.HopDuration = self._PlpOptions.HopDuration
		self.HighFrequency = self._PlpOptions.HighFrequency
		self.FrameSize = self._PlpOptions.FrameSize
		self.FrameDuration = self._PlpOptions.FrameDuration
		self.FilterBankSize = self._PlpOptions.FilterBankSize
		self.FilterBank = self._PlpOptions.FilterBank
		self.FftSize = self._PlpOptions.FftSize
		self.FeatureCount = self._PlpOptions.FeatureCount
		self.Errors = self._PlpOptions.Errors
		self.CenterFrequencies = self._PlpOptions.CenterFrequencies
 
	def equals(self, *args, **kwargs):
		return self._PlpOptions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._PlpOptions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._PlpOptions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._PlpOptions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._PlpOptions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PlpOptions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._PlpOptions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._PlpOptions.ToString(*args, **kwargs)
 
	def get_center_frequencies(self, *args, **kwargs):
		return self._PlpOptions.get_CenterFrequencies(*args, **kwargs)
 
	def get_errors(self, *args, **kwargs):
		return self._PlpOptions.get_Errors(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._PlpOptions.get_FeatureCount(*args, **kwargs)
 
	def get_fft_size(self, *args, **kwargs):
		return self._PlpOptions.get_FftSize(*args, **kwargs)
 
	def get_filter_bank(self, *args, **kwargs):
		return self._PlpOptions.get_FilterBank(*args, **kwargs)
 
	def get_filter_bank_size(self, *args, **kwargs):
		return self._PlpOptions.get_FilterBankSize(*args, **kwargs)
 
	def get_frame_duration(self, *args, **kwargs):
		return self._PlpOptions.get_FrameDuration(*args, **kwargs)
 
	def get_frame_size(self, *args, **kwargs):
		return self._PlpOptions.get_FrameSize(*args, **kwargs)
 
	def get_high_frequency(self, *args, **kwargs):
		return self._PlpOptions.get_HighFrequency(*args, **kwargs)
 
	def get_hop_duration(self, *args, **kwargs):
		return self._PlpOptions.get_HopDuration(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._PlpOptions.get_HopSize(*args, **kwargs)
 
	def get_include_energy(self, *args, **kwargs):
		return self._PlpOptions.get_IncludeEnergy(*args, **kwargs)
 
	def get_lifter_size(self, *args, **kwargs):
		return self._PlpOptions.get_LifterSize(*args, **kwargs)
 
	def get_log_energy_floor(self, *args, **kwargs):
		return self._PlpOptions.get_LogEnergyFloor(*args, **kwargs)
 
	def get_log_floor(self, *args, **kwargs):
		return self._PlpOptions.get_LogFloor(*args, **kwargs)
 
	def get_low_frequency(self, *args, **kwargs):
		return self._PlpOptions.get_LowFrequency(*args, **kwargs)
 
	def get_lpc_order(self, *args, **kwargs):
		return self._PlpOptions.get_LpcOrder(*args, **kwargs)
 
	def get_non_linearity(self, *args, **kwargs):
		return self._PlpOptions.get_NonLinearity(*args, **kwargs)
 
	def get_pre_emphasis(self, *args, **kwargs):
		return self._PlpOptions.get_PreEmphasis(*args, **kwargs)
 
	def get_rasta(self, *args, **kwargs):
		return self._PlpOptions.get_Rasta(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._PlpOptions.get_SamplingRate(*args, **kwargs)
 
	def get_spectrum_type(self, *args, **kwargs):
		return self._PlpOptions.get_SpectrumType(*args, **kwargs)
 
	def get_window(self, *args, **kwargs):
		return self._PlpOptions.get_Window(*args, **kwargs)
 
	def set_center_frequencies(self, value):
		return self._PlpOptions.set_CenterFrequencies(value)
 
	def set_feature_count(self, value):
		return self._PlpOptions.set_FeatureCount(value)
 
	def set_fft_size(self, value):
		return self._PlpOptions.set_FftSize(value)
 
	def set_filter_bank(self, value):
		return self._PlpOptions.set_FilterBank(value)
 
	def set_filter_bank_size(self, value):
		return self._PlpOptions.set_FilterBankSize(value)
 
	def set_frame_duration(self, value):
		return self._PlpOptions.set_FrameDuration(value)
 
	def set_frame_size(self, value):
		return self._PlpOptions.set_FrameSize(value)
 
	def set_high_frequency(self, value):
		return self._PlpOptions.set_HighFrequency(value)
 
	def set_hop_duration(self, value):
		return self._PlpOptions.set_HopDuration(value)
 
	def set_hop_size(self, value):
		return self._PlpOptions.set_HopSize(value)
 
	def set_include_energy(self, value):
		return self._PlpOptions.set_IncludeEnergy(value)
 
	def set_lifter_size(self, value):
		return self._PlpOptions.set_LifterSize(value)
 
	def set_log_energy_floor(self, value):
		return self._PlpOptions.set_LogEnergyFloor(value)
 
	def set_log_floor(self, value):
		return self._PlpOptions.set_LogFloor(value)
 
	def set_low_frequency(self, value):
		return self._PlpOptions.set_LowFrequency(value)
 
	def set_lpc_order(self, value):
		return self._PlpOptions.set_LpcOrder(value)
 
	def set_non_linearity(self, value):
		return self._PlpOptions.set_NonLinearity(value)
 
	def set_pre_emphasis(self, value):
		return self._PlpOptions.set_PreEmphasis(value)
 
	def set_rasta(self, value):
		return self._PlpOptions.set_Rasta(value)
 
	def set_sampling_rate(self, value):
		return self._PlpOptions.set_SamplingRate(value)
 
	def set_spectrum_type(self, value):
		return self._PlpOptions.set_SpectrumType(value)
 
	def set_window(self, value):
		return self._PlpOptions.set_Window(value)