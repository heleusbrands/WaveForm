from ..wrapper import NWaves 


 

class MorphEffect:

	def __init__(self, h: int, fftSize: int=0):
		self._MorphEffect = NWaves.Effects.MorphEffect(hopSize, fftSize)
		self.Wet = self._MorphEffect.Wet
		self.Dry = self._MorphEffect.Dry
 
	def apply_to(self, signal, mix):
		return self._MorphEffect.ApplyTo(signal, mix)
 
	def equals(self, *args, **kwargs):
		return self._MorphEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._MorphEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._MorphEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._MorphEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._MorphEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, h: int, fftSize: int=0):
		return self._MorphEffect.Overloads(hopSize, fftSize)
 
	def process(self, sample, mix):
		return self._MorphEffect.Process(sample, mix)
 
	def process_frame(self, *args, **kwargs):
		return self._MorphEffect.ProcessFrame(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._MorphEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._MorphEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._MorphEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._MorphEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._MorphEffect.WetDryMix(mix, mixingRule)
 
	def get_dry(self, *args, **kwargs):
		return self._MorphEffect.get_Dry(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._MorphEffect.get_Wet(*args, **kwargs)
 
	def set_dry(self, value):
		return self._MorphEffect.set_Dry(value)
 
	def set_wet(self, value):
		return self._MorphEffect.set_Wet(value)