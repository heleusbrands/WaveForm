from ...wrapper import NWaves 


 

class Wavelet:

	def __init__(self, *args, **kwargs):
		self._Wavelet = NWaves.Transforms.Wavelets.Wavelet(*args, **kwargs)
		self.Name = self._Wavelet.Name
		self.LoR = self._Wavelet.LoR
		self.LoD = self._Wavelet.LoD
		self.Length = self._Wavelet.Length
		self.HiR = self._Wavelet.HiR
		self.HiD = self._Wavelet.HiD
 
	def compute_orthonormal_coeffs(self, *args, **kwargs):
		return self._Wavelet.ComputeOrthonormalCoeffs(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._Wavelet.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._Wavelet.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Wavelet.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Wavelet.GetType(*args, **kwargs)
 
	def make_coiflet_wavelet(self, taps):
		return self._Wavelet.MakeCoifletWavelet(taps)
 
	def make_daubechies_wavelet(self, taps):
		return self._Wavelet.MakeDaubechiesWavelet(taps)
 
	def make_haar_wavelet(self, *args, **kwargs):
		return self._Wavelet.MakeHaarWavelet(*args, **kwargs)
 
	def make_symlet_wavelet(self, taps):
		return self._Wavelet.MakeSymletWavelet(taps)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Wavelet.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._Wavelet.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._Wavelet.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._Wavelet.ToString(*args, **kwargs)
 
	def get_hi_d(self, *args, **kwargs):
		return self._Wavelet.get_HiD(*args, **kwargs)
 
	def get_hi_r(self, *args, **kwargs):
		return self._Wavelet.get_HiR(*args, **kwargs)
 
	def get_length(self, *args, **kwargs):
		return self._Wavelet.get_Length(*args, **kwargs)
 
	def get_lo_d(self, *args, **kwargs):
		return self._Wavelet.get_LoD(*args, **kwargs)
 
	def get_lo_r(self, *args, **kwargs):
		return self._Wavelet.get_LoR(*args, **kwargs)
 
	def get_name(self, *args, **kwargs):
		return self._Wavelet.get_Name(*args, **kwargs)
 
	def set_hi_d(self, value):
		return self._Wavelet.set_HiD(value)
 
	def set_hi_r(self, value):
		return self._Wavelet.set_HiR(value)
 
	def set_length(self, value):
		return self._Wavelet.set_Length(value)
 
	def set_lo_d(self, value):
		return self._Wavelet.set_LoD(value)
 
	def set_lo_r(self, value):
		return self._Wavelet.set_LoR(value)
 
	def set_name(self, value):
		return self._Wavelet.set_Name(value)