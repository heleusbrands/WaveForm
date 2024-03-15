from .wrapper import RubberBand 


 

class RubberBandStretcher:

	def __init__(self, sampleRate: int, channels: int, options=RubberBand.Options, initialTimeRatio=1.0, initialPitchScale=1.0):
		self._RubberBandStretcher = RubberBand.RubberBandStretcher(sampleRate, channels, options, initialTimeRatio, initialPitchScale)
 
	def available(self, *args, **kwargs):
		return self._RubberBandStretcher.Available(*args, **kwargs)
 
	def calculate_stretch(self, *args, **kwargs):
		return self._RubberBandStretcher.CalculateStretch(*args, **kwargs)
 
	def dispose(self, *args, **kwargs):
		return self._RubberBandStretcher.Dispose(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._RubberBandStretcher.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._RubberBandStretcher.Finalize(*args, **kwargs)
 
	def get_channel_count(self, *args, **kwargs):
		return self._RubberBandStretcher.GetChannelCount(*args, **kwargs)
 
	def get_exact_time_points(self, *args, **kwargs):
		return self._RubberBandStretcher.GetExactTimePoints(*args, **kwargs)
 
	def get_frequency_cutoff(self, n):
		return self._RubberBandStretcher.GetFrequencyCutoff(n)
 
	def get_hash_code(self, *args, **kwargs):
		return self._RubberBandStretcher.GetHashCode(*args, **kwargs)
 
	def get_input_increment(self, *args, **kwargs):
		return self._RubberBandStretcher.GetInputIncrement(*args, **kwargs)
 
	def get_latency(self, *args, **kwargs):
		return self._RubberBandStretcher.GetLatency(*args, **kwargs)
 
	def get_output_increments(self, *args, **kwargs):
		return self._RubberBandStretcher.GetOutputIncrements(*args, **kwargs)
 
	def get_phase_reset_curve(self, *args, **kwargs):
		return self._RubberBandStretcher.GetPhaseResetCurve(*args, **kwargs)
 
	def get_pitch_scale(self, *args, **kwargs):
		return self._RubberBandStretcher.GetPitchScale(*args, **kwargs)
 
	def get_samples_required(self, *args, **kwargs):
		return self._RubberBandStretcher.GetSamplesRequired(*args, **kwargs)
 
	def get_time_ratio(self, *args, **kwargs):
		return self._RubberBandStretcher.GetTimeRatio(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._RubberBandStretcher.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._RubberBandStretcher.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, s: int, c: int, options=RubberBand.Options, initialTimeRatio=1.0, initialPitchScale=1.0):
		return self._RubberBandStretcher.Overloads(sampleRate, channels, options, initialTimeRatio, initialPitchScale)
 
	def process(self, *args, **kwargs):
		return self._RubberBandStretcher.Process(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._RubberBandStretcher.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._RubberBandStretcher.Reset(*args, **kwargs)
 
	def retrieve(self, output, samples):
		return self._RubberBandStretcher.Retrieve(output, samples)
 
	def set_debug_level(self, level):
		return self._RubberBandStretcher.SetDebugLevel(level)
 
	def set_default_debug_level(self, level):
		return self._RubberBandStretcher.SetDefaultDebugLevel(level)
 
	def set_detector_option(self, options):
		return self._RubberBandStretcher.SetDetectorOption(options)
 
	def set_expected_input_duration(self, samples):
		return self._RubberBandStretcher.SetExpectedInputDuration(samples)
 
	def set_formant_option(self, options):
		return self._RubberBandStretcher.SetFormantOption(options)
 
	def set_frequency_cutoff(self, n, f):
		return self._RubberBandStretcher.SetFrequencyCutoff(n, f)
 
	def set_key_frame_map(self, map):
		return self._RubberBandStretcher.SetKeyFrameMap(map)
 
	def set_max_process_size(self, samples):
		return self._RubberBandStretcher.SetMaxProcessSize(samples)
 
	def set_phase_option(self, options):
		return self._RubberBandStretcher.SetPhaseOption(options)
 
	def set_pitch_option(self, options):
		return self._RubberBandStretcher.SetPitchOption(options)
 
	def set_pitch_scale(self, scale):
		return self._RubberBandStretcher.SetPitchScale(scale)
 
	def set_time_ratio(self, ratio):
		return self._RubberBandStretcher.SetTimeRatio(ratio)
 
	def set_transients_option(self, options):
		return self._RubberBandStretcher.SetTransientsOption(options)
 
	def study(self, *args, **kwargs):
		return self._RubberBandStretcher.Study(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._RubberBandStretcher.ToString(*args, **kwargs)