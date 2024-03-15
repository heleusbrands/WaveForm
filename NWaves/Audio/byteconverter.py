from ..wrapper import NWaves 


 

class ByteConverter:

	def __init__(self, *args, **kwargs):
		self._ByteConverter = NWaves.Audio.ByteConverter(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._ByteConverter.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._ByteConverter.Finalize(*args, **kwargs)
 
	def from_floats16_bit(self, floats, bytes, normalized: bool=True, bigEndian: bool=False):
		return self._ByteConverter.FromFloats16Bit(floats, bytes, normalized, bigEndian)
 
	def from_floats8_bit(self, floats, bytes, normalized: bool=True):
		return self._ByteConverter.FromFloats8Bit(floats, bytes, normalized)
 
	def get_hash_code(self, *args, **kwargs):
		return self._ByteConverter.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._ByteConverter.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._ByteConverter.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._ByteConverter.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._ByteConverter.ReferenceEquals(objA, objB)
 
	def to_floats16_bit(self, bytes, floats, normalize: bool=True, bigEndian: bool=False):
		return self._ByteConverter.ToFloats16Bit(bytes, floats, normalize, bigEndian)
 
	def to_floats8_bit(self, bytes, floats, normalize: bool=True):
		return self._ByteConverter.ToFloats8Bit(bytes, floats, normalize)
 
	def to_string(self, *args, **kwargs):
		return self._ByteConverter.ToString(*args, **kwargs)