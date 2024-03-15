from ...wrapper import NWaves 


 

class TransferFunction:

	def __init__(self, *args, **kwargs):
		self._TransferFunction = NWaves.Filters.Base.TransferFunction(*args, **kwargs)
		self.Zi = self._TransferFunction.Zi
		self.StateSpace = self._TransferFunction.StateSpace
		self.Gain = self._TransferFunction.Gain
		self.Poles = self._TransferFunction.Poles
		self.Zeros = self._TransferFunction.Zeros
		self.CalculateZpIterations = self._TransferFunction.CalculateZpIterations
		self.Denominator = self._TransferFunction.Denominator
		self.Numerator = self._TransferFunction.Numerator
 
	def get_numerator(self, *args, **kwargs):
		return self._TransferFunction.get_Numerator(self, *args, **kwargs)
 
	def set_numerator(self, *args, **kwargs):
		return self._TransferFunction.set_Numerator(self, *args, **kwargs)
 
	def get_denominator(self, *args, **kwargs):
		return self._TransferFunction.get_Denominator(self, *args, **kwargs)
 
	def set_denominator(self, *args, **kwargs):
		return self._TransferFunction.set_Denominator(self, *args, **kwargs)
 
	def get_calculate_zp_iterations(self, *args, **kwargs):
		return self._TransferFunction.get_CalculateZpIterations(self, *args, **kwargs)
 
	def set_calculate_zp_iterations(self, *args, **kwargs):
		return self._TransferFunction.set_CalculateZpIterations(self, *args, **kwargs)
 
	def get_zeros(self, *args, **kwargs):
		return self._TransferFunction.get_Zeros(self, *args, **kwargs)
 
	def get_poles(self, *args, **kwargs):
		return self._TransferFunction.get_Poles(self, *args, **kwargs)
 
	def get_gain(self, *args, **kwargs):
		return self._TransferFunction.get_Gain(self, *args, **kwargs)
 
	def get_state_space(self, *args, **kwargs):
		return self._TransferFunction.get_StateSpace(self, *args, **kwargs)
 
	def get_zi(self, *args, **kwargs):
		return self._TransferFunction.get_Zi(self, *args, **kwargs)
 
	def impulse_response(self, *args, **kwargs):
		return self._TransferFunction.ImpulseResponse(self, *args, **kwargs)
 
	def frequency_response(self, *args, **kwargs):
		return self._TransferFunction.FrequencyResponse(self, *args, **kwargs)
 
	def group_delay(self, *args, **kwargs):
		return self._TransferFunction.GroupDelay(self, *args, **kwargs)
 
	def phase_delay(self, *args, **kwargs):
		return self._TransferFunction.PhaseDelay(self, *args, **kwargs)
 
	def normalize_at(self, *args, **kwargs):
		return self._TransferFunction.NormalizeAt(self, *args, **kwargs)
 
	def normalize(self, *args, **kwargs):
		return self._TransferFunction.Normalize(self, *args, **kwargs)
 
	def zp_to_tf(self, *args, **kwargs):
		return self._TransferFunction.ZpToTf(self, *args, **kwargs)
 
	def tf_to_zp(self, *args, **kwargs):
		return self._TransferFunction.TfToZp(self, *args, **kwargs)
 
	def op_multiply(self, *args, **kwargs):
		return self._TransferFunction.op_Multiply(self, *args, **kwargs)
 
	def op_addition(self, *args, **kwargs):
		return self._TransferFunction.op_Addition(self, *args, **kwargs)
 
	def from_csv(self, *args, **kwargs):
		return self._TransferFunction.FromCsv(self, *args, **kwargs)
 
	def to_csv(self, *args, **kwargs):
		return self._TransferFunction.ToCsv(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._TransferFunction.Overloads(self, *args, **kwargs)