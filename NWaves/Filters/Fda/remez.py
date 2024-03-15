from ...wrapper import NWaves 


 

class Remez:

	def __init__(self, o: int, frequencies, desired, weights, gridDensity: int=16):
		self._Remez = NWaves.Filters.Fda.Remez(order, frequencies, desired, weights, gridDensity)
		self.Order = self._Remez.Order
		self.K = self._Remez.K
		self.Iterations = self._Remez.Iterations
		self.InterpolatedResponse = self._Remez.InterpolatedResponse
		self.ExtremalFrequencies = self._Remez.ExtremalFrequencies
		self.Error = self._Remez.Error
 
	def db_to_passband_weight(self, ripple):
		return self._Remez.DbToPassbandWeight(ripple)
 
	def db_to_stopband_weight(self, ripple):
		return self._Remez.DbToStopbandWeight(ripple)
 
	def design(self, maxIterations: int=100):
		return self._Remez.Design(maxIterations)
 
	def equals(self, *args, **kwargs):
		return self._Remez.Equals(*args, **kwargs)
 
	def estimate_order(self, *args, **kwargs):
		return self._Remez.EstimateOrder(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Remez.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Remez.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Remez.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Remez.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, o: int, frequencies, desired, weights, gridDensity: int=16):
		return self._Remez.Overloads(order, frequencies, desired, weights, gridDensity)
 
	def reference_equals(self, objA, objB):
		return self._Remez.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._Remez.ToString(*args, **kwargs)
 
	def get_error(self, *args, **kwargs):
		return self._Remez.get_Error(*args, **kwargs)
 
	def get_extremal_frequencies(self, *args, **kwargs):
		return self._Remez.get_ExtremalFrequencies(*args, **kwargs)
 
	def get_interpolated_response(self, *args, **kwargs):
		return self._Remez.get_InterpolatedResponse(*args, **kwargs)
 
	def get_iterations(self, *args, **kwargs):
		return self._Remez.get_Iterations(*args, **kwargs)
 
	def get_k(self, *args, **kwargs):
		return self._Remez.get_K(*args, **kwargs)
 
	def get_order(self, *args, **kwargs):
		return self._Remez.get_Order(*args, **kwargs)