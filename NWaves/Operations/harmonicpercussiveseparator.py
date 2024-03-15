from ..wrapper import NWaves 


 

class HarmonicPercussiveSeparator:

	def __init__(self, fftSize: int=2048, hopSize: int=512, harmonicWinSize: int=17, percussiveWinSize: int=17, masking=NWaves.Operations.HpsMasking):
		self._HarmonicPercussiveSeparator = NWaves.Operations.HarmonicPercussiveSeparator(fftSize, hopSize, harmonicWinSize, percussiveWinSize, masking)
 
	def equals(self, *args, **kwargs):
		return self._HarmonicPercussiveSeparator.Equals(*args, **kwargs)
 
	def evaluate_signals(self, signal):
		return self._HarmonicPercussiveSeparator.EvaluateSignals(signal)
 
	def evaluate_spectrograms(self, signal):
		return self._HarmonicPercussiveSeparator.EvaluateSpectrograms(signal)
 
	def finalize(self, *args, **kwargs):
		return self._HarmonicPercussiveSeparator.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._HarmonicPercussiveSeparator.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._HarmonicPercussiveSeparator.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._HarmonicPercussiveSeparator.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, fftSize: int=2048, hopSize: int=512, harmonicWinSize: int=17, percussiveWinSize: int=17, masking=NWaves.Operations.HpsMasking):
		return self._HarmonicPercussiveSeparator.Overloads(fftSize, hopSize, harmonicWinSize, percussiveWinSize, masking)
 
	def reference_equals(self, objA, objB):
		return self._HarmonicPercussiveSeparator.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._HarmonicPercussiveSeparator.ToString(*args, **kwargs)