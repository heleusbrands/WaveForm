from ...wrapper import NWaves 


 

class OlaBlockConvolver:

	def __init__(self, kernel, fftSize):
		self._OlaBlockConvolver = NWaves.Operations.Convolution.OlaBlockConvolver(kernel, fftSize)
		self.HopSize = self._OlaBlockConvolver.HopSize
 
	def apply_to(self, signal, method=NWaves.Filters.Base.FilteringMethod):
		return self._OlaBlockConvolver.ApplyTo(signal, method)
 
	def change_kernel(self, kernel):
		return self._OlaBlockConvolver.ChangeKernel(kernel)
 
	def equals(self, *args, **kwargs):
		return self._OlaBlockConvolver.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._OlaBlockConvolver.Finalize(*args, **kwargs)
 
	def from_filter(self, filter, fftSize):
		return self._OlaBlockConvolver.FromFilter(filter, fftSize)
 
	def get_hash_code(self, *args, **kwargs):
		return self._OlaBlockConvolver.GetHashCode(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._OlaBlockConvolver.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._OlaBlockConvolver.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, kernel, fftSize):
		return self._OlaBlockConvolver.Overloads(kernel, fftSize)
 
	def process(self, sample):
		return self._OlaBlockConvolver.Process(sample)
 
	def process_frame(self, *args, **kwargs):
		return self._OlaBlockConvolver.ProcessFrame(*args, **kwargs)
 
	def reference_equals(self, objA, objB):
		return self._OlaBlockConvolver.ReferenceEquals(objA, objB)
 
	def reset(self, *args, **kwargs):
		return self._OlaBlockConvolver.Reset(*args, **kwargs)
 
	def to_string(self, *args, **kwargs):
		return self._OlaBlockConvolver.ToString(*args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._OlaBlockConvolver.get_HopSize(*args, **kwargs)