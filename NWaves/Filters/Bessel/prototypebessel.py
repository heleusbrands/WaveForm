from ...wrapper import NWaves 


 

class PrototypeBessel:

	def __init__(self, *args, **kwargs):
		self._PrototypeBessel = NWaves.Filters.Bessel.PrototypeBessel(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._PrototypeBessel.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._PrototypeBessel.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._PrototypeBessel.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._PrototypeBessel.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._PrototypeBessel.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PrototypeBessel.Overloads(*args, **kwargs)
 
	def poles(self, order):
		return self._PrototypeBessel.Poles(order)
 
	def reference_equals(self, objA, objB):
		return self._PrototypeBessel.ReferenceEquals(objA, objB)
 
	def reverse(self, k, n):
		return self._PrototypeBessel.Reverse(k, n)
 
	def to_string(self, *args, **kwargs):
		return self._PrototypeBessel.ToString(*args, **kwargs)