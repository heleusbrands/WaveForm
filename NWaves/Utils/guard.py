from ..wrapper import NWaves 


 

class Guard:

	def __init__(self, *args, **kwargs):
		self._Guard = NWaves.Utils.Guard(*args, **kwargs)
 
	def against_even_number(self, n, argName='Parameter'):
		return self._Guard.AgainstEvenNumber(n, argName)
 
	def against_exceedance(self, low, high, lowName='low', highName='high'):
		return self._Guard.AgainstExceedance(low, high, lowName, highName)
 
	def against_incorrect_filter_params(self, freqs, desired, weights):
		return self._Guard.AgainstIncorrectFilterParams(freqs, desired, weights)
 
	def against_inequality(self, arg1, arg2, arg1Name='argument1', arg2Name='argument2'):
		return self._Guard.AgainstInequality(arg1, arg2, arg1Name, arg2Name)
 
	def against_invalid_range(self, *args, **kwargs):
		return self._Guard.AgainstInvalidRange(*args, **kwargs)
 
	def against_non_positive(self, arg, argName='argument'):
		return self._Guard.AgainstNonPositive(arg, argName)
 
	def against_not_ordered(self, values, argName='Values'):
		return self._Guard.AgainstNotOrdered(values, argName)
 
	def against_not_power_of_two(self, n, argName='Parameter'):
		return self._Guard.AgainstNotPowerOfTwo(n, argName)
 
	def equals(self, *args, **kwargs):
		return self._Guard.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Guard.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Guard.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Guard.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Guard.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._Guard.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._Guard.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._Guard.ToString(*args, **kwargs)