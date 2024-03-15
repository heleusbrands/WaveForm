from ..wrapper import NWaves 


 

class Pitch:

	def __init__(self, *args, **kwargs):
		self._Pitch = NWaves.Features.Pitch(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._Pitch.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Pitch.Finalize(*args, **kwargs)
 
	def from_auto_correlation(self, *args, **kwargs):
		return self._Pitch.FromAutoCorrelation(*args, **kwargs)
 
	def from_cepstrum(self, signal, startPos: int=0, endPos: int=-1, low: int=80.0, high: int=400.0, cepstrumSize: int=256, fftSize: int=1024):
		return self._Pitch.FromCepstrum(signal, startPos, endPos, low, high, cepstrumSize, fftSize)
 
	def from_hps(self, *args, **kwargs):
		return self._Pitch.FromHps(*args, **kwargs)
 
	def from_hss(self, *args, **kwargs):
		return self._Pitch.FromHss(*args, **kwargs)
 
	def from_spectral_peaks(self, *args, **kwargs):
		return self._Pitch.FromSpectralPeaks(*args, **kwargs)
 
	def from_yin(self, *args, **kwargs):
		return self._Pitch.FromYin(*args, **kwargs)
 
	def from_zero_crossings_schmitt(self, *args, **kwargs):
		return self._Pitch.FromZeroCrossingsSchmitt(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Pitch.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Pitch.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Pitch.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._Pitch.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._Pitch.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._Pitch.ToString(*args, **kwargs)