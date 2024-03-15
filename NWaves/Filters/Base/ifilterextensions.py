from ...wrapper import NWaves 


 

class IFilterExtensions:

	def __init__(self, *args, **kwargs):
		self._IFilterExtensions = NWaves.Filters.Base.IFilterExtensions(*args, **kwargs)
 
	def apply_to(self, filter, signal, gain):
		return self._IFilterExtensions.ApplyTo(filter, signal, gain)
 
	def equals(self, *args, **kwargs):
		return self._IFilterExtensions.Equals(*args, **kwargs)
 
	def estimate_gain(self, filter, fftSize: int=512):
		return self._IFilterExtensions.EstimateGain(filter, fftSize)
 
	def filter_online(self, filter, signal):
		return self._IFilterExtensions.FilterOnline(filter, signal)
 
	def finalize(self, *args, **kwargs):
		return self._IFilterExtensions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._IFilterExtensions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._IFilterExtensions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._IFilterExtensions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._IFilterExtensions.Overloads(*args, **kwargs)
 
	def process(self, *args, **kwargs):
		return self._IFilterExtensions.Process(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._IFilterExtensions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._IFilterExtensions.ToString(*args, **kwargs)