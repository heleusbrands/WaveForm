from ...wrapper import NWaves 


 

class VtlnWarper:

	def __init__(self, alpha, lowFrequency, highFrequency, lowVtln, highVtln):
		self._VtlnWarper = NWaves.Filters.Fda.VtlnWarper(alpha, lowFrequency, highFrequency, lowVtln, highVtln)
 
	def equals(self, *args, **kwargs):
		return self._VtlnWarper.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._VtlnWarper.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._VtlnWarper.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._VtlnWarper.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._VtlnWarper.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, alpha, lowFrequency, highFrequency, lowVtln, highVtln):
		return self._VtlnWarper.Overloads(alpha, lowFrequency, highFrequency, lowVtln, highVtln)
 
	def reference_equals(self, objA, objB):
		return self._VtlnWarper.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._VtlnWarper.ToString(*args, **kwargs)
 
	def warp(self, frequency):
		return self._VtlnWarper.Warp(frequency)