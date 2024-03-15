from ...wrapper import NWaves 


 

class CosineBuilder:

	def __init__(self, *args, **kwargs):
		self._CosineBuilder = NWaves.Signals.Builders.CosineBuilder(*args, **kwargs)
		self.Signal = self._CosineBuilder.Signal
		self.SamplingRate = self._CosineBuilder.SamplingRate
		self.ParameterSetters = self._CosineBuilder.ParameterSetters
		self.Length = self._CosineBuilder.Length
		self.Duration = self._CosineBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._CosineBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._CosineBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._CosineBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._CosineBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._CosineBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._CosineBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._CosineBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._CosineBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._CosineBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._CosineBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._CosineBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._CosineBuilder.OfLength(sampleCount)
 
	def overloads(self, *args, **kwargs):
		return self._CosineBuilder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._CosineBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._CosineBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._CosineBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._CosineBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._CosineBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._CosineBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._CosineBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._CosineBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._CosineBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._CosineBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._CosineBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._CosineBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._CosineBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._CosineBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._CosineBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._CosineBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._CosineBuilder.set_Signal(value)