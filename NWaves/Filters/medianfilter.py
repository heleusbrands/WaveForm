from ..wrapper import NWaves 


 

class MedianFilter:

	def __init__(self, size: int=9):
		self._MedianFilter = NWaves.Filters.MedianFilter(size)
		self.Size = self._MedianFilter.Size
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._MedianFilter.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._MedianFilter.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._MedianFilter.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._MedianFilter.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._MedianFilter.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._MedianFilter.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, size: int=9):
		return self._MedianFilter.Overloads(size)
 
	def process(self, sample):
		return self._MedianFilter.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._MedianFilter.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._MedianFilter.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._MedianFilter.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._MedianFilter.get_Size(*args, **kwargs)