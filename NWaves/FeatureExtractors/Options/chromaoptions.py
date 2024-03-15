from ...wrapper import NWaves 


 

class ChromaOptions:

	def __init__(self, *args, **kwargs):
		self._ChromaOptions = NWaves.FeatureExtractors.Options.ChromaOptions(*args, **kwargs)
		self.Window = self._ChromaOptions.Window
		self.Tuning = self._ChromaOptions.Tuning
		self.SamplingRate = self._ChromaOptions.SamplingRate
		self.PreEmphasis = self._ChromaOptions.PreEmphasis
		self.OctaveWidth = self._ChromaOptions.OctaveWidth
		self.Norm = self._ChromaOptions.Norm
		self.HopSize = self._ChromaOptions.HopSize
		self.HopDuration = self._ChromaOptions.HopDuration
		self.FrameSize = self._ChromaOptions.FrameSize
		self.FrameDuration = self._ChromaOptions.FrameDuration
		self.FftSize = self._ChromaOptions.FftSize
		self.FeatureCount = self._ChromaOptions.FeatureCount
		self.Errors = self._ChromaOptions.Errors
		self.CenterOctave = self._ChromaOptions.CenterOctave
		self.BaseC = self._ChromaOptions.BaseC
 
	def equals(self, *args, **kwargs):
		return self._ChromaOptions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._ChromaOptions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._ChromaOptions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._ChromaOptions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._ChromaOptions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._ChromaOptions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._ChromaOptions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._ChromaOptions.ToString(*args, **kwargs)
 
	def get_base_c(self, *args, **kwargs):
		return self._ChromaOptions.get_BaseC(*args, **kwargs)
 
	def get_center_octave(self, *args, **kwargs):
		return self._ChromaOptions.get_CenterOctave(*args, **kwargs)
 
	def get_errors(self, *args, **kwargs):
		return self._ChromaOptions.get_Errors(*args, **kwargs)
 
	def get_feature_count(self, *args, **kwargs):
		return self._ChromaOptions.get_FeatureCount(*args, **kwargs)
 
	def get_fft_size(self, *args, **kwargs):
		return self._ChromaOptions.get_FftSize(*args, **kwargs)
 
	def get_frame_duration(self, *args, **kwargs):
		return self._ChromaOptions.get_FrameDuration(*args, **kwargs)
 
	def get_frame_size(self, *args, **kwargs):
		return self._ChromaOptions.get_FrameSize(*args, **kwargs)
 
	def get_hop_duration(self, *args, **kwargs):
		return self._ChromaOptions.get_HopDuration(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._ChromaOptions.get_HopSize(*args, **kwargs)
 
	def get_norm(self, *args, **kwargs):
		return self._ChromaOptions.get_Norm(*args, **kwargs)
 
	def get_octave_width(self, *args, **kwargs):
		return self._ChromaOptions.get_OctaveWidth(*args, **kwargs)
 
	def get_pre_emphasis(self, *args, **kwargs):
		return self._ChromaOptions.get_PreEmphasis(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._ChromaOptions.get_SamplingRate(*args, **kwargs)
 
	def get_tuning(self, *args, **kwargs):
		return self._ChromaOptions.get_Tuning(*args, **kwargs)
 
	def get_window(self, *args, **kwargs):
		return self._ChromaOptions.get_Window(*args, **kwargs)
 
	def set_base_c(self, value):
		return self._ChromaOptions.set_BaseC(value)
 
	def set_center_octave(self, value):
		return self._ChromaOptions.set_CenterOctave(value)
 
	def set_feature_count(self, value):
		return self._ChromaOptions.set_FeatureCount(value)
 
	def set_fft_size(self, value):
		return self._ChromaOptions.set_FftSize(value)
 
	def set_frame_duration(self, value):
		return self._ChromaOptions.set_FrameDuration(value)
 
	def set_frame_size(self, value):
		return self._ChromaOptions.set_FrameSize(value)
 
	def set_hop_duration(self, value):
		return self._ChromaOptions.set_HopDuration(value)
 
	def set_hop_size(self, value):
		return self._ChromaOptions.set_HopSize(value)
 
	def set_norm(self, value):
		return self._ChromaOptions.set_Norm(value)
 
	def set_octave_width(self, value):
		return self._ChromaOptions.set_OctaveWidth(value)
 
	def set_pre_emphasis(self, value):
		return self._ChromaOptions.set_PreEmphasis(value)
 
	def set_sampling_rate(self, value):
		return self._ChromaOptions.set_SamplingRate(value)
 
	def set_tuning(self, value):
		return self._ChromaOptions.set_Tuning(value)
 
	def set_window(self, value):
		return self._ChromaOptions.set_Window(value)