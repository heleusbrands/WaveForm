from ...wrapper import NWaves 


 

class FilterBanks:

	def __init__(self, *args, **kwargs):
		self._FilterBanks = NWaves.Filters.Fda.FilterBanks(*args, **kwargs)
 
	def apply(self, *args, **kwargs):
		return self._FilterBanks.Apply(*args, **kwargs)
 
	def apply_and_log(self, filterbank, spectrum, filtered, floor=1.401298464324817e-45):
		return self._FilterBanks.ApplyAndLog(filterbank, spectrum, filtered, floor)
 
	def apply_and_log10(self, filterbank, spectrum, filtered, floor=1.401298464324817e-45):
		return self._FilterBanks.ApplyAndLog10(filterbank, spectrum, filtered, floor)
 
	def apply_and_pow(self, filterbank, spectrum, filtered, power=0.3333333333333333):
		return self._FilterBanks.ApplyAndPow(filterbank, spectrum, filtered, power)
 
	def apply_and_to_decibel(self, filterbank, spectrum, filtered, minLevel=1.000000013351432e-10):
		return self._FilterBanks.ApplyAndToDecibel(filterbank, spectrum, filtered, minLevel)
 
	def bark_bands(self, b: int, s: int, lowFreq=0.0, highFreq=0.0, overlap: bool=True):
		return self._FilterBanks.BarkBands(barkFilterCount, samplingRate, lowFreq, highFreq, overlap)
 
	def bark_bands_slaney(self, b: int, s: int, lowFreq=0.0, highFreq=0.0, overlap: bool=True):
		return self._FilterBanks.BarkBandsSlaney(barkFilterCount, samplingRate, lowFreq, highFreq, overlap)
 
	def bark_bank_slaney(self, f: int, f: int, s: int, lowFreq=0.0, highFreq=0.0, width=1.0):
		return self._FilterBanks.BarkBankSlaney(filterCount, fftSize, samplingRate, lowFreq, highFreq, width)
 
	def bi_quad(self, fftSize, samplingRate, frequencies):
		return self._FilterBanks.BiQuad(fftSize, samplingRate, frequencies)
 
	def chroma(self, f: int, s: int, chromaCount: int=12, tuning=0.0, centerOctave=5.0, octaveWidth=2.0, norm: int=2, baseC: bool=True):
		return self._FilterBanks.Chroma(fftSize, samplingRate, chromaCount, tuning, centerOctave, octaveWidth, norm, baseC)
 
	def critical_bands(self, f: int, s: int, lowFreq=0.0, highFreq=0.0):
		return self._FilterBanks.CriticalBands(filterCount, samplingRate, lowFreq, highFreq)
 
	def equals(self, *args, **kwargs):
		return self._FilterBanks.Equals(*args, **kwargs)
 
	def erb(self, e: int, f: int, s: int, lowFreq=0.0, highFreq=0.0, normalizeGain: bool=True):
		return self._FilterBanks.Erb(erbFilterCount, fftSize, samplingRate, lowFreq, highFreq, normalizeGain)
 
	def finalize(self, *args, **kwargs):
		return self._FilterBanks.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._FilterBanks.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._FilterBanks.GetType(*args, **kwargs)
 
	def herz_bands(self, c: int, s: int, lowFreq=0.0, highFreq=0.0, overlap: bool=False):
		return self._FilterBanks.HerzBands(combFilterCount, samplingRate, lowFreq, highFreq, overlap)
 
	def mel_bands(self, m: int, s: int, lowFreq=0.0, highFreq=0.0, overlap: bool=True):
		return self._FilterBanks.MelBands(melFilterCount, samplingRate, lowFreq, highFreq, overlap)
 
	def mel_bands_slaney(self, m: int, s: int, lowFreq=0.0, highFreq=0.0, overlap: bool=True):
		return self._FilterBanks.MelBandsSlaney(melFilterCount, samplingRate, lowFreq, highFreq, overlap)
 
	def mel_bank_slaney(self, f: int, f: int, s: int, lowFreq=0.0, highFreq=0.0, normalizeGain: bool=True, vtln=None):
		return self._FilterBanks.MelBankSlaney(filterCount, fftSize, samplingRate, lowFreq, highFreq, normalizeGain, vtln)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._FilterBanks.MemberwiseClone(*args, **kwargs)
 
	def normalize(self, filterCount, frequencies, filterBank):
		return self._FilterBanks.Normalize(filterCount, frequencies, filterBank)
 
	def octave_bands(self, o: int, s: int, lowFreq=0.0, highFreq=0.0, overlap: bool=False):
		return self._FilterBanks.OctaveBands(octaveCount, samplingRate, lowFreq, highFreq, overlap)
 
	def overloads(self, *args, **kwargs):
		return self._FilterBanks.Overloads(*args, **kwargs)
 
	def rectangular(self, fftSize, samplingRate, frequencies, vtln=None, mapper=None):
		return self._FilterBanks.Rectangular(fftSize, samplingRate, frequencies, vtln, mapper)
 
	def reference_equals(self, objA, objB):
		return self._FilterBanks.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._FilterBanks.ToString(*args, **kwargs)
 
	def trapezoidal(self, fftSize, samplingRate, frequencies, vtln=None, mapper=None):
		return self._FilterBanks.Trapezoidal(fftSize, samplingRate, frequencies, vtln, mapper)
 
	def triangular(self, fftSize, samplingRate, frequencies, vtln=None, mapper=None):
		return self._FilterBanks.Triangular(fftSize, samplingRate, frequencies, vtln, mapper)