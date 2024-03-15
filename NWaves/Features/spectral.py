from ..wrapper import NWaves 


 

class Spectral:

	def __init__(self, *args, **kwargs):
		self._Spectral = NWaves.Features.Spectral(*args, **kwargs)
 
	def centroid(self, spectrum, frequencies):
		return self._Spectral.Centroid(spectrum, frequencies)
 
	def contrast(self, *args, **kwargs):
		return self._Spectral.Contrast(*args, **kwargs)
 
	def crest(self, spectrum):
		return self._Spectral.Crest(spectrum)
 
	def decrease(self, spectrum):
		return self._Spectral.Decrease(spectrum)
 
	def entropy(self, spectrum):
		return self._Spectral.Entropy(spectrum)
 
	def equals(self, *args, **kwargs):
		return self._Spectral.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Spectral.Finalize(*args, **kwargs)
 
	def flatness(self, spectrum, minLevel=1.000000013351432e-10):
		return self._Spectral.Flatness(spectrum, minLevel)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Spectral.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Spectral.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Spectral.MemberwiseClone(*args, **kwargs)
 
	def noiseness(self, spectrum, frequencies, noiseFrequency: int=3000.0):
		return self._Spectral.Noiseness(spectrum, frequencies, noiseFrequency)
 
	def overloads(self, *args, **kwargs):
		return self._Spectral.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._Spectral.ReferenceEquals(objA, objB)
 
	def rolloff(self, spectrum, frequencies, rolloffPercent: int=0.8500000238418579):
		return self._Spectral.Rolloff(spectrum, frequencies, rolloffPercent)
 
	def spread(self, spectrum, frequencies):
		return self._Spectral.Spread(spectrum, frequencies)
 
	def to_string(self, *args, **kwargs):
		return self._Spectral.ToString(*args, **kwargs)