from ...wrapper import NWaves 


 

class StereoDelayEffect:

	def __init__(self, s: int, pan, delayLeft, delayRight, feedbackLeft: int=0.5, feedbackRight: int=0.5, interpolationMode=NWaves.Utils.InterpolationMode, reserveDelay: int=0.0):
		self._StereoDelayEffect = NWaves.Effects.Stereo.StereoDelayEffect(samplingRate, pan, delayLeft, delayRight, feedbackLeft, feedbackRight, interpolationMode, reserveDelay)
		self.Wet = self._StereoDelayEffect.Wet
		self.Pan = self._StereoDelayEffect.Pan
		self.FeedbackRight = self._StereoDelayEffect.FeedbackRight
		self.FeedbackLeft = self._StereoDelayEffect.FeedbackLeft
		self.Dry = self._StereoDelayEffect.Dry
		self.DelayRight = self._StereoDelayEffect.DelayRight
		self.DelayLeft = self._StereoDelayEffect.DelayLeft
 
	def apply_to(self, *args, **kwargs):
		return self._StereoDelayEffect.ApplyTo(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._StereoDelayEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._StereoDelayEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._StereoDelayEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._StereoDelayEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._StereoDelayEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, s: int, pan, delayLeft, delayRight, feedbackLeft: int=0.5, feedbackRight: int=0.5, interpolationMode=NWaves.Utils.InterpolationMode, reserveDelay: int=0.0):
		return self._StereoDelayEffect.Overloads(samplingRate, pan, delayLeft, delayRight, feedbackLeft, feedbackRight, interpolationMode, reserveDelay)
 
	def process(self, left, right):
		return self._StereoDelayEffect.Process(left, right)
 
	def reference_equals(self, objA, objB):
		return self._StereoDelayEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._StereoDelayEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._StereoDelayEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._StereoDelayEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._StereoDelayEffect.WetDryMix(mix, mixingRule)
 
	def get_delay_left(self, *args, **kwargs):
		return self._StereoDelayEffect.get_DelayLeft(*args, **kwargs)
 
	def get_delay_right(self, *args, **kwargs):
		return self._StereoDelayEffect.get_DelayRight(*args, **kwargs)
 
	def get_dry(self, *args, **kwargs):
		return self._StereoDelayEffect.get_Dry(*args, **kwargs)
 
	def get_feedback_left(self, *args, **kwargs):
		return self._StereoDelayEffect.get_FeedbackLeft(*args, **kwargs)
 
	def get_feedback_right(self, *args, **kwargs):
		return self._StereoDelayEffect.get_FeedbackRight(*args, **kwargs)
 
	def get_pan(self, *args, **kwargs):
		return self._StereoDelayEffect.get_Pan(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._StereoDelayEffect.get_Wet(*args, **kwargs)
 
	def set_delay_left(self, value):
		return self._StereoDelayEffect.set_DelayLeft(value)
 
	def set_delay_right(self, value):
		return self._StereoDelayEffect.set_DelayRight(value)
 
	def set_dry(self, value):
		return self._StereoDelayEffect.set_Dry(value)
 
	def set_feedback_left(self, value):
		return self._StereoDelayEffect.set_FeedbackLeft(value)
 
	def set_feedback_right(self, value):
		return self._StereoDelayEffect.set_FeedbackRight(value)
 
	def set_pan(self, value):
		return self._StereoDelayEffect.set_Pan(value)
 
	def set_wet(self, value):
		return self._StereoDelayEffect.set_Wet(value)