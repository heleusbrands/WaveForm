from ..wrapper import NWaves 


 

class Scale:

	def __init__(self, *args, **kwargs):
		self._Scale = NWaves.Utils.Scale(*args, **kwargs)
 
	def bark_to_herz(self, bark):
		return self._Scale.BarkToHerz(bark)
 
	def bark_to_herz_slaney(self, bark):
		return self._Scale.BarkToHerzSlaney(bark)
 
	def equals(self, *args, **kwargs):
		return self._Scale.Equals(*args, **kwargs)
 
	def erb_to_herz(self, erb):
		return self._Scale.ErbToHerz(erb)
 
	def finalize(self, *args, **kwargs):
		return self._Scale.Finalize(*args, **kwargs)
 
	def freq_to_note(self, freq):
		return self._Scale.FreqToNote(freq)
 
	def freq_to_pitch(self, freq):
		return self._Scale.FreqToPitch(freq)
 
	def from_decibel(self, level, valueReference):
		return self._Scale.FromDecibel(level, valueReference)
 
	def from_decibel_power(self, l: float, valueReference=1.0):
		return self._Scale.FromDecibelPower(level, valueReference)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Scale.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Scale.GetType(*args, **kwargs)
 
	def herz_to_bark(self, herz):
		return self._Scale.HerzToBark(herz)
 
	def herz_to_bark_slaney(self, herz):
		return self._Scale.HerzToBarkSlaney(herz)
 
	def herz_to_erb(self, herz):
		return self._Scale.HerzToErb(herz)
 
	def herz_to_mel(self, herz):
		return self._Scale.HerzToMel(herz)
 
	def herz_to_mel_slaney(self, herz):
		return self._Scale.HerzToMelSlaney(herz)
 
	def herz_to_octave(self, h: float, tuning=0.0, binsPerOctave: int=12):
		return self._Scale.HerzToOctave(herz, tuning, binsPerOctave)
 
	def loudness_weighting(self, frequency, weightingType='A'):
		return self._Scale.LoudnessWeighting(frequency, weightingType)
 
	def mel_to_herz(self, mel):
		return self._Scale.MelToHerz(mel)
 
	def mel_to_herz_slaney(self, mel):
		return self._Scale.MelToHerzSlaney(mel)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Scale.MemberwiseClone(*args, **kwargs)
 
	def note_to_freq(self, note, octave):
		return self._Scale.NoteToFreq(note, octave)
 
	def overloads(self, *args, **kwargs):
		return self._Scale.Overloads(*args, **kwargs)
 
	def pitch_to_freq(self, pitch):
		return self._Scale.PitchToFreq(pitch)
 
	def reference_equals(self, objA, objB):
		return self._Scale.ReferenceEquals(objA, objB)
 
	def to_decibel(self, value, valueReference):
		return self._Scale.ToDecibel(value, valueReference)
 
	def to_decibel_power(self, v: float, v: floatReference=1.0):
		return self._Scale.ToDecibelPower(value, valueReference)
 
	def to_string(self, *args, **kwargs):
		return self._Scale.ToString(*args, **kwargs)