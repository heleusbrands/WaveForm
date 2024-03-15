from ..wrapper import NWaves 


 

class MemoryOperationExtensions:

	def __init__(self, *args, **kwargs):
		self._MemoryOperationExtensions = NWaves.Utils.MemoryOperationExtensions(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._MemoryOperationExtensions.Equals(*args, **kwargs)
 
	def fast_copy(self, source):
		return self._MemoryOperationExtensions.FastCopy(source)
 
	def fast_copy_fragment(self, source, s: int, sourceOffset: int=0, destinationOffset: int=0):
		return self._MemoryOperationExtensions.FastCopyFragment(source, size, sourceOffset, destinationOffset)
 
	def fast_copy_to(self, source, destination, s: int, sourceOffset: int=0, destinationOffset: int=0):
		return self._MemoryOperationExtensions.FastCopyTo(source, destination, size, sourceOffset, destinationOffset)
 
	def finalize(self, *args, **kwargs):
		return self._MemoryOperationExtensions.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._MemoryOperationExtensions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._MemoryOperationExtensions.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._MemoryOperationExtensions.MemberwiseClone(*args, **kwargs)
 
	def merge_with_array(self, source, another):
		return self._MemoryOperationExtensions.MergeWithArray(source, another)
 
	def overloads(self, *args, **kwargs):
		return self._MemoryOperationExtensions.Overloads(*args, **kwargs)
 
	def pad_zeros(self, source, size):
		return self._MemoryOperationExtensions.PadZeros(source, size)
 
	def reference_equals(self, objA, objB):
		return self._MemoryOperationExtensions.ReferenceEquals(objA, objB)
 
	def repeat_array(self, source, n):
		return self._MemoryOperationExtensions.RepeatArray(source, n)
 
	def to_doubles(self, values):
		return self._MemoryOperationExtensions.ToDoubles(values)
 
	def to_floats(self, values):
		return self._MemoryOperationExtensions.ToFloats(values)
 
	def to_string(self, *args, **kwargs):
		return self._MemoryOperationExtensions.ToString(*args, **kwargs)