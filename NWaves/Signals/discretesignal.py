from ..wrapper import NWaves 


 

class DiscreteSignal:

	def __init__(self, *args, **kwargs):
		self._DiscreteSignal = NWaves.Signals.DiscreteSignal(*args, **kwargs)
		self.SamplingRate = self._DiscreteSignal.SamplingRate
		self.Samples = self._DiscreteSignal.Samples
		self.Length = self._DiscreteSignal.Length
		self.Duration = self._DiscreteSignal.Duration
 
	def constant(self, constant, l: int, samplingRate: int=1):
		return self._DiscreteSignal.Constant(constant, length, samplingRate)
 
	def copy(self, *args, **kwargs):
		return self._DiscreteSignal.Copy(*args, **kwargs)
 
	def energy(self, startPos, endPos):
		return self._DiscreteSignal.Energy(startPos, endPos)
 
	def entropy(self, *args, **kwargs):
		return self._DiscreteSignal.Entropy(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._DiscreteSignal.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._DiscreteSignal.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._DiscreteSignal.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._DiscreteSignal.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._DiscreteSignal.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._DiscreteSignal.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._DiscreteSignal.ReferenceEquals(objA, objB)
 
	def rms(self, startPos, endPos):
		return self._DiscreteSignal.Rms(startPos, endPos)
 
	def to_string(self, *args, **kwargs):
		return self._DiscreteSignal.ToString(*args, **kwargs)
 
	def unit(self, l: int, samplingRate: int=1):
		return self._DiscreteSignal.Unit(length, samplingRate)
 
	def zero_crossing_rate(self, startPos, endPos):
		return self._DiscreteSignal.ZeroCrossingRate(startPos, endPos)
 
	def get_duration(self, *args, **kwargs):
		return self._DiscreteSignal.get_Duration(*args, **kwargs)
 
	def get_item(self, *args, **kwargs):
		return self._DiscreteSignal.get_Item(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._DiscreteSignal.get_Length(*args, **kwargs)
 
	def get_samples(self, *args, **kwargs):
		return self._DiscreteSignal.get_Samples(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._DiscreteSignal.get_SamplingRate(*args, **kwargs)
 
	def op_addition(self, *args, **kwargs):
		return self._DiscreteSignal.op_Addition(*args, **kwargs)
 
	def op_multiply(self, s, coeff):
		return self._DiscreteSignal.op_Multiply(s, coeff)
 
	def op_subtraction(self, *args, **kwargs):
		return self._DiscreteSignal.op_Subtraction(*args, **kwargs)
 
	def op_unary_negation(self, s):
		return self._DiscreteSignal.op_UnaryNegation(s)
 
	def set_item(self, index, value):
		return self._DiscreteSignal.set_Item(index, value)