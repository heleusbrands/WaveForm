from ...wrapper import NWaves 


 

class MfccSlaneyOptions:

	def __init__(self, s: int, f: int, f: float, lowFrequency=0.0, highFrequency=0.0, filterbankSize: int=40, fftSize: int=0, normalize: bool=True):
		self._MfccSlaneyOptions = NWaves.FeatureExtractors.Options.MfccSlaneyOptions(samplingRate, featureCount, frameDuration, lowFrequency, highFrequency, filterbankSize, fftSize, normalize)
		self.Window = self._MfccSlaneyOptions.Window
		self.SpectrumType = self._MfccSlaneyOptions.SpectrumType
		self.SamplingRate = self._MfccSlaneyOptions.SamplingRate
		self.PreEmphasis = self._MfccSlaneyOptions.PreEmphasis
		self.NonLinearity = self._MfccSlaneyOptions.NonLinearity
		self.LowFrequency = self._MfccSlaneyOptions.LowFrequency
		self.LogFloor = self._MfccSlaneyOptions.LogFloor
		self.LogEnergyFloor = self._MfccSlaneyOptions.LogEnergyFloor
		self.LifterSize = self._MfccSlaneyOptions.LifterSize
		self.IncludeEnergy = self._MfccSlaneyOptions.IncludeEnergy
		self.HopSize = self._MfccSlaneyOptions.HopSize
		self.HopDuration = self._MfccSlaneyOptions.HopDuration
		self.HighFrequency = self._MfccSlaneyOptions.HighFrequency
		self.FrameSize = self._MfccSlaneyOptions.FrameSize
		self.FrameDuration = self._MfccSlaneyOptions.FrameDuration
		self.FilterBankSize = self._MfccSlaneyOptions.FilterBankSize
		self.FilterBank = self._MfccSlaneyOptions.FilterBank
		self.FftSize = self._MfccSlaneyOptions.FftSize
		self.FeatureCount = self._MfccSlaneyOptions.FeatureCount
		self.Errors = self._MfccSlaneyOptions.Errors
		self.DctType = self._MfccSlaneyOptions.DctType
 
	def equals(self, *args, **kwargs):
		return self._MfccSlaneyOptions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._MfccSlaneyOptions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._MfccSlaneyOptions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._MfccSlaneyOptions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._MfccSlaneyOptions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, s: int, f: int, f: float, lowFrequency=0.0, highFrequency=0.0, filterbankSize: int=40, fftSize: int=0, normalize: bool=True):
		return self._MfccSlaneyOptions.Overloads(samplingRate, featureCount, frameDuration, lowFrequency, highFrequency, filterbankSize, fftSize, normalize)
 
	def reference_equals(self, objA, objB):
		return self._MfccSlaneyOptions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._MfccSlaneyOptions.ToString(*args, **kwargs)
 
	def get_dct_type(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_DctType(*args, **kwargs)
 
	def get_errors(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_Errors(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_FeatureCount(*args, **kwargs)
 
	def get_fft_size(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_FftSize(*args, **kwargs)
 
	def get_filter_bank(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_FilterBank(*args, **kwargs)
 
	def get_filter_bank_size(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_FilterBankSize(*args, **kwargs)
 
	def get_frame_duration(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_FrameDuration(*args, **kwargs)
 
	def get_frame_size(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_FrameSize(*args, **kwargs)
 
	def get_high_frequency(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_HighFrequency(*args, **kwargs)
 
	def get_hop_duration(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_HopDuration(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_HopSize(*args, **kwargs)
 
	def get_include_energy(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_IncludeEnergy(*args, **kwargs)
 
	def get_lifter_size(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_LifterSize(*args, **kwargs)
 
	def get_log_energy_floor(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_LogEnergyFloor(*args, **kwargs)
 
	def get_log_floor(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_LogFloor(*args, **kwargs)
 
	def get_low_frequency(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_LowFrequency(*args, **kwargs)
 
	def get_non_linearity(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_NonLinearity(*args, **kwargs)
 
	def get_pre_emphasis(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_PreEmphasis(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_SamplingRate(*args, **kwargs)
 
	def get_spectrum_type(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_SpectrumType(*args, **kwargs)
 
	def get_window(self, *args, **kwargs):
		return self._MfccSlaneyOptions.get_Window(*args, **kwargs)
 
	def set_dct_type(self, value):
		return self._MfccSlaneyOptions.set_DctType(value)
 
	def set_feature_count(self, value):
		return self._MfccSlaneyOptions.set_FeatureCount(value)
 
	def set_fft_size(self, value):
		return self._MfccSlaneyOptions.set_FftSize(value)
 
	def set_filter_bank(self, value):
		return self._MfccSlaneyOptions.set_FilterBank(value)
 
	def set_filter_bank_size(self, value):
		return self._MfccSlaneyOptions.set_FilterBankSize(value)
 
	def set_frame_duration(self, value):
		return self._MfccSlaneyOptions.set_FrameDuration(value)
 
	def set_frame_size(self, value):
		return self._MfccSlaneyOptions.set_FrameSize(value)
 
	def set_high_frequency(self, value):
		return self._MfccSlaneyOptions.set_HighFrequency(value)
 
	def set_hop_duration(self, value):
		return self._MfccSlaneyOptions.set_HopDuration(value)
 
	def set_hop_size(self, value):
		return self._MfccSlaneyOptions.set_HopSize(value)
 
	def set_include_energy(self, value):
		return self._MfccSlaneyOptions.set_IncludeEnergy(value)
 
	def set_lifter_size(self, value):
		return self._MfccSlaneyOptions.set_LifterSize(value)
 
	def set_log_energy_floor(self, value):
		return self._MfccSlaneyOptions.set_LogEnergyFloor(value)
 
	def set_log_floor(self, value):
		return self._MfccSlaneyOptions.set_LogFloor(value)
 
	def set_low_frequency(self, value):
		return self._MfccSlaneyOptions.set_LowFrequency(value)
 
	def set_non_linearity(self, value):
		return self._MfccSlaneyOptions.set_NonLinearity(value)
 
	def set_pre_emphasis(self, value):
		return self._MfccSlaneyOptions.set_PreEmphasis(value)
 
	def set_sampling_rate(self, value):
		return self._MfccSlaneyOptions.set_SamplingRate(value)
 
	def set_spectrum_type(self, value):
		return self._MfccSlaneyOptions.set_SpectrumType(value)
 
	def set_window(self, value):
		return self._MfccSlaneyOptions.set_Window(value)