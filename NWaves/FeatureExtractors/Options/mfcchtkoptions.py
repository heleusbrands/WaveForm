from ...wrapper import NWaves 


 

class MfccHtkOptions:

	def __init__(self, s: int, f: int, f: float, lowFrequency=0.0, highFrequency=0.0, filterbankSize: int=24, fftSize: int=0):
		self._MfccHtkOptions = NWaves.FeatureExtractors.Options.MfccHtkOptions(samplingRate, featureCount, frameDuration, lowFrequency, highFrequency, filterbankSize, fftSize)
		self.Window = self._MfccHtkOptions.Window
		self.SpectrumType = self._MfccHtkOptions.SpectrumType
		self.SamplingRate = self._MfccHtkOptions.SamplingRate
		self.PreEmphasis = self._MfccHtkOptions.PreEmphasis
		self.NonLinearity = self._MfccHtkOptions.NonLinearity
		self.LowFrequency = self._MfccHtkOptions.LowFrequency
		self.LogFloor = self._MfccHtkOptions.LogFloor
		self.LogEnergyFloor = self._MfccHtkOptions.LogEnergyFloor
		self.LifterSize = self._MfccHtkOptions.LifterSize
		self.IncludeEnergy = self._MfccHtkOptions.IncludeEnergy
		self.HopSize = self._MfccHtkOptions.HopSize
		self.HopDuration = self._MfccHtkOptions.HopDuration
		self.HighFrequency = self._MfccHtkOptions.HighFrequency
		self.FrameSize = self._MfccHtkOptions.FrameSize
		self.FrameDuration = self._MfccHtkOptions.FrameDuration
		self.FilterBankSize = self._MfccHtkOptions.FilterBankSize
		self.FilterBank = self._MfccHtkOptions.FilterBank
		self.FftSize = self._MfccHtkOptions.FftSize
		self.FeatureCount = self._MfccHtkOptions.FeatureCount
		self.Errors = self._MfccHtkOptions.Errors
		self.DctType = self._MfccHtkOptions.DctType
 
	def equals(self, *args, **kwargs):
		return self._MfccHtkOptions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._MfccHtkOptions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._MfccHtkOptions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._MfccHtkOptions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._MfccHtkOptions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, s: int, f: int, f: float, lowFrequency=0.0, highFrequency=0.0, filterbankSize: int=24, fftSize: int=0):
		return self._MfccHtkOptions.Overloads(samplingRate, featureCount, frameDuration, lowFrequency, highFrequency, filterbankSize, fftSize)
 
	def reference_equals(self, objA, objB):
		return self._MfccHtkOptions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._MfccHtkOptions.ToString(*args, **kwargs)
 
	def get_dct_type(self, *args, **kwargs):
		return self._MfccHtkOptions.get_DctType(*args, **kwargs)
 
	def get_errors(self, *args, **kwargs):
		return self._MfccHtkOptions.get_Errors(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._MfccHtkOptions.get_FeatureCount(*args, **kwargs)
 
	def get_fft_size(self, *args, **kwargs):
		return self._MfccHtkOptions.get_FftSize(*args, **kwargs)
 
	def get_filter_bank(self, *args, **kwargs):
		return self._MfccHtkOptions.get_FilterBank(*args, **kwargs)
 
	def get_filter_bank_size(self, *args, **kwargs):
		return self._MfccHtkOptions.get_FilterBankSize(*args, **kwargs)
 
	def get_frame_duration(self, *args, **kwargs):
		return self._MfccHtkOptions.get_FrameDuration(*args, **kwargs)
 
	def get_frame_size(self, *args, **kwargs):
		return self._MfccHtkOptions.get_FrameSize(*args, **kwargs)
 
	def get_high_frequency(self, *args, **kwargs):
		return self._MfccHtkOptions.get_HighFrequency(*args, **kwargs)
 
	def get_hop_duration(self, *args, **kwargs):
		return self._MfccHtkOptions.get_HopDuration(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._MfccHtkOptions.get_HopSize(*args, **kwargs)
 
	def get_include_energy(self, *args, **kwargs):
		return self._MfccHtkOptions.get_IncludeEnergy(*args, **kwargs)
 
	def get_lifter_size(self, *args, **kwargs):
		return self._MfccHtkOptions.get_LifterSize(*args, **kwargs)
 
	def get_log_energy_floor(self, *args, **kwargs):
		return self._MfccHtkOptions.get_LogEnergyFloor(*args, **kwargs)
 
	def get_log_floor(self, *args, **kwargs):
		return self._MfccHtkOptions.get_LogFloor(*args, **kwargs)
 
	def get_low_frequency(self, *args, **kwargs):
		return self._MfccHtkOptions.get_LowFrequency(*args, **kwargs)
 
	def get_non_linearity(self, *args, **kwargs):
		return self._MfccHtkOptions.get_NonLinearity(*args, **kwargs)
 
	def get_pre_emphasis(self, *args, **kwargs):
		return self._MfccHtkOptions.get_PreEmphasis(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._MfccHtkOptions.get_SamplingRate(*args, **kwargs)
 
	def get_spectrum_type(self, *args, **kwargs):
		return self._MfccHtkOptions.get_SpectrumType(*args, **kwargs)
 
	def get_window(self, *args, **kwargs):
		return self._MfccHtkOptions.get_Window(*args, **kwargs)
 
	def set_dct_type(self, value):
		return self._MfccHtkOptions.set_DctType(value)
 
	def set_feature_count(self, value):
		return self._MfccHtkOptions.set_FeatureCount(value)
 
	def set_fft_size(self, value):
		return self._MfccHtkOptions.set_FftSize(value)
 
	def set_filter_bank(self, value):
		return self._MfccHtkOptions.set_FilterBank(value)
 
	def set_filter_bank_size(self, value):
		return self._MfccHtkOptions.set_FilterBankSize(value)
 
	def set_frame_duration(self, value):
		return self._MfccHtkOptions.set_FrameDuration(value)
 
	def set_frame_size(self, value):
		return self._MfccHtkOptions.set_FrameSize(value)
 
	def set_high_frequency(self, value):
		return self._MfccHtkOptions.set_HighFrequency(value)
 
	def set_hop_duration(self, value):
		return self._MfccHtkOptions.set_HopDuration(value)
 
	def set_hop_size(self, value):
		return self._MfccHtkOptions.set_HopSize(value)
 
	def set_include_energy(self, value):
		return self._MfccHtkOptions.set_IncludeEnergy(value)
 
	def set_lifter_size(self, value):
		return self._MfccHtkOptions.set_LifterSize(value)
 
	def set_log_energy_floor(self, value):
		return self._MfccHtkOptions.set_LogEnergyFloor(value)
 
	def set_log_floor(self, value):
		return self._MfccHtkOptions.set_LogFloor(value)
 
	def set_low_frequency(self, value):
		return self._MfccHtkOptions.set_LowFrequency(value)
 
	def set_non_linearity(self, value):
		return self._MfccHtkOptions.set_NonLinearity(value)
 
	def set_pre_emphasis(self, value):
		return self._MfccHtkOptions.set_PreEmphasis(value)
 
	def set_sampling_rate(self, value):
		return self._MfccHtkOptions.set_SamplingRate(value)
 
	def set_spectrum_type(self, value):
		return self._MfccHtkOptions.set_SpectrumType(value)
 
	def set_window(self, value):
		return self._MfccHtkOptions.set_Window(value)