from ..wrapper import NWaves 


 

class DelayEffect:

	def __init__(self, s: int, delay, feedback: int=0.5, interpolationMode=NWaves.Utils.InterpolationMode, reserveDelay: int=0.0):
		self._DelayEffect = NWaves.Effects.DelayEffect(samplingRate, delay, feedback, interpolationMode, reserveDelay)
		self.Wet = self._DelayEffect.Wet
		self.Feedback = self._DelayEffect.Feedback
		self.Dry = self._DelayEffect.Dry
		self.Delay = self._DelayEffect.Delay
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._DelayEffect.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._DelayEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._DelayEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._DelayEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._DelayEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._DelayEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, s: int, delay, feedback: int=0.5, interpolationMode=NWaves.Utils.InterpolationMode, reserveDelay: int=0.0):
		return self._DelayEffect.Overloads(samplingRate, delay, feedback, interpolationMode, reserveDelay)
 
	def process(self, sample):
		return self._DelayEffect.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._DelayEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._DelayEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._DelayEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._DelayEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._DelayEffect.WetDryMix(mix, mixingRule)
 
	def get_delay(self, *args, **kwargs):
		return self._DelayEffect.get_Delay(*args, **kwargs)
 
	def get_dry(self, *args, **kwargs):
		return self._DelayEffect.get_Dry(*args, **kwargs)
 
	def get_feedback(self, *args, **kwargs):
		return self._DelayEffect.get_Feedback(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._DelayEffect.get_Wet(*args, **kwargs)
 
	def set_delay(self, value):
		return self._DelayEffect.set_Delay(value)
 
	def set_dry(self, value):
		return self._DelayEffect.set_Dry(value)
 
	def set_feedback(self, value):
		return self._DelayEffect.set_Feedback(value)
 
	def set_wet(self, value):
		return self._DelayEffect.set_Wet(value)