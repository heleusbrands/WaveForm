from ..wrapper import NWaves 


 

class EchoEffect:

	def __init__(self, s: int, delay, feedback: int=0.5, interpolationMode=NWaves.Utils.InterpolationMode, reserveDelay: int=0.0):
		self._EchoEffect = NWaves.Effects.EchoEffect(samplingRate, delay, feedback, interpolationMode, reserveDelay)
		self.Wet = self._EchoEffect.Wet
		self.Feedback = self._EchoEffect.Feedback
		self.Dry = self._EchoEffect.Dry
		self.Delay = self._EchoEffect.Delay
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._EchoEffect.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._EchoEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._EchoEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._EchoEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._EchoEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._EchoEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, s: int, delay, feedback: int=0.5, interpolationMode=NWaves.Utils.InterpolationMode, reserveDelay: int=0.0):
		return self._EchoEffect.Overloads(samplingRate, delay, feedback, interpolationMode, reserveDelay)
 
	def process(self, sample):
		return self._EchoEffect.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._EchoEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._EchoEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._EchoEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._EchoEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._EchoEffect.WetDryMix(mix, mixingRule)
 
	def get_delay(self, *args, **kwargs):
		return self._EchoEffect.get_Delay(*args, **kwargs)
 
	def get_dry(self, *args, **kwargs):
		return self._EchoEffect.get_Dry(*args, **kwargs)
 
	def get_feedback(self, *args, **kwargs):
		return self._EchoEffect.get_Feedback(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._EchoEffect.get_Wet(*args, **kwargs)
 
	def set_delay(self, value):
		return self._EchoEffect.set_Delay(value)
 
	def set_dry(self, value):
		return self._EchoEffect.set_Dry(value)
 
	def set_feedback(self, value):
		return self._EchoEffect.set_Feedback(value)
 
	def set_wet(self, value):
		return self._EchoEffect.set_Wet(value)