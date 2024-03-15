from ...wrapper import NWaves 


 

class TriangleWaveBuilder:

	def __init__(self, *args, **kwargs):
		self._TriangleWaveBuilder = NWaves.Signals.Builders.TriangleWaveBuilder(*args, **kwargs)
		self.Signal = self._TriangleWaveBuilder.Signal
		self.SamplingRate = self._TriangleWaveBuilder.SamplingRate
		self.ParameterSetters = self._TriangleWaveBuilder.ParameterSetters
		self.Length = self._TriangleWaveBuilder.Length
		self.Duration = self._TriangleWaveBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._TriangleWaveBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._TriangleWaveBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._TriangleWaveBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._TriangleWaveBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._TriangleWaveBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._TriangleWaveBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._TriangleWaveBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._TriangleWaveBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._TriangleWaveBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._TriangleWaveBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._TriangleWaveBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._TriangleWaveBuilder.OfLength(sampleCount)
 
	def overloads(self, *args, **kwargs):
		return self._TriangleWaveBuilder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._TriangleWaveBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._TriangleWaveBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._TriangleWaveBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._TriangleWaveBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._TriangleWaveBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._TriangleWaveBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._TriangleWaveBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._TriangleWaveBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._TriangleWaveBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._TriangleWaveBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._TriangleWaveBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._TriangleWaveBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._TriangleWaveBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._TriangleWaveBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._TriangleWaveBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._TriangleWaveBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._TriangleWaveBuilder.set_Signal(value)