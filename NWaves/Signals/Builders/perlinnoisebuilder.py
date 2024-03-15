from ...wrapper import NWaves 


 

class PerlinNoiseBuilder:

	def __init__(self, *args, **kwargs):
		self._PerlinNoiseBuilder = NWaves.Signals.Builders.PerlinNoiseBuilder(*args, **kwargs)
		self.Signal = self._PerlinNoiseBuilder.Signal
		self.SamplingRate = self._PerlinNoiseBuilder.SamplingRate
		self.ParameterSetters = self._PerlinNoiseBuilder.ParameterSetters
		self.Length = self._PerlinNoiseBuilder.Length
		self.Duration = self._PerlinNoiseBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._PerlinNoiseBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._PerlinNoiseBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._PerlinNoiseBuilder.OfLength(sampleCount)
 
	def overloads(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._PerlinNoiseBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._PerlinNoiseBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._PerlinNoiseBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._PerlinNoiseBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._PerlinNoiseBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._PerlinNoiseBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._PerlinNoiseBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._PerlinNoiseBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._PerlinNoiseBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._PerlinNoiseBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._PerlinNoiseBuilder.set_Signal(value)