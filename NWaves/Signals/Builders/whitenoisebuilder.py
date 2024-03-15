from ...wrapper import NWaves 


 

class WhiteNoiseBuilder:

	def __init__(self, *args, **kwargs):
		self._WhiteNoiseBuilder = NWaves.Signals.Builders.WhiteNoiseBuilder(*args, **kwargs)
		self.Signal = self._WhiteNoiseBuilder.Signal
		self.SamplingRate = self._WhiteNoiseBuilder.SamplingRate
		self.ParameterSetters = self._WhiteNoiseBuilder.ParameterSetters
		self.Length = self._WhiteNoiseBuilder.Length
		self.Duration = self._WhiteNoiseBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._WhiteNoiseBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._WhiteNoiseBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._WhiteNoiseBuilder.OfLength(sampleCount)
 
	def overloads(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._WhiteNoiseBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._WhiteNoiseBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._WhiteNoiseBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._WhiteNoiseBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._WhiteNoiseBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._WhiteNoiseBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._WhiteNoiseBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._WhiteNoiseBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._WhiteNoiseBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._WhiteNoiseBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._WhiteNoiseBuilder.set_Signal(value)