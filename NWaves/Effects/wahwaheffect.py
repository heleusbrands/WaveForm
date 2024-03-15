from ..wrapper import NWaves 


 

class WahwahEffect:

	def __init__(self, *args, **kwargs):
		self._WahwahEffect = NWaves.Effects.WahwahEffect(*args, **kwargs)
		self.Wet = self._WahwahEffect.Wet
		self.Q = self._WahwahEffect.Q
		self.MinFrequency = self._WahwahEffect.MinFrequency
		self.MaxFrequency = self._WahwahEffect.MaxFrequency
		self.LfoFrequency = self._WahwahEffect.LfoFrequency
		self.Lfo = self._WahwahEffect.Lfo
		self.Dry = self._WahwahEffect.Dry
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._WahwahEffect.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._WahwahEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._WahwahEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._WahwahEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._WahwahEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._WahwahEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._WahwahEffect.Overloads(*args, **kwargs)
 
	def process(self, sample):
		return self._WahwahEffect.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._WahwahEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._WahwahEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._WahwahEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._WahwahEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._WahwahEffect.WetDryMix(mix, mixingRule)
 
	def get_dry(self, *args, **kwargs):
		return self._WahwahEffect.get_Dry(*args, **kwargs)
 
	def get_lfo(self, *args, **kwargs):
		return self._WahwahEffect.get_Lfo(*args, **kwargs)
 
	def get_lfo_frequency(self, *args, **kwargs):
		return self._WahwahEffect.get_LfoFrequency(*args, **kwargs)
 
	def get_max_frequency(self, *args, **kwargs):
		return self._WahwahEffect.get_MaxFrequency(*args, **kwargs)
 
	def get_min_frequency(self, *args, **kwargs):
		return self._WahwahEffect.get_MinFrequency(*args, **kwargs)
 
	def get_q(self, *args, **kwargs):
		return self._WahwahEffect.get_Q(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._WahwahEffect.get_Wet(*args, **kwargs)
 
	def set_dry(self, value):
		return self._WahwahEffect.set_Dry(value)
 
	def set_lfo(self, value):
		return self._WahwahEffect.set_Lfo(value)
 
	def set_lfo_frequency(self, value):
		return self._WahwahEffect.set_LfoFrequency(value)
 
	def set_max_frequency(self, value):
		return self._WahwahEffect.set_MaxFrequency(value)
 
	def set_min_frequency(self, value):
		return self._WahwahEffect.set_MinFrequency(value)
 
	def set_q(self, value):
		return self._WahwahEffect.set_Q(value)
 
	def set_wet(self, value):
		return self._WahwahEffect.set_Wet(value)