from ...wrapper import NWaves 


 

class AwgnBuilder:

	def __init__(self, *args, **kwargs):
		self._AwgnBuilder = NWaves.Signals.Builders.AwgnBuilder(*args, **kwargs)
		self.Signal = self._AwgnBuilder.Signal
		self.SamplingRate = self._AwgnBuilder.SamplingRate
		self.ParameterSetters = self._AwgnBuilder.ParameterSetters
		self.Length = self._AwgnBuilder.Length
		self.Duration = self._AwgnBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._AwgnBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._AwgnBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._AwgnBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._AwgnBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._AwgnBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._AwgnBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._AwgnBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._AwgnBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._AwgnBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._AwgnBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._AwgnBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._AwgnBuilder.OfLength(sampleCount)
 
	def overloads(self, *args, **kwargs):
		return self._AwgnBuilder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._AwgnBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._AwgnBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._AwgnBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._AwgnBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._AwgnBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._AwgnBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._AwgnBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._AwgnBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._AwgnBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._AwgnBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._AwgnBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._AwgnBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._AwgnBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._AwgnBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._AwgnBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._AwgnBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._AwgnBuilder.set_Signal(value)