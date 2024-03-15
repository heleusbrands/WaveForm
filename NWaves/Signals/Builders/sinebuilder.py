from ...wrapper import NWaves 


 

class SineBuilder:

	def __init__(self, *args, **kwargs):
		self._SineBuilder = NWaves.Signals.Builders.SineBuilder(*args, **kwargs)
		self.Signal = self._SineBuilder.Signal
		self.SamplingRate = self._SineBuilder.SamplingRate
		self.ParameterSetters = self._SineBuilder.ParameterSetters
		self.Length = self._SineBuilder.Length
		self.Duration = self._SineBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._SineBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._SineBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._SineBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._SineBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._SineBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._SineBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._SineBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._SineBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._SineBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._SineBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._SineBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._SineBuilder.OfLength(sampleCount)
 
	def overloads(self, *args, **kwargs):
		return self._SineBuilder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._SineBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._SineBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._SineBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._SineBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._SineBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._SineBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._SineBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._SineBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._SineBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._SineBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._SineBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._SineBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._SineBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._SineBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._SineBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._SineBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._SineBuilder.set_Signal(value)