from ...wrapper import NWaves 


 

class OlsBlockConvolver:

	def __init__(self, kernel, fftSize):
		self._OlsBlockConvolver = NWaves.Operations.Convolution.OlsBlockConvolver(kernel, fftSize)
		self.HopSize = self._OlsBlockConvolver.HopSize
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._OlsBlockConvolver.ApplyTo(signal, method)
 
	def change_kernel(self, kernel):
		return self._OlsBlockConvolver.ChangeKernel(kernel)
 
	def equals(self, *args, **kwargs):
		return self._OlsBlockConvolver.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._OlsBlockConvolver.Finalize(*args, **kwargs)
 
	def from_filter(self, filter, fftSize):
		return self._OlsBlockConvolver.FromFilter(filter, fftSize)
 
	def get_hash_code(self, *args, **kwargs):
		return self._OlsBlockConvolver.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._OlsBlockConvolver.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._OlsBlockConvolver.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, kernel, fftSize):
		return self._OlsBlockConvolver.Overloads(kernel, fftSize)
 
	def process(self, sample):
		return self._OlsBlockConvolver.Process(sample)
 
	def process_frame(self, *args, **kwargs):
		return self._OlsBlockConvolver.ProcessFrame(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._OlsBlockConvolver.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._OlsBlockConvolver.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._OlsBlockConvolver.ToString(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._OlsBlockConvolver.get_HopSize(*args, **kwargs)