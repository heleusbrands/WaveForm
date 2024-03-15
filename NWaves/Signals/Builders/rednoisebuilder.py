from ...wrapper import NWaves 


 

class RedNoiseBuilder:

	def __init__(self, *args, **kwargs):
		self._RedNoiseBuilder = NWaves.Signals.Builders.RedNoiseBuilder(*args, **kwargs)
		self.Signal = self._RedNoiseBuilder.Signal
		self.SamplingRate = self._RedNoiseBuilder.SamplingRate
		self.ParameterSetters = self._RedNoiseBuilder.ParameterSetters
		self.Length = self._RedNoiseBuilder.Length
		self.Duration = self._RedNoiseBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._RedNoiseBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._RedNoiseBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._RedNoiseBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._RedNoiseBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._RedNoiseBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._RedNoiseBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._RedNoiseBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._RedNoiseBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._RedNoiseBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._RedNoiseBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._RedNoiseBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._RedNoiseBuilder.OfLength(sampleCount)
 
	def overloads(self, *args, **kwargs):
		return self._RedNoiseBuilder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._RedNoiseBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._RedNoiseBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._RedNoiseBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._RedNoiseBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._RedNoiseBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._RedNoiseBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._RedNoiseBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._RedNoiseBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._RedNoiseBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._RedNoiseBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._RedNoiseBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._RedNoiseBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._RedNoiseBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._RedNoiseBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._RedNoiseBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._RedNoiseBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._RedNoiseBuilder.set_Signal(value)