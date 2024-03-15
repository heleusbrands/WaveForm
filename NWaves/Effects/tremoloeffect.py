from ..wrapper import NWaves 


 

class TremoloEffect:

	def __init__(self, *args, **kwargs):
		self._TremoloEffect = NWaves.Effects.TremoloEffect(*args, **kwargs)
		self.Wet = self._TremoloEffect.Wet
		self.Lfo = self._TremoloEffect.Lfo
		self.Index = self._TremoloEffect.Index
		self.Frequency = self._TremoloEffect.Frequency
		self.Dry = self._TremoloEffect.Dry
		self.Depth = self._TremoloEffect.Depth
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._TremoloEffect.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._TremoloEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._TremoloEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._TremoloEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._TremoloEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._TremoloEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._TremoloEffect.Overloads(*args, **kwargs)
 
	def process(self, sample):
		return self._TremoloEffect.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._TremoloEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._TremoloEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._TremoloEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._TremoloEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._TremoloEffect.WetDryMix(mix, mixingRule)
 
	def get_depth(self, *args, **kwargs):
		return self._TremoloEffect.get_Depth(*args, **kwargs)
 
	def get_dry(self, *args, **kwargs):
		return self._TremoloEffect.get_Dry(*args, **kwargs)
 
	def get_frequency(self, *args, **kwargs):
		return self._TremoloEffect.get_Frequency(*args, **kwargs)
 
	def get_index(self, *args, **kwargs):
		return self._TremoloEffect.get_Index(*args, **kwargs)
 
	def get_lfo(self, *args, **kwargs):
		return self._TremoloEffect.get_Lfo(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._TremoloEffect.get_Wet(*args, **kwargs)
 
	def set_depth(self, value):
		return self._TremoloEffect.set_Depth(value)
 
	def set_dry(self, value):
		return self._TremoloEffect.set_Dry(value)
 
	def set_frequency(self, value):
		return self._TremoloEffect.set_Frequency(value)
 
	def set_index(self, value):
		return self._TremoloEffect.set_Index(value)
 
	def set_lfo(self, value):
		return self._TremoloEffect.set_Lfo(value)
 
	def set_wet(self, value):
		return self._TremoloEffect.set_Wet(value)