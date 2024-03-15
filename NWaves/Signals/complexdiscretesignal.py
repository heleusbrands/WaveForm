from ..wrapper import NWaves 


 

class ComplexDiscreteSignal:

	def __init__(self, *args, **kwargs):
		self._ComplexDiscreteSignal = NWaves.Signals.ComplexDiscreteSignal(*args, **kwargs)
		self.SamplingRate = self._ComplexDiscreteSignal.SamplingRate
		self.Real = self._ComplexDiscreteSignal.Real
		self.Power = self._ComplexDiscreteSignal.Power
		self.PhaseUnwrapped = self._ComplexDiscreteSignal.PhaseUnwrapped
		self.Phase = self._ComplexDiscreteSignal.Phase
		self.Magnitude = self._ComplexDiscreteSignal.Magnitude
		self.Length = self._ComplexDiscreteSignal.Length
		self.Imag = self._ComplexDiscreteSignal.Imag
 
	def copy(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.Copy(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._ComplexDiscreteSignal.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.ToString(*args, **kwargs)
 
	def get_imag(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.get_Imag(*args, **kwargs)
 
	def get_item(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.get_Item(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.get_Length(*args, **kwargs)
 
	def get_magnitude(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.get_Magnitude(*args, **kwargs)
 
	def get_phase(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.get_Phase(*args, **kwargs)
 
	def get_phase_unwrapped(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.get_PhaseUnwrapped(*args, **kwargs)
 
	def get_power(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.get_Power(*args, **kwargs)
 
	def get_real(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.get_Real(*args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.get_SamplingRate(*args, **kwargs)
 
	def op_addition(self, *args, **kwargs):
		return self._ComplexDiscreteSignal.op_Addition(*args, **kwargs)
 
	def op_multiply(self, s, coeff):
		return self._ComplexDiscreteSignal.op_Multiply(s, coeff)
 
	def op_subtraction(self, s, constant):
		return self._ComplexDiscreteSignal.op_Subtraction(s, constant)
 
	def set_item(self, index, value):
		return self._ComplexDiscreteSignal.set_Item(index, value)