from ...wrapper import NWaves 


 

class Mci:

	def __init__(self, *args, **kwargs):
		self._Mci = NWaves.Audio.Mci.Mci(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._Mci.Equals(*args, **kwargs)
 
	def execute(self, command):
		return self._Mci.Execute(command)
 
	def finalize(self, *args, **kwargs):
		return self._Mci.Finalize(*args, **kwargs)
 
	def get_error_string(self, dwError, lpstrBuffer, wLength):
		return self._Mci.GetErrorString(dwError, lpstrBuffer, wLength)
 
	def get_hash_code(self, *args, **kwargs):
		return self._Mci.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._Mci.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._Mci.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._Mci.Overloads(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._Mci.ReferenceEquals(objA, objB)
 
	def send_string(self, command, returnValue, returnLength, winHandle):
		return self._Mci.SendString(command, returnValue, returnLength, winHandle)
 
	def to_string(self, *args, **kwargs):
		return self._Mci.ToString(*args, **kwargs)