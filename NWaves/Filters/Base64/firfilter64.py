from ...wrapper import NWaves 


 

class FirFilter64:

	def __init__(self, *args, **kwargs):
		self._FirFilter64 = NWaves.Filters.Base64.FirFilter64(*args, **kwargs)
		self.KernelSizeForBlockConvolution = self._FirFilter64.KernelSizeForBlockConvolution
		self.Tf = self._FirFilter64.Tf
		self.Kernel = self._FirFilter64.Kernel
 
	def get_kernel(self, *args, **kwargs):
		return self._FirFilter64.get_Kernel(self, *args, **kwargs)
 
	def get_tf(self, *args, **kwargs):
		return self._FirFilter64.get_Tf(self, *args, **kwargs)
 
	def set_tf(self, *args, **kwargs):
		return self._FirFilter64.set_Tf(self, *args, **kwargs)
 
	def get_kernel_size_for_block_convolution(self, *args, **kwargs):
		return self._FirFilter64.get_KernelSizeForBlockConvolution(self, *args, **kwargs)
 
	def set_kernel_size_for_block_convolution(self, *args, **kwargs):
		return self._FirFilter64.set_KernelSizeForBlockConvolution(self, *args, **kwargs)
 
	def apply_to(self, *args, **kwargs):
		return self._FirFilter64.ApplyTo(self, *args, **kwargs)
 
	def process(self, *args, **kwargs):
		return self._FirFilter64.Process(self, *args, **kwargs)
 
	def process_all_samples(self, *args, **kwargs):
		return self._FirFilter64.ProcessAllSamples(self, *args, **kwargs)
 
	def change_kernel(self, *args, **kwargs):
		return self._FirFilter64.ChangeKernel(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._FirFilter64.Reset(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._FirFilter64.Overloads(self, *args, **kwargs)