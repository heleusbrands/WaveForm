from ...wrapper import NWaves 


 

class OlsBlockConvolver64:

	def __init__(self, kernel, fftSize):
		self._OlsBlockConvolver64 = NWaves.Operations.Convolution.OlsBlockConvolver64(kernel, fftSize)
		self.HopSize = self._OlsBlockConvolver64.HopSize
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._OlsBlockConvolver64.ApplyTo(signal, method)
 
	def change_kernel(self, kernel):
		return self._OlsBlockConvolver64.ChangeKernel(kernel)
 
	def equals(self, *args, **kwargs):
		return self._OlsBlockConvolver64.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._OlsBlockConvolver64.Finalize(*args, **kwargs)
 
	def from_filter(self, filter, fftSize):
		return self._OlsBlockConvolver64.FromFilter(filter, fftSize)
 
	def get_hash_code(self, *args, **kwargs):
		return self._OlsBlockConvolver64.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._OlsBlockConvolver64.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._OlsBlockConvolver64.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, kernel, fftSize):
		return self._OlsBlockConvolver64.Overloads(kernel, fftSize)
 
	def process(self, sample):
		return self._OlsBlockConvolver64.Process(sample)
 
	def process_frame(self, *args, **kwargs):
		return self._OlsBlockConvolver64.ProcessFrame(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._OlsBlockConvolver64.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._OlsBlockConvolver64.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._OlsBlockConvolver64.ToString(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._OlsBlockConvolver64.get_HopSize(*args, **kwargs)