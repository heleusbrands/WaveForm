from ..wrapper import NWaves 


 

class Harmonic:

	def __init__(self, *args, **kwargs):
		self._Harmonic = NWaves.Features.Harmonic(*args, **kwargs)
 
	def centroid(self, spectrum, peaks, peakFrequencies):
		return self._Harmonic.Centroid(spectrum, peaks, peakFrequencies)
 
	def equals(self, *args, **kwargs):
		return self._Harmonic.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Harmonic.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Harmonic.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Harmonic.GetType(*args, **kwargs)
 
	def inharmonicity(self, spectrum, peaks, peakFrequencies):
		return self._Harmonic.Inharmonicity(spectrum, peaks, peakFrequencies)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Harmonic.MemberwiseClone(*args, **kwargs)
 
	def odd_to_even_ratio(self, spectrum, peaks):
		return self._Harmonic.OddToEvenRatio(spectrum, peaks)
 
	def overloads(self, *args, **kwargs):
		return self._Harmonic.Overloads(*args, **kwargs)
 
	def peaks(self, spectrum, peaks, peakFrequencies, s: int, pitch: int=-1.0):
		return self._Harmonic.Peaks(spectrum, peaks, peakFrequencies, samplingRate, pitch)
 
	def reference_equals(self, objA, objB):
		return self._Harmonic.ReferenceEquals(objA, objB)
 
	def spread(self, spectrum, peaks, peakFrequencies):
		return self._Harmonic.Spread(spectrum, peaks, peakFrequencies)
 
	def to_string(self, *args, **kwargs):
		return self._Harmonic.ToString(*args, **kwargs)
 
	def tristimulus(self, spectrum, peaks, n):
		return self._Harmonic.Tristimulus(spectrum, peaks, n)