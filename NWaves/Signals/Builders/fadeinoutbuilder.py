from ...wrapper import NWaves 


 

class FadeInOutBuilder:

	def __init__(self, builder):
		self._FadeInOutBuilder = NWaves.Signals.Builders.FadeInOutBuilder(builder)
		self.Signal = self._FadeInOutBuilder.Signal
		self.SamplingRate = self._FadeInOutBuilder.SamplingRate
		self.ParameterSetters = self._FadeInOutBuilder.ParameterSetters
		self.Length = self._FadeInOutBuilder.Length
		self.FadeStarted = self._FadeInOutBuilder.FadeStarted
		self.FadeFinished = self._FadeInOutBuilder.FadeFinished
		self.Duration = self._FadeInOutBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._FadeInOutBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._FadeInOutBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._FadeInOutBuilder.Equals(*args, **kwargs)
 
	def fade_out(self, *args, **kwargs):
		return self._FadeInOutBuilder.FadeOut(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._FadeInOutBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._FadeInOutBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._FadeInOutBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._FadeInOutBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._FadeInOutBuilder.GetType(*args, **kwargs)
 
	def in(self, seconds):
		return self._FadeInOutBuilder.In(seconds)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._FadeInOutBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._FadeInOutBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._FadeInOutBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._FadeInOutBuilder.OfLength(sampleCount)
 
	def out(self, seconds):
		return self._FadeInOutBuilder.Out(seconds)
 
	def overloads(self, builder):
		return self._FadeInOutBuilder.Overloads(builder)
 
	def reference_equals(self, objA, objB):
		return self._FadeInOutBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._FadeInOutBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._FadeInOutBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._FadeInOutBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._FadeInOutBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._FadeInOutBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._FadeInOutBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._FadeInOutBuilder.get_Duration(*args, **kwargs)
 
	def get_fade_finished(self, *args, **kwargs):
		return self._FadeInOutBuilder.get_FadeFinished(*args, **kwargs)
 
	def get_fade_started(self, *args, **kwargs):
		return self._FadeInOutBuilder.get_FadeStarted(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._FadeInOutBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._FadeInOutBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._FadeInOutBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._FadeInOutBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._FadeInOutBuilder.set_Duration(value)
 
	def set_fade_started(self, value):
		return self._FadeInOutBuilder.set_FadeStarted(value)
 
	def set_length(self, value):
		return self._FadeInOutBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._FadeInOutBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._FadeInOutBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._FadeInOutBuilder.set_Signal(value)