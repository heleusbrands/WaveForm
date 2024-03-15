from ..wrapper import NWaves 


 

class GriffinLimReconstructor:

	def __init__(self, *args, **kwargs):
		self._GriffinLimReconstructor = NWaves.Operations.GriffinLimReconstructor(*args, **kwargs)
		self.Gain = self._GriffinLimReconstructor.Gain
 
	def equals(self, *args, **kwargs):
		return self._GriffinLimReconstructor.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._GriffinLimReconstructor.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._GriffinLimReconstructor.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._GriffinLimReconstructor.GetType(*args, **kwargs)
 
	def iterate(self, signal=None):
		return self._GriffinLimReconstructor.Iterate(signal)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._GriffinLimReconstructor.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._GriffinLimReconstructor.Overloads(*args, **kwargs)
 
	def reconstruct(self, iterations: int=20):
		return self._GriffinLimReconstructor.Reconstruct(iterations)
 
	def reference_equals(self, objA, objB):
		return self._GriffinLimReconstructor.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._GriffinLimReconstructor.ToString(*args, **kwargs)
 
	def get_gain(self, *args, **kwargs):
		return self._GriffinLimReconstructor.get_Gain(*args, **kwargs)
 
	def set_gain(self, value):
		return self._GriffinLimReconstructor.set_Gain(value)