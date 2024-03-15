from ..wrapper import NWaves 


 

class DynamicsProcessor:

	def __init__(self, mode, s: int, threshold, ratio, makeupGain: int=0.0, attack: int=0.009999999776482582, release: int=0.10000000149011612, minAmplitudeDb: int=-120.0):
		self._DynamicsProcessor = NWaves.Operations.DynamicsProcessor(mode, samplingRate, threshold, ratio, makeupGain, attack, release, minAmplitudeDb)
		self.Threshold = self._DynamicsProcessor.Threshold
		self.Release = self._DynamicsProcessor.Release
		self.Ratio = self._DynamicsProcessor.Ratio
		self.MakeupGain = self._DynamicsProcessor.MakeupGain
		self.Attack = self._DynamicsProcessor.Attack
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._DynamicsProcessor.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._DynamicsProcessor.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._DynamicsProcessor.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._DynamicsProcessor.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._DynamicsProcessor.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._DynamicsProcessor.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, mode, s: int, threshold, ratio, makeupGain: int=0.0, attack: int=0.009999999776482582, release: int=0.10000000149011612, minAmplitudeDb: int=-120.0):
		return self._DynamicsProcessor.Overloads(mode, samplingRate, threshold, ratio, makeupGain, attack, release, minAmplitudeDb)
 
	def process(self, sample):
		return self._DynamicsProcessor.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._DynamicsProcessor.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._DynamicsProcessor.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._DynamicsProcessor.ToString(*args, **kwargs)
 
	def get_attack(self, *args, **kwargs):
		return self._DynamicsProcessor.get_Attack(*args, **kwargs)
 
	def get_makeup_gain(self, *args, **kwargs):
		return self._DynamicsProcessor.get_MakeupGain(*args, **kwargs)
 
	def get_ratio(self, *args, **kwargs):
		return self._DynamicsProcessor.get_Ratio(*args, **kwargs)
 
	def get_release(self, *args, **kwargs):
		return self._DynamicsProcessor.get_Release(*args, **kwargs)
 
	def get_threshold(self, *args, **kwargs):
		return self._DynamicsProcessor.get_Threshold(*args, **kwargs)
 
	def set_attack(self, value):
		return self._DynamicsProcessor.set_Attack(value)
 
	def set_makeup_gain(self, value):
		return self._DynamicsProcessor.set_MakeupGain(value)
 
	def set_ratio(self, value):
		return self._DynamicsProcessor.set_Ratio(value)
 
	def set_release(self, value):
		return self._DynamicsProcessor.set_Release(value)
 
	def set_threshold(self, value):
		return self._DynamicsProcessor.set_Threshold(value)