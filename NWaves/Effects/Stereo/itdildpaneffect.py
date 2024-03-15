from ...wrapper import NWaves 


 

class ItdIldPanEffect:

	def __init__(self, s: int, pan, interpolationMode=NWaves.Utils.InterpolationMode, reserveDelay=0.005, headRadius: int=0.08500000089406967):
		self._ItdIldPanEffect = NWaves.Effects.Stereo.ItdIldPanEffect(samplingRate, pan, interpolationMode, reserveDelay, headRadius)
		self.Wet = self._ItdIldPanEffect.Wet
		self.Pan = self._ItdIldPanEffect.Pan
		self.HeadRadius = self._ItdIldPanEffect.HeadRadius
		self.Dry = self._ItdIldPanEffect.Dry
 
	def apply_to(self, *args, **kwargs):
		return self._ItdIldPanEffect.ApplyTo(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._ItdIldPanEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._ItdIldPanEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._ItdIldPanEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._ItdIldPanEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._ItdIldPanEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, s: int, pan, interpolationMode=NWaves.Utils.InterpolationMode, reserveDelay=0.005, headRadius: int=0.08500000089406967):
		return self._ItdIldPanEffect.Overloads(samplingRate, pan, interpolationMode, reserveDelay, headRadius)
 
	def process(self, left, right):
		return self._ItdIldPanEffect.Process(left, right)
 
	def reference_equals(self, objA, objB):
		return self._ItdIldPanEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._ItdIldPanEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._ItdIldPanEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._ItdIldPanEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._ItdIldPanEffect.WetDryMix(mix, mixingRule)
 
	def get_dry(self, *args, **kwargs):
		return self._ItdIldPanEffect.get_Dry(*args, **kwargs)
 
	def get_head_radius(self, *args, **kwargs):
		return self._ItdIldPanEffect.get_HeadRadius(*args, **kwargs)
 
	def get_pan(self, *args, **kwargs):
		return self._ItdIldPanEffect.get_Pan(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._ItdIldPanEffect.get_Wet(*args, **kwargs)
 
	def set_dry(self, value):
		return self._ItdIldPanEffect.set_Dry(value)
 
	def set_pan(self, value):
		return self._ItdIldPanEffect.set_Pan(value)
 
	def set_wet(self, value):
		return self._ItdIldPanEffect.set_Wet(value)