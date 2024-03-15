from ..wrapper import NWaves 


 

class PitchShiftEffect:

	def __init__(self, s: float, windowSize: int=1024, hopSize: int=128, tsm=NWaves.Operations.Tsm.TsmAlgorithm):
		self._PitchShiftEffect = NWaves.Effects.PitchShiftEffect(shift, windowSize, hopSize, tsm)
		self.WindowSize = self._PitchShiftEffect.WindowSize
		self.Wet = self._PitchShiftEffect.Wet
		self.Tsm = self._PitchShiftEffect.Tsm
		self.Shift = self._PitchShiftEffect.Shift
		self.HopSize = self._PitchShiftEffect.HopSize
		self.Dry = self._PitchShiftEffect.Dry
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._PitchShiftEffect.ApplyTo(signal, method)
 
	def equals(self, *args, **kwargs):
		return self._PitchShiftEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._PitchShiftEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._PitchShiftEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._PitchShiftEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._PitchShiftEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, s: float, windowSize: int=1024, hopSize: int=128, tsm=NWaves.Operations.Tsm.TsmAlgorithm):
		return self._PitchShiftEffect.Overloads(shift, windowSize, hopSize, tsm)
 
	def process(self, sample):
		return self._PitchShiftEffect.Process(sample)
 
	def reference_equals(self, objA, objB):
		return self._PitchShiftEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._PitchShiftEffect.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._PitchShiftEffect.ToString(*args, **kwargs)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._PitchShiftEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._PitchShiftEffect.WetDryMix(mix, mixingRule)
 
	def get_dry(self, *args, **kwargs):
		return self._PitchShiftEffect.get_Dry(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._PitchShiftEffect.get_HopSize(*args, **kwargs)
 
	def get_shift(self, *args, **kwargs):
		return self._PitchShiftEffect.get_Shift(*args, **kwargs)
 
	def get_tsm(self, *args, **kwargs):
		return self._PitchShiftEffect.get_Tsm(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._PitchShiftEffect.get_Wet(*args, **kwargs)
 
	def get_window_size(self, *args, **kwargs):
		return self._PitchShiftEffect.get_WindowSize(*args, **kwargs)
 
	def set_dry(self, value):
		return self._PitchShiftEffect.set_Dry(value)
 
	def set_hop_size(self, value):
		return self._PitchShiftEffect.set_HopSize(value)
 
	def set_shift(self, value):
		return self._PitchShiftEffect.set_Shift(value)
 
	def set_tsm(self, value):
		return self._PitchShiftEffect.set_Tsm(value)
 
	def set_wet(self, value):
		return self._PitchShiftEffect.set_Wet(value)
 
	def set_window_size(self, value):
		return self._PitchShiftEffect.set_WindowSize(value)