from ..wrapper import NWaves 


 

class Matrix:

	def __init__(self, r: int, columns: int=0):
		self._Matrix = NWaves.Utils.Matrix(rows, columns)
		self.T = self._Matrix.T
		self.Rows = self._Matrix.Rows
		self.Columns = self._Matrix.Columns
 
	def as2d_array(self, *args, **kwargs):
		return self._Matrix.As2dArray(*args, **kwargs)
 
	def companion(self, a):
		return self._Matrix.Companion(a)
 
	def equals(self, *args, **kwargs):
		return self._Matrix.Equals(*args, **kwargs)
 
	def eye(self, size):
		return self._Matrix.Eye(size)
 
	def finalize(self, *args, **kwargs):
		return self._Matrix.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Matrix.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Matrix.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Matrix.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, r: int, columns: int=0):
		return self._Matrix.Overloads(rows, columns)
 
	def reference_equals(self, objA, objB):
		return self._Matrix.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._Matrix.ToString(*args, **kwargs)
 
	def get_columns(self, *args, **kwargs):
		return self._Matrix.get_Columns(*args, **kwargs)
 
	def get_item(self, i):
		return self._Matrix.get_Item(i)
 
	def get_rows(self, *args, **kwargs):
		return self._Matrix.get_Rows(*args, **kwargs)
 
	def get_t(self, *args, **kwargs):
		return self._Matrix.get_T(*args, **kwargs)
 
	def op_addition(self, m1, m2):
		return self._Matrix.op_Addition(m1, m2)
 
	def op_subtraction(self, m1, m2):
		return self._Matrix.op_Subtraction(m1, m2)
 
	def set_columns(self, value):
		return self._Matrix.set_Columns(value)
 
	def set_rows(self, value):
		return self._Matrix.set_Rows(value)