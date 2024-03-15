from ..wrapper import NWaves 


 

class MagnitudePhaseList:

	def __init__(self, *args, **kwargs):
		self._MagnitudePhaseList = NWaves.Transforms.MagnitudePhaseList(*args, **kwargs)
		self.Phases = self._MagnitudePhaseList.Phases
		self.Magnitudes = self._MagnitudePhaseList.Magnitudes
 
	def equals(self, obj):
		return self._MagnitudePhaseList.Equals(obj)
 
	def finalize(self, *args, **kwargs):
		return self._MagnitudePhaseList.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._MagnitudePhaseList.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._MagnitudePhaseList.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._MagnitudePhaseList.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._MagnitudePhaseList.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._MagnitudePhaseList.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._MagnitudePhaseList.ToString(*args, **kwargs)
 
	def get_magnitudes(self, *args, **kwargs):
		return self._MagnitudePhaseList.get_Magnitudes(*args, **kwargs)
 
	def get_phases(self, *args, **kwargs):
		return self._MagnitudePhaseList.get_Phases(*args, **kwargs)
 
	def set_magnitudes(self, value):
		return self._MagnitudePhaseList.set_Magnitudes(value)
 
	def set_phases(self, value):
		return self._MagnitudePhaseList.set_Phases(value)