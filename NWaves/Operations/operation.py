from ..wrapper import NWaves 


 

class Operation:

	def __init__(self, *args, **kwargs):
		self._Operation = NWaves.Operations.Operation(*args, **kwargs)
 
	def block_convolve(self, signal, kernel, f: int, method=NWaves.Filters.Base.FilteringMethod):
		return self._Operation.BlockConvolve(signal, kernel, fftSize, method)
 
	def change_peak(self, *args, **kwargs):
		return self._Operation.ChangePeak(*args, **kwargs)
 
	def change_rms(self, *args, **kwargs):
		return self._Operation.ChangeRms(*args, **kwargs)
 
	def convolve(self, signal, kernel):
		return self._Operation.Convolve(signal, kernel)
 
	def cross_correlate(self, signal1, signal2):
		return self._Operation.CrossCorrelate(signal1, signal2)
 
	def decimate(self, signal, factor, filter=None):
		return self._Operation.Decimate(signal, factor, filter)
 
	def deconvolve(self, signal, kernel):
		return self._Operation.Deconvolve(signal, kernel)
 
	def envelope(self, signal, attackTime: int=0.009999999776482582, releaseTime: int=0.05000000074505806):
		return self._Operation.Envelope(signal, attackTime, releaseTime)
 
	def equals(self, *args, **kwargs):
		return self._Operation.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Operation.Finalize(*args, **kwargs)
 
	def full_rectify(self, signal):
		return self._Operation.FullRectify(signal)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Operation.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Operation.GetType(*args, **kwargs)
 
	def half_rectify(self, signal):
		return self._Operation.HalfRectify(signal)
 
	def interpolate(self, signal, factor, filter=None):
		return self._Operation.Interpolate(signal, factor, filter)
 
	def lomb_scargle(self, x, y, freqs, subtractMean: bool=False, normalize: bool=False):
		return self._Operation.LombScargle(x, y, freqs, subtractMean, normalize)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Operation.MemberwiseClone(*args, **kwargs)
 
	def normalize_peak(self, *args, **kwargs):
		return self._Operation.NormalizePeak(*args, **kwargs)
 
	def normalize_rms(self, *args, **kwargs):
		return self._Operation.NormalizeRms(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._Operation.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._Operation.ReferenceEquals(objA, objB)
 
	def resample(self, signal, n: int, filter=None, order: int=15):
		return self._Operation.Resample(signal, newSamplingRate, filter, order)
 
	def resample_up_down(self, signal, up, down, filter=None):
		return self._Operation.ResampleUpDown(signal, up, down, filter)
 
	def spectral_subtract(self, signal, noise, fftSize: int=1024, hopSize: int=256):
		return self._Operation.SpectralSubtract(signal, noise, fftSize, hopSize)
 
	def time_stretch(self, *args, **kwargs):
		return self._Operation.TimeStretch(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._Operation.ToString(*args, **kwargs)
 
	def welch(self, signal, windowSize: int=1024, hopSize: int=256, window=NWaves.Windows.WindowType, fftSize: int=0, samplingRate: int=0):
		return self._Operation.Welch(signal, windowSize, hopSize, window, fftSize, samplingRate)