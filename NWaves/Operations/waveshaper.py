from ..wrapper import NWaves 


 

class WaveShaper:

	def __init__(self, waveShapingFunction):
		self._WaveShaper = NWaves.Operations.WaveShaper(waveShapingFunction)
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._WaveShaper.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._WaveShaper.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._WaveShaper.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._WaveShaper.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._WaveShaper.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._WaveShaper.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, waveShapingFunction):
		return self._WaveShaper.Overloads(waveShapingFunction)
 
	def process(self, sample):
		return self._WaveShaper.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._WaveShaper.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._WaveShaper.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._WaveShaper.ToString(*args, **kwargs)