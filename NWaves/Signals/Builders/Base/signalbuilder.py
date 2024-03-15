from ....wrapper import NWaves 


 

class SignalBuilder:

	def __init__(self, *args, **kwargs):
		self._SignalBuilder = NWaves.Signals.Builders.Base.SignalBuilder(*args, **kwargs)
		self.Signal = self._SignalBuilder.Signal
		self.SamplingRate = self._SignalBuilder.SamplingRate
		self.ParameterSetters = self._SignalBuilder.ParameterSetters
		self.Length = self._SignalBuilder.Length
		self.Duration = self._SignalBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._SignalBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._SignalBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._SignalBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._SignalBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._SignalBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._SignalBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._SignalBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._SignalBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._SignalBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._SignalBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._SignalBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._SignalBuilder.OfLength(sampleCount)
 
	def overloads(self, *args, **kwargs):
		return self._SignalBuilder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._SignalBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._SignalBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._SignalBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._SignalBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._SignalBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._SignalBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._SignalBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._SignalBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._SignalBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._SignalBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._SignalBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._SignalBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._SignalBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._SignalBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._SignalBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._SignalBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._SignalBuilder.set_Signal(value)