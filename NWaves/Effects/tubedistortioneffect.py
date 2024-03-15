from ..wrapper import NWaves 


 

class TubeDistortionEffect:

	def __init__(self, inputGain: int=20.0, outputGain: int=-12.0, q: int=-0.20000000298023224, dist: int=5.0, rh: int=0.9950000047683716, rl: int=0.5):
		self._TubeDistortionEffect = NWaves.Effects.TubeDistortionEffect(inputGain, outputGain, q, dist, rh, rl)
		self.Wet = self._TubeDistortionEffect.Wet
		self.Rl = self._TubeDistortionEffect.Rl
		self.Rh = self._TubeDistortionEffect.Rh
		self.Q = self._TubeDistortionEffect.Q
		self.OutputGain = self._TubeDistortionEffect.OutputGain
		self.InputGain = self._TubeDistortionEffect.InputGain
		self.Dry = self._TubeDistortionEffect.Dry
		self.Dist = self._TubeDistortionEffect.Dist
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._TubeDistortionEffect.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._TubeDistortionEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._TubeDistortionEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._TubeDistortionEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._TubeDistortionEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._TubeDistortionEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, inputGain: int=20.0, outputGain: int=-12.0, q: int=-0.20000000298023224, dist: int=5.0, rh: int=0.9950000047683716, rl: int=0.5):
		return self._TubeDistortionEffect.Overloads(inputGain, outputGain, q, dist, rh, rl)
 
	def process(self, sample):
		return self._TubeDistortionEffect.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._TubeDistortionEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._TubeDistortionEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._TubeDistortionEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._TubeDistortionEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._TubeDistortionEffect.WetDryMix(mix, mixingRule)
 
	def get_dist(self, *args, **kwargs):
		return self._TubeDistortionEffect.get_Dist(*args, **kwargs)
 
	def get_dry(self, *args, **kwargs):
		return self._TubeDistortionEffect.get_Dry(*args, **kwargs)
 
	def get_input_gain(self, *args, **kwargs):
		return self._TubeDistortionEffect.get_InputGain(*args, **kwargs)
 
	def get_output_gain(self, *args, **kwargs):
		return self._TubeDistortionEffect.get_OutputGain(*args, **kwargs)
 
	def get_q(self, *args, **kwargs):
		return self._TubeDistortionEffect.get_Q(*args, **kwargs)
 
	def get_rh(self, *args, **kwargs):
		return self._TubeDistortionEffect.get_Rh(*args, **kwargs)
 
	def get_rl(self, *args, **kwargs):
		return self._TubeDistortionEffect.get_Rl(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._TubeDistortionEffect.get_Wet(*args, **kwargs)
 
	def set_dist(self, value):
		return self._TubeDistortionEffect.set_Dist(value)
 
	def set_dry(self, value):
		return self._TubeDistortionEffect.set_Dry(value)
 
	def set_input_gain(self, value):
		return self._TubeDistortionEffect.set_InputGain(value)
 
	def set_output_gain(self, value):
		return self._TubeDistortionEffect.set_OutputGain(value)
 
	def set_q(self, value):
		return self._TubeDistortionEffect.set_Q(value)
 
	def set_wet(self, value):
		return self._TubeDistortionEffect.set_Wet(value)