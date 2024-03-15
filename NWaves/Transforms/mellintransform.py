from ..wrapper import NWaves 


 

class MellinTransform:

	def __init__(self, i: int, s: int, beta=0.5):
		self._MellinTransform = NWaves.Transforms.MellinTransform(inputSize, size, beta)
		self.Size = self._MellinTransform.Size
		self.InputSize = self._MellinTransform.InputSize
 
	def direct(self, *args, **kwargs):
		return self._MellinTransform.Direct(*args, **kwargs)
 
	def direct_norm(self, *args, **kwargs):
		return self._MellinTransform.DirectNorm(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._MellinTransform.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._MellinTransform.Finalize(*args, **kwargs)
 
	def get_hash_code(self, *args, **kwargs):
		return self._MellinTransform.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._MellinTransform.GetType(*args, **kwargs)
 
	def inverse(self, inRe, inIm, outRe, outIm):
		return self._MellinTransform.Inverse(inRe, inIm, outRe, outIm)
 
	def inverse_norm(self, inRe, inIm, outRe, outIm):
		return self._MellinTransform.InverseNorm(inRe, inIm, outRe, outIm)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._MellinTransform.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, i: int, s: int, beta=0.5):
		return self._MellinTransform.Overloads(inputSize, size, beta)
 
	def reference_equals(self, objA, objB):
		return self._MellinTransform.ReferenceEquals(objA, objB)
 
	def to_string(self, *args, **kwargs):
		return self._MellinTransform.ToString(*args, **kwargs)
 
	def get_input_size(self, *args, **kwargs):
		return self._MellinTransform.get_InputSize(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._MellinTransform.get_Size(*args, **kwargs)