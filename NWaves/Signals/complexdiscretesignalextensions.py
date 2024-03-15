from ..wrapper import NWaves 


 

class ComplexDiscreteSignalExtensions:

	def __init__(self, *args, **kwargs):
		self._ComplexDiscreteSignalExtensions = NWaves.Signals.ComplexDiscreteSignalExtensions(*args, **kwargs)
 
	def amplify(self, signal, coeff):
		return self._ComplexDiscreteSignalExtensions.Amplify(signal, coeff)
 
	def attenuate(self, signal, coeff):
		return self._ComplexDiscreteSignalExtensions.Attenuate(signal, coeff)
 
	def concatenate(self, signal1, signal2):
		return self._ComplexDiscreteSignalExtensions.Concatenate(signal1, signal2)
 
	def delay(self, signal, delay):
		return self._ComplexDiscreteSignalExtensions.Delay(signal, delay)
 
	def divide(self, signal1, signal2):
		return self._ComplexDiscreteSignalExtensions.Divide(signal1, signal2)
 
	def equals(self, *args, **kwargs):
		return self._ComplexDiscreteSignalExtensions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._ComplexDiscreteSignalExtensions.Finalize(*args, **kwargs)
 
	def first(self, signal, n):
		return self._ComplexDiscreteSignalExtensions.First(signal, n)
 
	def get_hash_code(self, *args, **kwargs):
		return self._ComplexDiscreteSignalExtensions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._ComplexDiscreteSignalExtensions.GetType(*args, **kwargs)
 
	def last(self, signal, n):
		return self._ComplexDiscreteSignalExtensions.Last(signal, n)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._ComplexDiscreteSignalExtensions.MemberwiseClone(*args, **kwargs)
 
	def multiply(self, signal1, signal2):
		return self._ComplexDiscreteSignalExtensions.Multiply(signal1, signal2)
 
	def overloads(self, *args, **kwargs):
		return self._ComplexDiscreteSignalExtensions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._ComplexDiscreteSignalExtensions.ReferenceEquals(objA, objB)
 
	def repeat(self, signal, n):
		return self._ComplexDiscreteSignalExtensions.Repeat(signal, n)
 
	def superimpose(self, signal1, signal2):
		return self._ComplexDiscreteSignalExtensions.Superimpose(signal1, signal2)
 
	def to_complex_numbers(self, signal):
		return self._ComplexDiscreteSignalExtensions.ToComplexNumbers(signal)
 
	def to_string(self, *args, **kwargs):
		return self._ComplexDiscreteSignalExtensions.ToString(*args, **kwargs)
 
	def unwrap(self, phase, tolerance=3.141592653589793):
		return self._ComplexDiscreteSignalExtensions.Unwrap(phase, tolerance)
 
	def zero_padded(self, signal, length):
		return self._ComplexDiscreteSignalExtensions.ZeroPadded(signal, length)