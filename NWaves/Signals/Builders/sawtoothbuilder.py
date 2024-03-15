from ...wrapper import NWaves 


 

class SawtoothBuilder:

	def __init__(self, *args, **kwargs):
		self._SawtoothBuilder = NWaves.Signals.Builders.SawtoothBuilder(*args, **kwargs)
		self.Signal = self._SawtoothBuilder.Signal
		self.SamplingRate = self._SawtoothBuilder.SamplingRate
		self.ParameterSetters = self._SawtoothBuilder.ParameterSetters
		self.Length = self._SawtoothBuilder.Length
		self.Duration = self._SawtoothBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._SawtoothBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._SawtoothBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._SawtoothBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._SawtoothBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._SawtoothBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._SawtoothBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._SawtoothBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._SawtoothBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._SawtoothBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._SawtoothBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._SawtoothBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._SawtoothBuilder.OfLength(sampleCount)
 
	def overloads(self, *args, **kwargs):
		return self._SawtoothBuilder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._SawtoothBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._SawtoothBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._SawtoothBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._SawtoothBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._SawtoothBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._SawtoothBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._SawtoothBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._SawtoothBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._SawtoothBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._SawtoothBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._SawtoothBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._SawtoothBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._SawtoothBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._SawtoothBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._SawtoothBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._SawtoothBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._SawtoothBuilder.set_Signal(value)