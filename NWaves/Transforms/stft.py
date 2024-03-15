from ..wrapper import NWaves 


 

class Stft:

	def __init__(self, windowSize: int=1024, hopSize: int=256, window=NWaves.Windows.WindowType, fftSize: int=0):
		self._Stft = NWaves.Transforms.Stft(windowSize, hopSize, window, fftSize)
		self.Size = self._Stft.Size
 
	def average_periodogram(self, input):
		return self._Stft.AveragePeriodogram(input)
 
	def direct(self, *args, **kwargs):
		return self._Stft.Direct(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._Stft.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Stft.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Stft.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Stft.GetType(*args, **kwargs)
 
	def inverse(self, stft, perfectReconstruction: bool=True):
		return self._Stft.Inverse(stft, perfectReconstruction)
 
	def magnitude_phase_spectrogram(self, *args, **kwargs):
		return self._Stft.MagnitudePhaseSpectrogram(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Stft.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, windowSize: int=1024, hopSize: int=256, window=NWaves.Windows.WindowType, fftSize: int=0):
		return self._Stft.Overloads(windowSize, hopSize, window, fftSize)
 
	def reconstruct_magnitude_phase(self, spectrogram, perfectReconstruction: bool=True):
		return self._Stft.ReconstructMagnitudePhase(spectrogram, perfectReconstruction)
 
	def reference_equals(self, objA, objB):
		return self._Stft.ReferenceEquals(objA, objB)
 
	def spectrogram(self, *args, **kwargs):
		return self._Stft.Spectrogram(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._Stft.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._Stft.get_Size(*args, **kwargs)