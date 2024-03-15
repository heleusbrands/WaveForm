from ...wrapper import NWaves 


 

class IirFilter:

	def __init__(self, *args, **kwargs):
		self._IirFilter = NWaves.Filters.Base.IirFilter(*args, **kwargs)
		self.DefaultImpulseResponseLength = self._IirFilter.DefaultImpulseResponseLength
		self.Tf = self._IirFilter.Tf
 
	def get_tf(self, *args, **kwargs):
		return self._IirFilter.get_Tf(self, *args, **kwargs)
 
	def set_tf(self, *args, **kwargs):
		return self._IirFilter.set_Tf(self, *args, **kwargs)
 
	def get_default_impulse_response_length(self, *args, **kwargs):
		return self._IirFilter.get_DefaultImpulseResponseLength(self, *args, **kwargs)
 
	def set_default_impulse_response_length(self, *args, **kwargs):
		return self._IirFilter.set_DefaultImpulseResponseLength(self, *args, **kwargs)
 
	def apply_to(self, *args, **kwargs):
		return self._IirFilter.ApplyTo(self, *args, **kwargs)
 
	def process(self, *args, **kwargs):
		return self._IirFilter.Process(self, *args, **kwargs)
 
	def apply_filter_directly(self, *args, **kwargs):
		return self._IirFilter.ApplyFilterDirectly(self, *args, **kwargs)
 
	def change_numerator_coeffs(self, *args, **kwargs):
		return self._IirFilter.ChangeNumeratorCoeffs(self, *args, **kwargs)
 
	def change_denominator_coeffs(self, *args, **kwargs):
		return self._IirFilter.ChangeDenominatorCoeffs(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._IirFilter.Change(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._IirFilter.Reset(self, *args, **kwargs)
 
	def normalize(self, *args, **kwargs):
		return self._IirFilter.Normalize(self, *args, **kwargs)
 
	def op_multiply(self, *args, **kwargs):
		return self._IirFilter.op_Multiply(self, *args, **kwargs)
 
	def op_addition(self, *args, **kwargs):
		return self._IirFilter.op_Addition(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._IirFilter.Overloads(self, *args, **kwargs)