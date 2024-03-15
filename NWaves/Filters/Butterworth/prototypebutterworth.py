from ...wrapper import NWaves 


 

class PrototypeButterworth:

	def __init__(self, *args, **kwargs):
		self._PrototypeButterworth = NWaves.Filters.Butterworth.PrototypeButterworth(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._PrototypeButterworth.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._PrototypeButterworth.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._PrototypeButterworth.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._PrototypeButterworth.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._PrototypeButterworth.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PrototypeButterworth.Overloads(*args, **kwargs)
 
	def poles(self, order):
		return self._PrototypeButterworth.Poles(order)
 
	def reference_equals(self, objA, objB):
		return self._PrototypeButterworth.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._PrototypeButterworth.ToString(*args, **kwargs)