from ...wrapper import NWaves 


 

class PrototypeChebyshevII:

	def __init__(self, *args, **kwargs):
		self._PrototypeChebyshevII = NWaves.Filters.ChebyshevII.PrototypeChebyshevII(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._PrototypeChebyshevII.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._PrototypeChebyshevII.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._PrototypeChebyshevII.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._PrototypeChebyshevII.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._PrototypeChebyshevII.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PrototypeChebyshevII.Overloads(*args, **kwargs)
 
	def poles(self, o: int, ripple=0.1):
		return self._PrototypeChebyshevII.Poles(order, ripple)
 
	def reference_equals(self, objA, objB):
		return self._PrototypeChebyshevII.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._PrototypeChebyshevII.ToString(*args, **kwargs)
 
	def zeros(self, order):
		return self._PrototypeChebyshevII.Zeros(order)