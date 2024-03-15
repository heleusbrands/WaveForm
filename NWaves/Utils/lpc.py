from ..wrapper import NWaves 


 

class Lpc:

	def __init__(self, *args, **kwargs):
		self._Lpc = NWaves.Utils.Lpc(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._Lpc.Equals(*args, **kwargs)
 
	def estimate_order(self, samplingRate):
		return self._Lpc.EstimateOrder(samplingRate)
 
	def finalize(self, *args, **kwargs):
		return self._Lpc.Finalize(*args, **kwargs)
 
	def from_cepstrum(self, lpcc, lpc):
		return self._Lpc.FromCepstrum(lpcc, lpc)
 
	def from_lsf(self, lsf, lpc):
		return self._Lpc.FromLsf(lsf, lpc)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Lpc.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Lpc.GetType(*args, **kwargs)
 
	def levinson_durbin(self, input, a, o: int, offset: int=0):
		return self._Lpc.LevinsonDurbin(input, a, order, offset)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Lpc.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._Lpc.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._Lpc.ReferenceEquals(objA, objB)
 
	def to_cepstrum(self, lpc, gain, lpcc):
		return self._Lpc.ToCepstrum(lpc, gain, lpcc)
 
	def to_lsf(self, lpc, lsf):
		return self._Lpc.ToLsf(lpc, lsf)
 
	def to_string(self, *args, **kwargs):
		return self._Lpc.ToString(*args, **kwargs)