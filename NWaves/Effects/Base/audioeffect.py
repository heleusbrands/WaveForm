from ...wrapper import NWaves 


 

class AudioEffect:

	def __init__(self, *args, **kwargs):
		self._AudioEffect = NWaves.Effects.Base.AudioEffect(*args, **kwargs)
		self.Wet = self._AudioEffect.Wet
		self.Dry = self._AudioEffect.Dry
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._AudioEffect.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._AudioEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._AudioEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._AudioEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._AudioEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._AudioEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._AudioEffect.Overloads(*args, **kwargs)
 
	def process(self, sample):
		return self._AudioEffect.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._AudioEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._AudioEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._AudioEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._AudioEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._AudioEffect.WetDryMix(mix, mixingRule)
 
	def get_dry(self, *args, **kwargs):
		return self._AudioEffect.get_Dry(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._AudioEffect.get_Wet(*args, **kwargs)
 
	def set_dry(self, value):
		return self._AudioEffect.set_Dry(value)
 
	def set_wet(self, value):
		return self._AudioEffect.set_Wet(value)