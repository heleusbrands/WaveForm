from ...wrapper import NWaves 


 

class WetDryMixer:

	def __init__(self, *args, **kwargs):
		self._WetDryMixer = NWaves.Effects.Base.WetDryMixer(*args, **kwargs)
		self.Wet = self._WetDryMixer.Wet
		self.Dry = self._WetDryMixer.Dry
 
	def equals(self, *args, **kwargs):
		return self._WetDryMixer.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._WetDryMixer.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._WetDryMixer.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._WetDryMixer.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._WetDryMixer.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._WetDryMixer.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._WetDryMixer.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._WetDryMixer.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._WetDryMixer.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._WetDryMixer.WetDryMix(mix, mixingRule)
 
	def get_dry(self, *args, **kwargs):
		return self._WetDryMixer.get_Dry(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._WetDryMixer.get_Wet(*args, **kwargs)
 
	def set_dry(self, value):
		return self._WetDryMixer.set_Dry(value)
 
	def set_wet(self, value):
		return self._WetDryMixer.set_Wet(value)