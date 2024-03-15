from ..wrapper import NWaves 


 

class CepstralTransform:

	def __init__(self, c: int, fftSize: int=0, logBase=2.718281828459045):
		self._CepstralTransform = NWaves.Transforms.CepstralTransform(cepstrumSize, fftSize, logBase)
		self.Size = self._CepstralTransform.Size
 
	def complex_cepstrum(self, input, cepstrum, normalize: bool=True):
		return self._CepstralTransform.ComplexCepstrum(input, cepstrum, normalize)
 
	def direct(self, input, output):
		return self._CepstralTransform.Direct(input, output)
 
	def direct_norm(self, input, output):
		return self._CepstralTransform.DirectNorm(input, output)
 
	def equals(self, *args, **kwargs):
		return self._CepstralTransform.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._CepstralTransform.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._CepstralTransform.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._CepstralTransform.GetType(*args, **kwargs)
 
	def inverse(self, input, output):
		return self._CepstralTransform.Inverse(input, output)
 
	def inverse_complex_cepstrum(self, input, cepstrum, normalize: bool=True, delay=0.0):
		return self._CepstralTransform.InverseComplexCepstrum(input, cepstrum, normalize, delay)
 
	def inverse_norm(self, input, output):
		return self._CepstralTransform.InverseNorm(input, output)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._CepstralTransform.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, c: int, fftSize: int=0, logBase=2.718281828459045):
		return self._CepstralTransform.Overloads(cepstrumSize, fftSize, logBase)
 
	def phase_cepstrum(self, input, cepstrum, normalize: bool=True):
		return self._CepstralTransform.PhaseCepstrum(input, cepstrum, normalize)
 
	def power_cepstrum(self, input, cepstrum, normalize: bool=True):
		return self._CepstralTransform.PowerCepstrum(input, cepstrum, normalize)
 
	def real_cepstrum(self, input, cepstrum, normalize: bool=True):
		return self._CepstralTransform.RealCepstrum(input, cepstrum, normalize)
 
	def reference_equals(self, objA, objB):
		return self._CepstralTransform.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._CepstralTransform.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._CepstralTransform.get_Size(*args, **kwargs)