from ...wrapper import NWaves 


 

class StateSpace:

	def __init__(self, *args, **kwargs):
		self._StateSpace = NWaves.Filters.Base.StateSpace(*args, **kwargs)
		self.D = self._StateSpace.D
		self.C = self._StateSpace.C
		self.B = self._StateSpace.B
		self.A = self._StateSpace.A
 
	def equals(self, *args, **kwargs):
		return self._StateSpace.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._StateSpace.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._StateSpace.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._StateSpace.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._StateSpace.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._StateSpace.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._StateSpace.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._StateSpace.ToString(*args, **kwargs)
 
	def get_a(self, *args, **kwargs):
		return self._StateSpace.get_A(*args, **kwargs)
 
	def get_b(self, *args, **kwargs):
		return self._StateSpace.get_B(*args, **kwargs)
 
	def get_c(self, *args, **kwargs):
		return self._StateSpace.get_C(*args, **kwargs)
 
	def get_d(self, *args, **kwargs):
		return self._StateSpace.get_D(*args, **kwargs)
 
	def set_a(self, value):
		return self._StateSpace.set_A(value)
 
	def set_b(self, value):
		return self._StateSpace.set_B(value)
 
	def set_c(self, value):
		return self._StateSpace.set_C(value)
 
	def set_d(self, value):
		return self._StateSpace.set_D(value)