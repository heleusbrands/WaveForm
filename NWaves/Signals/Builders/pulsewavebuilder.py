from ...wrapper import NWaves 


 

class PulseWaveBuilder:

	def __init__(self, *args, **kwargs):
		self._PulseWaveBuilder = NWaves.Signals.Builders.PulseWaveBuilder(*args, **kwargs)
		self.Signal = self._PulseWaveBuilder.Signal
		self.SamplingRate = self._PulseWaveBuilder.SamplingRate
		self.ParameterSetters = self._PulseWaveBuilder.ParameterSetters
		self.Length = self._PulseWaveBuilder.Length
		self.Duration = self._PulseWaveBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._PulseWaveBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._PulseWaveBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._PulseWaveBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._PulseWaveBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._PulseWaveBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._PulseWaveBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._PulseWaveBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._PulseWaveBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._PulseWaveBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._PulseWaveBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._PulseWaveBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._PulseWaveBuilder.OfLength(sampleCount)
 
	def overloads(self, *args, **kwargs):
		return self._PulseWaveBuilder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._PulseWaveBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._PulseWaveBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._PulseWaveBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._PulseWaveBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._PulseWaveBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._PulseWaveBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._PulseWaveBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._PulseWaveBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._PulseWaveBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._PulseWaveBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._PulseWaveBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._PulseWaveBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._PulseWaveBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._PulseWaveBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._PulseWaveBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._PulseWaveBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._PulseWaveBuilder.set_Signal(value)