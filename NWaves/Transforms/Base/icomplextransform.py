from ...wrapper import NWaves 


 

class IComplexTransform:

	def __init__(self, /, *args, **kwargs):
		self._IComplexTransform = NWaves.Transforms.Base.IComplexTransform(self, args, kwargs)
		self.Size = self._IComplexTransform.Size
 
	def direct(self, inRe, inIm, outRe, outIm):
		return self._IComplexTransform.Direct(inRe, inIm, outRe, outIm)
 
	def direct_norm(self, inRe, inIm, outRe, outIm):
		return self._IComplexTransform.DirectNorm(inRe, inIm, outRe, outIm)
 
	def equals(self, obj):
		return self._IComplexTransform.Equals(obj)
 
	def get_hash_code(self, *args, **kwargs):
		return self._IComplexTransform.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._IComplexTransform.GetType(*args, **kwargs)
 
	def inverse(self, inRe, inIm, outRe, outIm):
		return self._IComplexTransform.Inverse(inRe, inIm, outRe, outIm)
 
	def inverse_norm(self, inRe, inIm, outRe, outIm):
		return self._IComplexTransform.InverseNorm(inRe, inIm, outRe, outIm)
 
	def to_string(self, *args, **kwargs):
		return self._IComplexTransform.ToString(*args, **kwargs)
 
	def get_size(self, *args, **kwargs):
		return self._IComplexTransform.get_Size(*args, **kwargs)