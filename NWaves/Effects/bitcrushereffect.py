from ..wrapper import NWaves 


 

class BitCrusherEffect:

	def __init__(self, bitDepth):
		self._BitCrusherEffect = NWaves.Effects.BitCrusherEffect(bitDepth)
		self.Wet = self._BitCrusherEffect.Wet
		self.Dry = self._BitCrusherEffect.Dry
		self.BitDepth = self._BitCrusherEffect.BitDepth
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._BitCrusherEffect.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._BitCrusherEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._BitCrusherEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._BitCrusherEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._BitCrusherEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._BitCrusherEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, bitDepth):
		return self._BitCrusherEffect.Overloads(bitDepth)
 
	def process(self, sample):
		return self._BitCrusherEffect.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._BitCrusherEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._BitCrusherEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._BitCrusherEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._BitCrusherEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._BitCrusherEffect.WetDryMix(mix, mixingRule)
 
	def get_bit_depth(self, *args, **kwargs):
		return self._BitCrusherEffect.get_BitDepth(*args, **kwargs)
 
	def get_dry(self, *args, **kwargs):
		return self._BitCrusherEffect.get_Dry(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._BitCrusherEffect.get_Wet(*args, **kwargs)
 
	def set_bit_depth(self, value):
		return self._BitCrusherEffect.set_BitDepth(value)
 
	def set_dry(self, value):
		return self._BitCrusherEffect.set_Dry(value)
 
	def set_wet(self, value):
		return self._BitCrusherEffect.set_Wet(value)