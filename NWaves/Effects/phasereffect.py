from ..wrapper import NWaves 


 

class PhaserEffect:

	def __init__(self, *args, **kwargs):
		self._PhaserEffect = NWaves.Effects.PhaserEffect(*args, **kwargs)
		self.Wet = self._PhaserEffect.Wet
		self.Q = self._PhaserEffect.Q
		self.MinFrequency = self._PhaserEffect.MinFrequency
		self.MaxFrequency = self._PhaserEffect.MaxFrequency
		self.LfoFrequency = self._PhaserEffect.LfoFrequency
		self.Lfo = self._PhaserEffect.Lfo
		self.Dry = self._PhaserEffect.Dry
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._PhaserEffect.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._PhaserEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._PhaserEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._PhaserEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._PhaserEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._PhaserEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PhaserEffect.Overloads(*args, **kwargs)
 
	def process(self, sample):
		return self._PhaserEffect.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._PhaserEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._PhaserEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._PhaserEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._PhaserEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._PhaserEffect.WetDryMix(mix, mixingRule)
 
	def get_dry(self, *args, **kwargs):
		return self._PhaserEffect.get_Dry(*args, **kwargs)
 
	def get_lfo(self, *args, **kwargs):
		return self._PhaserEffect.get_Lfo(*args, **kwargs)
 
	def get_lfo_frequency(self, *args, **kwargs):
		return self._PhaserEffect.get_LfoFrequency(*args, **kwargs)
 
	def get_max_frequency(self, *args, **kwargs):
		return self._PhaserEffect.get_MaxFrequency(*args, **kwargs)
 
	def get_min_frequency(self, *args, **kwargs):
		return self._PhaserEffect.get_MinFrequency(*args, **kwargs)
 
	def get_q(self, *args, **kwargs):
		return self._PhaserEffect.get_Q(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._PhaserEffect.get_Wet(*args, **kwargs)
 
	def set_dry(self, value):
		return self._PhaserEffect.set_Dry(value)
 
	def set_lfo(self, value):
		return self._PhaserEffect.set_Lfo(value)
 
	def set_lfo_frequency(self, value):
		return self._PhaserEffect.set_LfoFrequency(value)
 
	def set_max_frequency(self, value):
		return self._PhaserEffect.set_MaxFrequency(value)
 
	def set_min_frequency(self, value):
		return self._PhaserEffect.set_MinFrequency(value)
 
	def set_q(self, value):
		return self._PhaserEffect.set_Q(value)
 
	def set_wet(self, value):
		return self._PhaserEffect.set_Wet(value)