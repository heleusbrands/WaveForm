from ...wrapper import NWaves 


 

class BinauralPanEffect:

	def __init__(self, azimuths, elevations, leftHrirs, rightHrirs):
		self._BinauralPanEffect = NWaves.Effects.Stereo.BinauralPanEffect(azimuths, elevations, leftHrirs, rightHrirs)
		self.Wet = self._BinauralPanEffect.Wet
		self.Elevation = self._BinauralPanEffect.Elevation
		self.Dry = self._BinauralPanEffect.Dry
		self.Azimuth = self._BinauralPanEffect.Azimuth
 
	def apply_to(self, *args, **kwargs):
		return self._BinauralPanEffect.ApplyTo(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._BinauralPanEffect.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._BinauralPanEffect.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._BinauralPanEffect.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._BinauralPanEffect.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._BinauralPanEffect.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, azimuths, elevations, leftHrirs, rightHrirs):
		return self._BinauralPanEffect.Overloads(azimuths, elevations, leftHrirs, rightHrirs)
 
	def process(self, left, right):
		return self._BinauralPanEffect.Process(left, right)
 
	def reference_equals(self, objA, objB):
		return self._BinauralPanEffect.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._BinauralPanEffect.Reset(*args, **kwargs)
 
	def set_crossover_filters(self, lowpassLeft, highpassLeft, lowpassRight, highpassRight):
		return self._BinauralPanEffect.SetCrossoverFilters(lowpassLeft, highpassLeft, lowpassRight, highpassRight)
 
	def set_crossover_parameters(self, freq, samplingRate):
		return self._BinauralPanEffect.SetCrossoverParameters(freq, samplingRate)
 
	def to_string(self, *args, **kwargs):
		return self._BinauralPanEffect.ToString(*args, **kwargs)
 
	def update_hrir(self, azimuth, elevation):
		return self._BinauralPanEffect.UpdateHrir(azimuth, elevation)
 
	def use_crossover(self, useCrossover):
		return self._BinauralPanEffect.UseCrossover(useCrossover)
 
	def wet_dry_db(self, wetDb, dryDb):
		return self._BinauralPanEffect.WetDryDb(wetDb, dryDb)
 
	def wet_dry_mix(self, mix, mixingRule=NWaves.Effects.Base.MixingRule):
		return self._BinauralPanEffect.WetDryMix(mix, mixingRule)
 
	def get_azimuth(self, *args, **kwargs):
		return self._BinauralPanEffect.get_Azimuth(*args, **kwargs)
 
	def get_dry(self, *args, **kwargs):
		return self._BinauralPanEffect.get_Dry(*args, **kwargs)
 
	def get_elevation(self, *args, **kwargs):
		return self._BinauralPanEffect.get_Elevation(*args, **kwargs)
 
	def get_wet(self, *args, **kwargs):
		return self._BinauralPanEffect.get_Wet(*args, **kwargs)
 
	def set_azimuth(self, value):
		return self._BinauralPanEffect.set_Azimuth(value)
 
	def set_dry(self, value):
		return self._BinauralPanEffect.set_Dry(value)
 
	def set_elevation(self, value):
		return self._BinauralPanEffect.set_Elevation(value)
 
	def set_wet(self, value):
		return self._BinauralPanEffect.set_Wet(value)