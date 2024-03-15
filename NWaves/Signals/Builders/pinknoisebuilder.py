from ...wrapper import NWaves 


 

class PinkNoiseBuilder:

	def __init__(self, *args, **kwargs):
		self._PinkNoiseBuilder = NWaves.Signals.Builders.PinkNoiseBuilder(*args, **kwargs)
		self.Signal = self._PinkNoiseBuilder.Signal
		self.SamplingRate = self._PinkNoiseBuilder.SamplingRate
		self.ParameterSetters = self._PinkNoiseBuilder.ParameterSetters
		self.Length = self._PinkNoiseBuilder.Length
		self.Duration = self._PinkNoiseBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._PinkNoiseBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._PinkNoiseBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._PinkNoiseBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._PinkNoiseBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._PinkNoiseBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._PinkNoiseBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._PinkNoiseBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._PinkNoiseBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._PinkNoiseBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._PinkNoiseBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._PinkNoiseBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._PinkNoiseBuilder.OfLength(sampleCount)
 
	def overloads(self, *args, **kwargs):
		return self._PinkNoiseBuilder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._PinkNoiseBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._PinkNoiseBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._PinkNoiseBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._PinkNoiseBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._PinkNoiseBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._PinkNoiseBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._PinkNoiseBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._PinkNoiseBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._PinkNoiseBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._PinkNoiseBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._PinkNoiseBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._PinkNoiseBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._PinkNoiseBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._PinkNoiseBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._PinkNoiseBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._PinkNoiseBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._PinkNoiseBuilder.set_Signal(value)