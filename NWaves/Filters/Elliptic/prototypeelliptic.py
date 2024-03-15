from ...wrapper import NWaves 


 

class PrototypeElliptic:

	def __init__(self, *args, **kwargs):
		self._PrototypeElliptic = NWaves.Filters.Elliptic.PrototypeElliptic(*args, **kwargs)
 
	def asne(self, x, k: float, iterCount: int=5):
		return self._PrototypeElliptic.Asne(x, k, iterCount)
 
	def cde(self, x, landen):
		return self._PrototypeElliptic.Cde(x, landen)
 
	def equals(self, *args, **kwargs):
		return self._PrototypeElliptic.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._PrototypeElliptic.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._PrototypeElliptic.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._PrototypeElliptic.GetType(*args, **kwargs)
 
	def landen(self, k: float, iterCount: int=5):
		return self._PrototypeElliptic.Landen(k, iterCount)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._PrototypeElliptic.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PrototypeElliptic.Overloads(*args, **kwargs)
 
	def poles(self, o: int, ripplePass=1.0, rippleStop=20.0):
		return self._PrototypeElliptic.Poles(order, ripplePass, rippleStop)
 
	def reference_equals(self, objA, objB):
		return self._PrototypeElliptic.ReferenceEquals(objA, objB)
 
	def sne(self, x, landen):
		return self._PrototypeElliptic.Sne(x, landen)
 
	def to_string(self, *args, **kwargs):
		return self._PrototypeElliptic.ToString(*args, **kwargs)
 
	def zeros(self, o: int, ripplePass=1.0, rippleStop=20.0):
		return self._PrototypeElliptic.Zeros(order, ripplePass, rippleStop)