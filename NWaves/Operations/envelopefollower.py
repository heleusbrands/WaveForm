from ..wrapper import NWaves 


 

class EnvelopeFollower:

	def __init__(self, s: int, attackTime: int=0.009999999776482582, releaseTime: int=0.05000000074505806):
		self._EnvelopeFollower = NWaves.Operations.EnvelopeFollower(samplingRate, attackTime, releaseTime)
		self.ReleaseTime = self._EnvelopeFollower.ReleaseTime
		self.AttackTime = self._EnvelopeFollower.AttackTime
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._EnvelopeFollower.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._EnvelopeFollower.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._EnvelopeFollower.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._EnvelopeFollower.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._EnvelopeFollower.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._EnvelopeFollower.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, s: int, attackTime: int=0.009999999776482582, releaseTime: int=0.05000000074505806):
		return self._EnvelopeFollower.Overloads(samplingRate, attackTime, releaseTime)
 
	def process(self, sample):
		return self._EnvelopeFollower.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._EnvelopeFollower.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._EnvelopeFollower.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._EnvelopeFollower.ToString(*args, **kwargs)
 
	def get_attack_time(self, *args, **kwargs):
		return self._EnvelopeFollower.get_AttackTime(*args, **kwargs)
 
	def get_release_time(self, *args, **kwargs):
		return self._EnvelopeFollower.get_ReleaseTime(*args, **kwargs)
 
	def set_attack_time(self, value):
		return self._EnvelopeFollower.set_AttackTime(value)
 
	def set_release_time(self, value):
		return self._EnvelopeFollower.set_ReleaseTime(value)