from ...wrapper import NWaves 


 

class ZiFilter:

	def __init__(self, *args, **kwargs):
		self._ZiFilter = NWaves.Filters.Base.ZiFilter(*args, **kwargs)
		self.Tf = self._ZiFilter.Tf
		self.Zi = self._ZiFilter.Zi
 
	def get_zi(self, *args, **kwargs):
		return self._ZiFilter.get_Zi(self, *args, **kwargs)
 
	def get_tf(self, *args, **kwargs):
		return self._ZiFilter.get_Tf(self, *args, **kwargs)
 
	def set_tf(self, *args, **kwargs):
		return self._ZiFilter.set_Tf(self, *args, **kwargs)
 
	def init(self, *args, **kwargs):
		return self._ZiFilter.Init(self, *args, **kwargs)
 
	def process(self, *args, **kwargs):
		return self._ZiFilter.Process(self, *args, **kwargs)
 
	def zero_phase(self, *args, **kwargs):
		return self._ZiFilter.ZeroPhase(self, *args, **kwargs)
 
	def change_numerator_coeffs(self, *args, **kwargs):
		return self._ZiFilter.ChangeNumeratorCoeffs(self, *args, **kwargs)
 
	def change_denominator_coeffs(self, *args, **kwargs):
		return self._ZiFilter.ChangeDenominatorCoeffs(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._ZiFilter.Change(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._ZiFilter.Reset(self, *args, **kwargs)
 
	def apply_to(self, *args, **kwargs):
		return self._ZiFilter.ApplyTo(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._ZiFilter.Overloads(self, *args, **kwargs)