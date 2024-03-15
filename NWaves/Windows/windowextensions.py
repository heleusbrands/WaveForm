from ..wrapper import NWaves 


 

class WindowExtensions:

	def __init__(self, *args, **kwargs):
		self._WindowExtensions = NWaves.Windows.WindowExtensions(*args, **kwargs)
 
	def apply_window(self, *args, **kwargs):
		return self._WindowExtensions.ApplyWindow(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._WindowExtensions.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._WindowExtensions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._WindowExtensions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._WindowExtensions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._WindowExtensions.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._WindowExtensions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._WindowExtensions.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._WindowExtensions.ToString(*args, **kwargs)