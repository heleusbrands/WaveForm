from ...wrapper import NWaves 


 

class FirFilter:

	def __init__(self, *args, **kwargs):
		self._FirFilter = NWaves.Filters.Base.FirFilter(*args, **kwargs)
		self.KernelSizeForBlockConvolution = self._FirFilter.KernelSizeForBlockConvolution
		self.Tf = self._FirFilter.Tf
		self.Kernel = self._FirFilter.Kernel
 
	def get_kernel(self, *args, **kwargs):
		return self._FirFilter.get_Kernel(self, *args, **kwargs)
 
	def get_tf(self, *args, **kwargs):
		return self._FirFilter.get_Tf(self, *args, **kwargs)
 
	def set_tf(self, *args, **kwargs):
		return self._FirFilter.set_Tf(self, *args, **kwargs)
 
	def get_kernel_size_for_block_convolution(self, *args, **kwargs):
		return self._FirFilter.get_KernelSizeForBlockConvolution(self, *args, **kwargs)
 
	def set_kernel_size_for_block_convolution(self, *args, **kwargs):
		return self._FirFilter.set_KernelSizeForBlockConvolution(self, *args, **kwargs)
 
	def apply_to(self, *args, **kwargs):
		return self._FirFilter.ApplyTo(self, *args, **kwargs)
 
	def process(self, *args, **kwargs):
		return self._FirFilter.Process(self, *args, **kwargs)
 
	def process_all_samples(self, *args, **kwargs):
		return self._FirFilter.ProcessAllSamples(self, *args, **kwargs)
 
	def apply_filter_directly(self, *args, **kwargs):
		return self._FirFilter.ApplyFilterDirectly(self, *args, **kwargs)
 
	def change_kernel(self, *args, **kwargs):
		return self._FirFilter.ChangeKernel(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._FirFilter.Reset(self, *args, **kwargs)
 
	def op_multiply(self, *args, **kwargs):
		return self._FirFilter.op_Multiply(self, *args, **kwargs)
 
	def op_addition(self, *args, **kwargs):
		return self._FirFilter.op_Addition(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._FirFilter.Overloads(self, *args, **kwargs)