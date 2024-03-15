from ...wrapper import NWaves 


 

class PolyphaseSystem:

	def __init__(self, kern: intel, n: int, type: int=1):
		self._PolyphaseSystem = NWaves.Filters.Polyphase.PolyphaseSystem(kernel, n, type)
		self.MultirateFilters = self._PolyphaseSystem.MultirateFilters
		self.Filters = self._PolyphaseSystem.Filters
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._PolyphaseSystem.ApplyTo(signal, method)
 
	def decimate(self, signal):
		return self._PolyphaseSystem.Decimate(signal)
 
	def equals(self, *args, **kwargs):
		return self._PolyphaseSystem.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._PolyphaseSystem.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._PolyphaseSystem.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._PolyphaseSystem.GetType(*args, **kwargs)
 
	def interpolate(self, signal):
		return self._PolyphaseSystem.Interpolate(signal)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._PolyphaseSystem.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, kern: intel, n: int, type: int=1):
		return self._PolyphaseSystem.Overloads(kernel, n, type)
 
	def process(self, sample):
		return self._PolyphaseSystem.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._PolyphaseSystem.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._PolyphaseSystem.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._PolyphaseSystem.ToString(*args, **kwargs)
 
	def get_filters(self, *args, **kwargs):
		return self._PolyphaseSystem.get_Filters(*args, **kwargs)
 
	def get_multirate_filters(self, *args, **kwargs):
		return self._PolyphaseSystem.get_MultirateFilters(*args, **kwargs)