from ..wrapper import NWaves 


 

class DistortionEffect:

	def __init__(self, mode, inputGain: int=12.0, outputGain: int=-12.0):
		self._DistortionEffect = NWaves.Effects.DistortionEffect(mode, inputGain, outputGain)
		self.Wet = self._DistortionEffect.Wet
		self.OutputGain = self._DistortionEffect.OutputGain
		self.Mode = self._DistortionEffect.Mode
		self.InputGain = self._DistortionEffect.InputGain
		self.Dry = self._DistortionEffect.Dry
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._DistortionEffect.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._DistortionEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._DistortionEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._DistortionEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._DistortionEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._DistortionEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, mode, inputGain: int=12.0, outputGain: int=-12.0):
		return self._DistortionEffect.Overloads(mode, inputGain, outputGain)
 
	def process(self, sample):
		return self._DistortionEffect.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._DistortionEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._DistortionEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._DistortionEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._DistortionEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._DistortionEffect.WetDryMix(mix, mixingRule)
 
	def get_dry(self, *args, **kwargs):
		return self._DistortionEffect.get_Dry(*args, **kwargs)
 
	def get_input_gain(self, *args, **kwargs):
		return self._DistortionEffect.get_InputGain(*args, **kwargs)
 
	def get_mode(self, *args, **kwargs):
		return self._DistortionEffect.get_Mode(*args, **kwargs)
 
	def get_output_gain(self, *args, **kwargs):
		return self._DistortionEffect.get_OutputGain(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._DistortionEffect.get_Wet(*args, **kwargs)
 
	def set_dry(self, value):
		return self._DistortionEffect.set_Dry(value)
 
	def set_input_gain(self, value):
		return self._DistortionEffect.set_InputGain(value)
 
	def set_mode(self, value):
		return self._DistortionEffect.set_Mode(value)
 
	def set_output_gain(self, value):
		return self._DistortionEffect.set_OutputGain(value)
 
	def set_wet(self, value):
		return self._DistortionEffect.set_Wet(value)