from ..wrapper import NWaves 


 

class ChorusEffect:

	def __init__(self, *args, **kwargs):
		self._ChorusEffect = NWaves.Effects.ChorusEffect(*args, **kwargs)
		self.Widths = self._ChorusEffect.Widths
		self.Wet = self._ChorusEffect.Wet
		self.LfoFrequencies = self._ChorusEffect.LfoFrequencies
		self.Dry = self._ChorusEffect.Dry
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._ChorusEffect.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._ChorusEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._ChorusEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._ChorusEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._ChorusEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._ChorusEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._ChorusEffect.Overloads(*args, **kwargs)
 
	def process(self, sample):
		return self._ChorusEffect.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._ChorusEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._ChorusEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._ChorusEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._ChorusEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._ChorusEffect.WetDryMix(mix, mixingRule)
 
	def get_dry(self, *args, **kwargs):
		return self._ChorusEffect.get_Dry(*args, **kwargs)
 
	def get_lfo_frequencies(self, *args, **kwargs):
		return self._ChorusEffect.get_LfoFrequencies(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._ChorusEffect.get_Wet(*args, **kwargs)
 
	def get_widths(self, *args, **kwargs):
		return self._ChorusEffect.get_Widths(*args, **kwargs)
 
	def set_dry(self, value):
		return self._ChorusEffect.set_Dry(value)
 
	def set_lfo_frequencies(self, value):
		return self._ChorusEffect.set_LfoFrequencies(value)
 
	def set_wet(self, value):
		return self._ChorusEffect.set_Wet(value)
 
	def set_widths(self, value):
		return self._ChorusEffect.set_Widths(value)