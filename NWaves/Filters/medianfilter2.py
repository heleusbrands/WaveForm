from ..wrapper import NWaves 


 

class MedianFilter2:

	def __init__(self, size: int=9):
		self._MedianFilter2 = NWaves.Filters.MedianFilter2(size)
		self.Size = self._MedianFilter2.Size
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._MedianFilter2.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._MedianFilter2.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._MedianFilter2.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._MedianFilter2.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._MedianFilter2.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._MedianFilter2.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, size: int=9):
		return self._MedianFilter2.Overloads(size)
 
	def process(self, sample):
		return self._MedianFilter2.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._MedianFilter2.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._MedianFilter2.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._MedianFilter2.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._MedianFilter2.get_Size(*args, **kwargs)