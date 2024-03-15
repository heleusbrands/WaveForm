from ..wrapper import NWaves 


 

class VibratoEffect:

	def __init__(self, *args, **kwargs):
		self._VibratoEffect = NWaves.Effects.VibratoEffect(*args, **kwargs)
		self.Width = self._VibratoEffect.Width
		self.Wet = self._VibratoEffect.Wet
		self.LfoFrequency = self._VibratoEffect.LfoFrequency
		self.Lfo = self._VibratoEffect.Lfo
		self.InterpolationMode = self._VibratoEffect.InterpolationMode
		self.Dry = self._VibratoEffect.Dry
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._VibratoEffect.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._VibratoEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._VibratoEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._VibratoEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._VibratoEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._VibratoEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._VibratoEffect.Overloads(*args, **kwargs)
 
	def process(self, sample):
		return self._VibratoEffect.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._VibratoEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._VibratoEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._VibratoEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._VibratoEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._VibratoEffect.WetDryMix(mix, mixingRule)
 
	def get_dry(self, *args, **kwargs):
		return self._VibratoEffect.get_Dry(*args, **kwargs)
 
	def get_interpolation_mode(self, *args, **kwargs):
		return self._VibratoEffect.get_InterpolationMode(*args, **kwargs)
 
	def get_lfo(self, *args, **kwargs):
		return self._VibratoEffect.get_Lfo(*args, **kwargs)
 
	def get_lfo_frequency(self, *args, **kwargs):
		return self._VibratoEffect.get_LfoFrequency(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._VibratoEffect.get_Wet(*args, **kwargs)
 
	def get_width(self, *args, **kwargs):
		return self._VibratoEffect.get_Width(*args, **kwargs)
 
	def set_dry(self, value):
		return self._VibratoEffect.set_Dry(value)
 
	def set_interpolation_mode(self, value):
		return self._VibratoEffect.set_InterpolationMode(value)
 
	def set_lfo(self, value):
		return self._VibratoEffect.set_Lfo(value)
 
	def set_lfo_frequency(self, value):
		return self._VibratoEffect.set_LfoFrequency(value)
 
	def set_wet(self, value):
		return self._VibratoEffect.set_Wet(value)
 
	def set_width(self, value):
		return self._VibratoEffect.set_Width(value)