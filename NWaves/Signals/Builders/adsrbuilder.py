from ...wrapper import NWaves 


 

class AdsrBuilder:

	def __init__(self, attack, decay, sustain, release):
		self._AdsrBuilder = NWaves.Signals.Builders.AdsrBuilder(attack, decay, sustain, release)
		self.State = self._AdsrBuilder.State
		self.Signal = self._AdsrBuilder.Signal
		self.SamplingRate = self._AdsrBuilder.SamplingRate
		self.ParameterSetters = self._AdsrBuilder.ParameterSetters
		self.Length = self._AdsrBuilder.Length
		self.Duration = self._AdsrBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._AdsrBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._AdsrBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._AdsrBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._AdsrBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._AdsrBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._AdsrBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._AdsrBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._AdsrBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._AdsrBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._AdsrBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._AdsrBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._AdsrBuilder.OfLength(sampleCount)
 
	def overloads(self, attack, decay, sustain, release):
		return self._AdsrBuilder.Overloads(attack, decay, sustain, release)
 
	def reference_equals(self, objA, objB):
		return self._AdsrBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._AdsrBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._AdsrBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._AdsrBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._AdsrBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._AdsrBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._AdsrBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._AdsrBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._AdsrBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._AdsrBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._AdsrBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._AdsrBuilder.get_Signal(*args, **kwargs)
 
	def get_state(self, *args, **kwargs):
		return self._AdsrBuilder.get_State(*args, **kwargs)
 
	def set_duration(self, value):
		return self._AdsrBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._AdsrBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._AdsrBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._AdsrBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._AdsrBuilder.set_Signal(value)