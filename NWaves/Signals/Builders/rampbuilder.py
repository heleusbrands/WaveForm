from ...wrapper import NWaves 


 

class RampBuilder:

	def __init__(self, *args, **kwargs):
		self._RampBuilder = NWaves.Signals.Builders.RampBuilder(*args, **kwargs)
		self.Signal = self._RampBuilder.Signal
		self.SamplingRate = self._RampBuilder.SamplingRate
		self.ParameterSetters = self._RampBuilder.ParameterSetters
		self.Length = self._RampBuilder.Length
		self.Duration = self._RampBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._RampBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._RampBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._RampBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._RampBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._RampBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._RampBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._RampBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._RampBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._RampBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._RampBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._RampBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._RampBuilder.OfLength(sampleCount)
 
	def overloads(self, *args, **kwargs):
		return self._RampBuilder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._RampBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._RampBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._RampBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._RampBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._RampBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._RampBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._RampBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._RampBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._RampBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._RampBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._RampBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._RampBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._RampBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._RampBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._RampBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._RampBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._RampBuilder.set_Signal(value)