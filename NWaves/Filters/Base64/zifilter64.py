from ...wrapper import NWaves 


 

class ZiFilter64:

	def __init__(self, *args, **kwargs):
		self._ZiFilter64 = NWaves.Filters.Base64.ZiFilter64(*args, **kwargs)
		self.Tf = self._ZiFilter64.Tf
		self.Zi = self._ZiFilter64.Zi
 
	def get_zi(self, *args, **kwargs):
		return self._ZiFilter64.get_Zi(self, *args, **kwargs)
 
	def get_tf(self, *args, **kwargs):
		return self._ZiFilter64.get_Tf(self, *args, **kwargs)
 
	def set_tf(self, *args, **kwargs):
		return self._ZiFilter64.set_Tf(self, *args, **kwargs)
 
	def init(self, *args, **kwargs):
		return self._ZiFilter64.Init(self, *args, **kwargs)
 
	def process(self, *args, **kwargs):
		return self._ZiFilter64.Process(self, *args, **kwargs)
 
	def zero_phase(self, *args, **kwargs):
		return self._ZiFilter64.ZeroPhase(self, *args, **kwargs)
 
	def change_numerator_coeffs(self, *args, **kwargs):
		return self._ZiFilter64.ChangeNumeratorCoeffs(self, *args, **kwargs)
 
	def change_denominator_coeffs(self, *args, **kwargs):
		return self._ZiFilter64.ChangeDenominatorCoeffs(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._ZiFilter64.Change(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._ZiFilter64.Reset(self, *args, **kwargs)
 
	def apply_to(self, *args, **kwargs):
		return self._ZiFilter64.ApplyTo(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._ZiFilter64.Overloads(self, *args, **kwargs)