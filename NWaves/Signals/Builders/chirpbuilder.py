from ...wrapper import NWaves 


 

class ChirpBuilder:

	def __init__(self, *args, **kwargs):
		self._ChirpBuilder = NWaves.Signals.Builders.ChirpBuilder(*args, **kwargs)
		self.Signal = self._ChirpBuilder.Signal
		self.SamplingRate = self._ChirpBuilder.SamplingRate
		self.ParameterSetters = self._ChirpBuilder.ParameterSetters
		self.Length = self._ChirpBuilder.Length
		self.Duration = self._ChirpBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._ChirpBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._ChirpBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._ChirpBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._ChirpBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._ChirpBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._ChirpBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._ChirpBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._ChirpBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._ChirpBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._ChirpBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._ChirpBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._ChirpBuilder.OfLength(sampleCount)
 
	def overloads(self, *args, **kwargs):
		return self._ChirpBuilder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._ChirpBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._ChirpBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._ChirpBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._ChirpBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._ChirpBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._ChirpBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._ChirpBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._ChirpBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._ChirpBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._ChirpBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._ChirpBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._ChirpBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._ChirpBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._ChirpBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._ChirpBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._ChirpBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._ChirpBuilder.set_Signal(value)