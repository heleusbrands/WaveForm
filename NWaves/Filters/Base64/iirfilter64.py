from ...wrapper import NWaves 


 

class IirFilter64:

	def __init__(self, *args, **kwargs):
		self._IirFilter64 = NWaves.Filters.Base64.IirFilter64(*args, **kwargs)
		self.DefaultImpulseResponseLength = self._IirFilter64.DefaultImpulseResponseLength
		self.Tf = self._IirFilter64.Tf
 
	def get_tf(self, *args, **kwargs):
		return self._IirFilter64.get_Tf(self, *args, **kwargs)
 
	def set_tf(self, *args, **kwargs):
		return self._IirFilter64.set_Tf(self, *args, **kwargs)
 
	def get_default_impulse_response_length(self, *args, **kwargs):
		return self._IirFilter64.get_DefaultImpulseResponseLength(self, *args, **kwargs)
 
	def set_default_impulse_response_length(self, *args, **kwargs):
		return self._IirFilter64.set_DefaultImpulseResponseLength(self, *args, **kwargs)
 
	def apply_to(self, *args, **kwargs):
		return self._IirFilter64.ApplyTo(self, *args, **kwargs)
 
	def process(self, *args, **kwargs):
		return self._IirFilter64.Process(self, *args, **kwargs)
 
	def change_numerator_coeffs(self, *args, **kwargs):
		return self._IirFilter64.ChangeNumeratorCoeffs(self, *args, **kwargs)
 
	def change_denominator_coeffs(self, *args, **kwargs):
		return self._IirFilter64.ChangeDenominatorCoeffs(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._IirFilter64.Reset(self, *args, **kwargs)
 
	def normalize(self, *args, **kwargs):
		return self._IirFilter64.Normalize(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._IirFilter64.Overloads(self, *args, **kwargs)