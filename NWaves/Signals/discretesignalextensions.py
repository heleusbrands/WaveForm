from ..wrapper import NWaves 


 

class DiscreteSignalExtensions:

	def __init__(self, *args, **kwargs):
		self._DiscreteSignalExtensions = NWaves.Signals.DiscreteSignalExtensions(*args, **kwargs)
 
	def amplify(self, signal, coeff):
		return self._DiscreteSignalExtensions.Amplify(signal, coeff)
 
	def attenuate(self, signal, coeff):
		return self._DiscreteSignalExtensions.Attenuate(signal, coeff)
 
	def concatenate(self, signal1, signal2):
		return self._DiscreteSignalExtensions.Concatenate(signal1, signal2)
 
	def crossfade(self, signal1, signal2, duration):
		return self._DiscreteSignalExtensions.Crossfade(signal1, signal2, duration)
 
	def delay(self, signal, delay):
		return self._DiscreteSignalExtensions.Delay(signal, delay)
 
	def equals(self, *args, **kwargs):
		return self._DiscreteSignalExtensions.Equals(*args, **kwargs)
 
	def fade_in(self, signal, duration):
		return self._DiscreteSignalExtensions.FadeIn(signal, duration)
 
	def fade_in_fade_out(self, signal, fadeInDuration, fadeOutDuration):
		return self._DiscreteSignalExtensions.FadeInFadeOut(signal, fadeInDuration, fadeOutDuration)
 
	def fade_out(self, signal, duration):
		return self._DiscreteSignalExtensions.FadeOut(signal, duration)
 
	def finalize(self, *args, **kwargs):
		return self._DiscreteSignalExtensions.Finalize(*args, **kwargs)
 
	def first(self, signal, n):
		return self._DiscreteSignalExtensions.First(signal, n)
 
	def full_rectify(self, signal):
		return self._DiscreteSignalExtensions.FullRectify(signal)
 
	def get_hash_code(self, *args, **kwargs):
		return self._DiscreteSignalExtensions.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._DiscreteSignalExtensions.GetType(*args, **kwargs)
 
	def half_rectify(self, signal):
		return self._DiscreteSignalExtensions.HalfRectify(signal)
 
	def last(self, signal, n):
		return self._DiscreteSignalExtensions.Last(signal, n)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._DiscreteSignalExtensions.MemberwiseClone(*args, **kwargs)
 
	def normalize_max(self, signal, bitsPerSample: int=0):
		return self._DiscreteSignalExtensions.NormalizeMax(signal, bitsPerSample)
 
	def overloads(self, *args, **kwargs):
		return self._DiscreteSignalExtensions.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._DiscreteSignalExtensions.ReferenceEquals(objA, objB)
 
	def repeat(self, signal, n):
		return self._DiscreteSignalExtensions.Repeat(signal, n)
 
	def reverse(self, signal):
		return self._DiscreteSignalExtensions.Reverse(signal)
 
	def subtract(self, signal1, signal2):
		return self._DiscreteSignalExtensions.Subtract(signal1, signal2)
 
	def superimpose(self, signal1, signal2):
		return self._DiscreteSignalExtensions.Superimpose(signal1, signal2)
 
	def superimpose_many(self, signal1, signal2, positions):
		return self._DiscreteSignalExtensions.SuperimposeMany(signal1, signal2, positions)
 
	def to_complex(self, signal):
		return self._DiscreteSignalExtensions.ToComplex(signal)
 
	def to_string(self, *args, **kwargs):
		return self._DiscreteSignalExtensions.ToString(*args, **kwargs)