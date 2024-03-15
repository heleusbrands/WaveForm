from ...wrapper import NWaves 


 

class PrototypeChebyshevI:

	def __init__(self, *args, **kwargs):
		self._PrototypeChebyshevI = NWaves.Filters.ChebyshevI.PrototypeChebyshevI(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._PrototypeChebyshevI.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._PrototypeChebyshevI.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._PrototypeChebyshevI.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._PrototypeChebyshevI.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._PrototypeChebyshevI.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PrototypeChebyshevI.Overloads(*args, **kwargs)
 
	def poles(self, o: int, ripple=0.1):
		return self._PrototypeChebyshevI.Poles(order, ripple)
 
	def reference_equals(self, objA, objB):
		return self._PrototypeChebyshevI.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._PrototypeChebyshevI.ToString(*args, **kwargs)