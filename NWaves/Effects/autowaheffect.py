from ..wrapper import NWaves 


 

class AutowahEffect:

	def __init__(self, s: int, minFreq: intuency: int=30.0, maxFreq: intuency: int=2000.0, q: int=0.5, attackTime: int=0.009999999776482582, releaseTime: int=0.05000000074505806):
		self._AutowahEffect = NWaves.Effects.AutowahEffect(samplingRate, minFrequency, maxFrequency, q, attackTime, releaseTime)
		self.Wet = self._AutowahEffect.Wet
		self.ReleaseTime = self._AutowahEffect.ReleaseTime
		self.Q = self._AutowahEffect.Q
		self.MinFrequency = self._AutowahEffect.MinFrequency
		self.MaxFrequency = self._AutowahEffect.MaxFrequency
		self.Dry = self._AutowahEffect.Dry
		self.AttackTime = self._AutowahEffect.AttackTime
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._AutowahEffect.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._AutowahEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._AutowahEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._AutowahEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._AutowahEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._AutowahEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, s: int, minFreq: intuency: int=30.0, maxFreq: intuency: int=2000.0, q: int=0.5, attackTime: int=0.009999999776482582, releaseTime: int=0.05000000074505806):
		return self._AutowahEffect.Overloads(samplingRate, minFrequency, maxFrequency, q, attackTime, releaseTime)
 
	def process(self, sample):
		return self._AutowahEffect.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._AutowahEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._AutowahEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._AutowahEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._AutowahEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._AutowahEffect.WetDryMix(mix, mixingRule)
 
	def get_attack_time(self, *args, **kwargs):
		return self._AutowahEffect.get_AttackTime(*args, **kwargs)
 
	def get_dry(self, *args, **kwargs):
		return self._AutowahEffect.get_Dry(*args, **kwargs)
 
	def get_max_frequency(self, *args, **kwargs):
		return self._AutowahEffect.get_MaxFrequency(*args, **kwargs)
 
	def get_min_frequency(self, *args, **kwargs):
		return self._AutowahEffect.get_MinFrequency(*args, **kwargs)
 
	def get_q(self, *args, **kwargs):
		return self._AutowahEffect.get_Q(*args, **kwargs)
 
	def get_release_time(self, *args, **kwargs):
		return self._AutowahEffect.get_ReleaseTime(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._AutowahEffect.get_Wet(*args, **kwargs)
 
	def set_attack_time(self, value):
		return self._AutowahEffect.set_AttackTime(value)
 
	def set_dry(self, value):
		return self._AutowahEffect.set_Dry(value)
 
	def set_max_frequency(self, value):
		return self._AutowahEffect.set_MaxFrequency(value)
 
	def set_min_frequency(self, value):
		return self._AutowahEffect.set_MinFrequency(value)
 
	def set_q(self, value):
		return self._AutowahEffect.set_Q(value)
 
	def set_release_time(self, value):
		return self._AutowahEffect.set_ReleaseTime(value)
 
	def set_wet(self, value):
		return self._AutowahEffect.set_Wet(value)