from ...wrapper import NWaves 


 

class PingPongDelayEffect:

	def __init__(self, s: int, pan, delay, feedback: int=0.5, interpolationMode=NWaves.Utils.InterpolationMode, reserveDelay: int=0.0):
		self._PingPongDelayEffect = NWaves.Effects.Stereo.PingPongDelayEffect(samplingRate, pan, delay, feedback, interpolationMode, reserveDelay)
		self.Wet = self._PingPongDelayEffect.Wet
		self.Pan = self._PingPongDelayEffect.Pan
		self.Feedback = self._PingPongDelayEffect.Feedback
		self.Dry = self._PingPongDelayEffect.Dry
		self.Delay = self._PingPongDelayEffect.Delay
 
	def apply_to(self, *args, **kwargs):
		return self._PingPongDelayEffect.ApplyTo(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._PingPongDelayEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._PingPongDelayEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._PingPongDelayEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._PingPongDelayEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._PingPongDelayEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, s: int, pan, delay, feedback: int=0.5, interpolationMode=NWaves.Utils.InterpolationMode, reserveDelay: int=0.0):
		return self._PingPongDelayEffect.Overloads(samplingRate, pan, delay, feedback, interpolationMode, reserveDelay)
 
	def process(self, left, right):
		return self._PingPongDelayEffect.Process(left, right)
 
	def reference_equals(self, objA, objB):
		return self._PingPongDelayEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._PingPongDelayEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._PingPongDelayEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._PingPongDelayEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._PingPongDelayEffect.WetDryMix(mix, mixingRule)
 
	def get_delay(self, *args, **kwargs):
		return self._PingPongDelayEffect.get_Delay(*args, **kwargs)
 
	def get_dry(self, *args, **kwargs):
		return self._PingPongDelayEffect.get_Dry(*args, **kwargs)
 
	def get_feedback(self, *args, **kwargs):
		return self._PingPongDelayEffect.get_Feedback(*args, **kwargs)
 
	def get_pan(self, *args, **kwargs):
		return self._PingPongDelayEffect.get_Pan(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._PingPongDelayEffect.get_Wet(*args, **kwargs)
 
	def set_delay(self, value):
		return self._PingPongDelayEffect.set_Delay(value)
 
	def set_dry(self, value):
		return self._PingPongDelayEffect.set_Dry(value)
 
	def set_feedback(self, value):
		return self._PingPongDelayEffect.set_Feedback(value)
 
	def set_pan(self, value):
		return self._PingPongDelayEffect.set_Pan(value)
 
	def set_wet(self, value):
		return self._PingPongDelayEffect.set_Wet(value)