from ...wrapper import NWaves 


 

class PnccOptions:

	def __init__(self, *args, **kwargs):
		self._PnccOptions = NWaves.FeatureExtractors.Options.PnccOptions(*args, **kwargs)
		self.Window = self._PnccOptions.Window
		self.SpectrumType = self._PnccOptions.SpectrumType
		self.SamplingRate = self._PnccOptions.SamplingRate
		self.PreEmphasis = self._PnccOptions.PreEmphasis
		self.Power = self._PnccOptions.Power
		self.NonLinearity = self._PnccOptions.NonLinearity
		self.LowFrequency = self._PnccOptions.LowFrequency
		self.LogFloor = self._PnccOptions.LogFloor
		self.LogEnergyFloor = self._PnccOptions.LogEnergyFloor
		self.IncludeEnergy = self._PnccOptions.IncludeEnergy
		self.HopSize = self._PnccOptions.HopSize
		self.HopDuration = self._PnccOptions.HopDuration
		self.HighFrequency = self._PnccOptions.HighFrequency
		self.FrameSize = self._PnccOptions.FrameSize
		self.FrameDuration = self._PnccOptions.FrameDuration
		self.FilterBankSize = self._PnccOptions.FilterBankSize
		self.FilterBank = self._PnccOptions.FilterBank
		self.FftSize = self._PnccOptions.FftSize
		self.FeatureCount = self._PnccOptions.FeatureCount
		self.Errors = self._PnccOptions.Errors
 
	def equals(self, *args, **kwargs):
		return self._PnccOptions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._PnccOptions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._PnccOptions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._PnccOptions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._PnccOptions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PnccOptions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._PnccOptions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._PnccOptions.ToString(*args, **kwargs)
 
	def get_errors(self, *args, **kwargs):
		return self._PnccOptions.get_Errors(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._PnccOptions.get_FeatureCount(*args, **kwargs)
 
	def get_fft_size(self, *args, **kwargs):
		return self._PnccOptions.get_FftSize(*args, **kwargs)
 
	def get_filter_bank(self, *args, **kwargs):
		return self._PnccOptions.get_FilterBank(*args, **kwargs)
 
	def get_filter_bank_size(self, *args, **kwargs):
		return self._PnccOptions.get_FilterBankSize(*args, **kwargs)
 
	def get_frame_duration(self, *args, **kwargs):
		return self._PnccOptions.get_FrameDuration(*args, **kwargs)
 
	def get_frame_size(self, *args, **kwargs):
		return self._PnccOptions.get_FrameSize(*args, **kwargs)
 
	def get_high_frequency(self, *args, **kwargs):
		return self._PnccOptions.get_HighFrequency(*args, **kwargs)
 
	def get_hop_duration(self, *args, **kwargs):
		return self._PnccOptions.get_HopDuration(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._PnccOptions.get_HopSize(*args, **kwargs)
 
	def get_include_energy(self, *args, **kwargs):
		return self._PnccOptions.get_IncludeEnergy(*args, **kwargs)
 
	def get_log_energy_floor(self, *args, **kwargs):
		return self._PnccOptions.get_LogEnergyFloor(*args, **kwargs)
 
	def get_log_floor(self, *args, **kwargs):
		return self._PnccOptions.get_LogFloor(*args, **kwargs)
 
	def get_low_frequency(self, *args, **kwargs):
		return self._PnccOptions.get_LowFrequency(*args, **kwargs)
 
	def get_non_linearity(self, *args, **kwargs):
		return self._PnccOptions.get_NonLinearity(*args, **kwargs)
 
	def get_power(self, *args, **kwargs):
		return self._PnccOptions.get_Power(*args, **kwargs)
 
	def get_pre_emphasis(self, *args, **kwargs):
		return self._PnccOptions.get_PreEmphasis(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._PnccOptions.get_SamplingRate(*args, **kwargs)
 
	def get_spectrum_type(self, *args, **kwargs):
		return self._PnccOptions.get_SpectrumType(*args, **kwargs)
 
	def get_window(self, *args, **kwargs):
		return self._PnccOptions.get_Window(*args, **kwargs)
 
	def set_feature_count(self, value):
		return self._PnccOptions.set_FeatureCount(value)
 
	def set_fft_size(self, value):
		return self._PnccOptions.set_FftSize(value)
 
	def set_filter_bank(self, value):
		return self._PnccOptions.set_FilterBank(value)
 
	def set_filter_bank_size(self, value):
		return self._PnccOptions.set_FilterBankSize(value)
 
	def set_frame_duration(self, value):
		return self._PnccOptions.set_FrameDuration(value)
 
	def set_frame_size(self, value):
		return self._PnccOptions.set_FrameSize(value)
 
	def set_high_frequency(self, value):
		return self._PnccOptions.set_HighFrequency(value)
 
	def set_hop_duration(self, value):
		return self._PnccOptions.set_HopDuration(value)
 
	def set_hop_size(self, value):
		return self._PnccOptions.set_HopSize(value)
 
	def set_include_energy(self, value):
		return self._PnccOptions.set_IncludeEnergy(value)
 
	def set_log_energy_floor(self, value):
		return self._PnccOptions.set_LogEnergyFloor(value)
 
	def set_log_floor(self, value):
		return self._PnccOptions.set_LogFloor(value)
 
	def set_low_frequency(self, value):
		return self._PnccOptions.set_LowFrequency(value)
 
	def set_non_linearity(self, value):
		return self._PnccOptions.set_NonLinearity(value)
 
	def set_power(self, value):
		return self._PnccOptions.set_Power(value)
 
	def set_pre_emphasis(self, value):
		return self._PnccOptions.set_PreEmphasis(value)
 
	def set_sampling_rate(self, value):
		return self._PnccOptions.set_SamplingRate(value)
 
	def set_spectrum_type(self, value):
		return self._PnccOptions.set_SpectrumType(value)
 
	def set_window(self, value):
		return self._PnccOptions.set_Window(value)