from ...wrapper import NWaves 


 

class StereoEffect:

	def __init__(self, *args, **kwargs):
		self._StereoEffect = NWaves.Effects.Stereo.StereoEffect(*args, **kwargs)
		self.Wet = self._StereoEffect.Wet
		self.Dry = self._StereoEffect.Dry
 
	def apply_to(self, *args, **kwargs):
		return self._StereoEffect.ApplyTo(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._StereoEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._StereoEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._StereoEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._StereoEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._StereoEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._StereoEffect.Overloads(*args, **kwargs)
 
	def process(self, *args, **kwargs):
		return self._StereoEffect.Process(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._StereoEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._StereoEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._StereoEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._StereoEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._StereoEffect.WetDryMix(mix, mixingRule)
 
	def get_dry(self, *args, **kwargs):
		return self._StereoEffect.get_Dry(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._StereoEffect.get_Wet(*args, **kwargs)
 
	def set_dry(self, value):
		return self._StereoEffect.set_Dry(value)
 
	def set_wet(self, value):
		return self._StereoEffect.set_Wet(value)