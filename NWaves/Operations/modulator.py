from ..wrapper import NWaves 


 

class Modulator:

	def __init__(self, *args, **kwargs):
		self._Modulator = NWaves.Operations.Modulator(*args, **kwargs)
 
	def amplitude(self, carrier, modulatorFrequency: int=20.0, modulationIndex: int=0.5):
		return self._Modulator.Amplitude(carrier, modulatorFrequency, modulationIndex)
 
	def demodulate_amplitude(self, signal):
		return self._Modulator.DemodulateAmplitude(signal)
 
	def demodulate_frequency(self, signal):
		return self._Modulator.DemodulateFrequency(signal)
 
	def equals(self, *args, **kwargs):
		return self._Modulator.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Modulator.Finalize(*args, **kwargs)
 
	def frequency(self, baseband, carrierAmplitude, carrierFrequency, deviation: int=0.10000000149011612):
		return self._Modulator.Frequency(baseband, carrierAmplitude, carrierFrequency, deviation)
 
	def frequency_linear(self, carrierFrequency, carrierAmplitude, modulationIndex, l: int, samplingRate: int=1):
		return self._Modulator.FrequencyLinear(carrierFrequency, carrierAmplitude, modulationIndex, length, samplingRate)
 
	def frequency_sinusoidal(self, carrierFrequency, carrierAmplitude, modulatorFrequency, modulationIndex, l: int, samplingRate: int=1):
		return self._Modulator.FrequencySinusoidal(carrierFrequency, carrierAmplitude, modulatorFrequency, modulationIndex, length, samplingRate)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Modulator.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Modulator.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Modulator.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._Modulator.Overloads(*args, **kwargs)
 
	def phase(self, baseband, carrierAmplitude, carrierFrequency, deviation: int=0.800000011920929):
		return self._Modulator.Phase(baseband, carrierAmplitude, carrierFrequency, deviation)
 
	def reference_equals(self, objA, objB):
		return self._Modulator.ReferenceEquals(objA, objB)
 
	def ring(self, carrier, modulator):
		return self._Modulator.Ring(carrier, modulator)
 
	def to_string(self, *args, **kwargs):
		return self._Modulator.ToString(*args, **kwargs)