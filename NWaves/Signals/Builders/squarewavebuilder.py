from ...wrapper import NWaves 


 

class SquareWaveBuilder:

	def __init__(self, *args, **kwargs):
		self._SquareWaveBuilder = NWaves.Signals.Builders.SquareWaveBuilder(*args, **kwargs)
		self.Signal = self._SquareWaveBuilder.Signal
		self.SamplingRate = self._SquareWaveBuilder.SamplingRate
		self.ParameterSetters = self._SquareWaveBuilder.ParameterSetters
		self.Length = self._SquareWaveBuilder.Length
		self.Duration = self._SquareWaveBuilder.Duration
 
	def build(self, *args, **kwargs):
		return self._SquareWaveBuilder.Build(*args, **kwargs)
 
	def delayed_by(self, delay):
		return self._SquareWaveBuilder.DelayedBy(delay)
 
	def equals(self, *args, **kwargs):
		return self._SquareWaveBuilder.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._SquareWaveBuilder.Finalize(*args, **kwargs)
 
	def generate(self, *args, **kwargs):
		return self._SquareWaveBuilder.Generate(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._SquareWaveBuilder.GetHashCode(*args, **kwargs)
 
	def get_parameters_info(self, *args, **kwargs):
		return self._SquareWaveBuilder.GetParametersInfo(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._SquareWaveBuilder.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._SquareWaveBuilder.MemberwiseClone(*args, **kwargs)
 
	def next_sample(self, *args, **kwargs):
		return self._SquareWaveBuilder.NextSample(*args, **kwargs)
 
	def of_duration(self, seconds):
		return self._SquareWaveBuilder.OfDuration(seconds)
 
	def of_length(self, sampleCount):
		return self._SquareWaveBuilder.OfLength(sampleCount)
 
	def overloads(self, *args, **kwargs):
		return self._SquareWaveBuilder.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._SquareWaveBuilder.ReferenceEquals(objA, objB)
 
	def repeated_times(self, times):
		return self._SquareWaveBuilder.RepeatedTimes(times)
 
	def reset(self, *args, **kwargs):
		return self._SquareWaveBuilder.Reset(*args, **kwargs)
 
	def sampled_at(self, samplingRate):
		return self._SquareWaveBuilder.SampledAt(samplingRate)
 
	def set_parameter(self, parameterName, parameterValue):
		return self._SquareWaveBuilder.SetParameter(parameterName, parameterValue)
 
	def superimposed_with(self, signal):
		return self._SquareWaveBuilder.SuperimposedWith(signal)
 
	def to_string(self, *args, **kwargs):
		return self._SquareWaveBuilder.ToString(*args, **kwargs)
 
	def get_duration(self, *args, **kwargs):
		return self._SquareWaveBuilder.get_Duration(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._SquareWaveBuilder.get_Length(*args, **kwargs)
 
	def get_parameter_setters(self, *args, **kwargs):
		return self._SquareWaveBuilder.get_ParameterSetters(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._SquareWaveBuilder.get_SamplingRate(*args, **kwargs)
 
	def get_signal(self, *args, **kwargs):
		return self._SquareWaveBuilder.get_Signal(*args, **kwargs)
 
	def set_duration(self, value):
		return self._SquareWaveBuilder.set_Duration(value)
 
	def set_length(self, value):
		return self._SquareWaveBuilder.set_Length(value)
 
	def set_parameter_setters(self, value):
		return self._SquareWaveBuilder.set_ParameterSetters(value)
 
	def set_sampling_rate(self, value):
		return self._SquareWaveBuilder.set_SamplingRate(value)
 
	def set_signal(self, value):
		return self._SquareWaveBuilder.set_Signal(value)