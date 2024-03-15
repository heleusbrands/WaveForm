from ..wrapper import NWaves 


 

class Resampler:

	def __init__(self, *args, **kwargs):
		self._Resampler = NWaves.Operations.Resampler(*args, **kwargs)
		self.MinResamplingFilterOrder = self._Resampler.MinResamplingFilterOrder
 
	def decimate(self, signal, factor, filter=None):
		return self._Resampler.Decimate(signal, factor, filter)
 
	def equals(self, *args, **kwargs):
		return self._Resampler.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Resampler.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Resampler.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Resampler.GetType(*args, **kwargs)
 
	def interpolate(self, signal, factor, filter=None):
		return self._Resampler.Interpolate(signal, factor, filter)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Resampler.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._Resampler.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._Resampler.ReferenceEquals(objA, objB)
 
	def resample(self, signal, n: int, filter=None, order: int=15):
		return self._Resampler.Resample(signal, newSamplingRate, filter, order)
 
	def resample_up_down(self, signal, up, down, filter=None):
		return self._Resampler.ResampleUpDown(signal, up, down, filter)
 
	def to_string(self, *args, **kwargs):
		return self._Resampler.ToString(*args, **kwargs)
 
	def get_min_resampling_filter_order(self, *args, **kwargs):
		return self._Resampler.get_MinResamplingFilterOrder(*args, **kwargs)
 
	def set_min_resampling_filter_order(self, value):
		return self._Resampler.set_MinResamplingFilterOrder(value)