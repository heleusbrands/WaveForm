from ..wrapper import NWaves 


 

class FractionalDelayLine:

	def __init__(self, *args, **kwargs):
		self._FractionalDelayLine = NWaves.Utils.FractionalDelayLine(*args, **kwargs)
		self.Size = self._FractionalDelayLine.Size
		self.InterpolationMode = self._FractionalDelayLine.InterpolationMode
 
	def ensure(self, *args, **kwargs):
		return self._FractionalDelayLine.Ensure(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._FractionalDelayLine.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._FractionalDelayLine.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._FractionalDelayLine.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._FractionalDelayLine.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._FractionalDelayLine.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._FractionalDelayLine.Overloads(*args, **kwargs)
 
	def read(self, delay):
		return self._FractionalDelayLine.Read(delay)
 
	def reference_equals(self, objA, objB):
		return self._FractionalDelayLine.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._FractionalDelayLine.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._FractionalDelayLine.ToString(*args, **kwargs)
 
	def write(self, sample):
		return self._FractionalDelayLine.Write(sample)
 
	def get_interpolation_mode(self, *args, **kwargs):
		return self._FractionalDelayLine.get_InterpolationMode(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._FractionalDelayLine.get_Size(*args, **kwargs)
 
	def set_interpolation_mode(self, value):
		return self._FractionalDelayLine.set_InterpolationMode(value)