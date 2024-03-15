from ...wrapper import NWaves 


 

class SincBuilder:

	def __init__(self, *args, **kwargs):
		self._SincBuilder = NWaves.Signals.Builders.SincBuilder(*args, **kwargs)
		self.Signal = self._SincBuilder.Signal
		self.SamplingRate = self._SincBuilder.SamplingRate
		self.ParameterSetters = self._SincBuilder.ParameterSetters
		self.Length = self._SincBuilder.Length
		self.Duration = self._SincBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._SincBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._SincBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._SincBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._SincBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._SincBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._SincBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._SincBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._SincBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._SincBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._SincBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._SincBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._SincBuilder.OfLength(sampleCount)
 
	def overloads(self, *args, **kwargs):
		return self._SincBuilder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._SincBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._SincBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._SincBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._SincBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._SincBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._SincBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._SincBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._SincBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._SincBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._SincBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._SincBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._SincBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._SincBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._SincBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._SincBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._SincBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._SincBuilder.set_Signal(value)