from ..wrapper import NWaves 


 

class FlangerEffect:

	def __init__(self, *args, **kwargs):
		self._FlangerEffect = NWaves.Effects.FlangerEffect(*args, **kwargs)
		self.Width = self._FlangerEffect.Width
		self.Wet = self._FlangerEffect.Wet
		self.LfoFrequency = self._FlangerEffect.LfoFrequency
		self.Lfo = self._FlangerEffect.Lfo
		self.Inverted = self._FlangerEffect.Inverted
		self.InterpolationMode = self._FlangerEffect.InterpolationMode
		self.Feedback = self._FlangerEffect.Feedback
		self.Dry = self._FlangerEffect.Dry
		self.Depth = self._FlangerEffect.Depth
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._FlangerEffect.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._FlangerEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._FlangerEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._FlangerEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._FlangerEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._FlangerEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._FlangerEffect.Overloads(*args, **kwargs)
 
	def process(self, sample):
		return self._FlangerEffect.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._FlangerEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._FlangerEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._FlangerEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._FlangerEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._FlangerEffect.WetDryMix(mix, mixingRule)
 
	def get_depth(self, *args, **kwargs):
		return self._FlangerEffect.get_Depth(*args, **kwargs)
 
	def get_dry(self, *args, **kwargs):
		return self._FlangerEffect.get_Dry(*args, **kwargs)
 
	def get_feedback(self, *args, **kwargs):
		return self._FlangerEffect.get_Feedback(*args, **kwargs)
 
	def get_interpolation_mode(self, *args, **kwargs):
		return self._FlangerEffect.get_InterpolationMode(*args, **kwargs)
 
	def get_inverted(self, *args, **kwargs):
		return self._FlangerEffect.get_Inverted(*args, **kwargs)
 
	def get_lfo(self, *args, **kwargs):
		return self._FlangerEffect.get_Lfo(*args, **kwargs)
 
	def get_lfo_frequency(self, *args, **kwargs):
		return self._FlangerEffect.get_LfoFrequency(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._FlangerEffect.get_Wet(*args, **kwargs)
 
	def get_width(self, *args, **kwargs):
		return self._FlangerEffect.get_Width(*args, **kwargs)
 
	def set_depth(self, value):
		return self._FlangerEffect.set_Depth(value)
 
	def set_dry(self, value):
		return self._FlangerEffect.set_Dry(value)
 
	def set_feedback(self, value):
		return self._FlangerEffect.set_Feedback(value)
 
	def set_interpolation_mode(self, value):
		return self._FlangerEffect.set_InterpolationMode(value)
 
	def set_inverted(self, value):
		return self._FlangerEffect.set_Inverted(value)
 
	def set_lfo(self, value):
		return self._FlangerEffect.set_Lfo(value)
 
	def set_lfo_frequency(self, value):
		return self._FlangerEffect.set_LfoFrequency(value)
 
	def set_wet(self, value):
		return self._FlangerEffect.set_Wet(value)
 
	def set_width(self, value):
		return self._FlangerEffect.set_Width(value)