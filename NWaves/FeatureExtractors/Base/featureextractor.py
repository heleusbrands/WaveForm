from ...wrapper import NWaves 


 

class FeatureExtractor:

	def __init__(self, options):
		self._FeatureExtractor = NWaves.FeatureExtractors.Base.FeatureExtractor(options)
		self.SamplingRate = self._FeatureExtractor.SamplingRate
		self.HopSize = self._FeatureExtractor.HopSize
		self.FrameSize = self._FeatureExtractor.FrameSize
		self.HopDuration = self._FeatureExtractor.HopDuration
		self.FrameDuration = self._FeatureExtractor.FrameDuration
		self.DeltaDeltaFeatureDescriptions = self._FeatureExtractor.DeltaDeltaFeatureDescriptions
		self.DeltaFeatureDescriptions = self._FeatureExtractor.DeltaFeatureDescriptions
		self.FeatureDescriptions = self._FeatureExtractor.FeatureDescriptions
		self.FeatureCount = self._FeatureExtractor.FeatureCount
 
	def get_feature_count(self, *args, **kwargs):
		return self._FeatureExtractor.get_FeatureCount(self, *args, **kwargs)
 
	def set_feature_count(self, *args, **kwargs):
		return self._FeatureExtractor.set_FeatureCount(self, *args, **kwargs)
 
	def get_feature_descriptions(self, *args, **kwargs):
		return self._FeatureExtractor.get_FeatureDescriptions(self, *args, **kwargs)
 
	def get_delta_feature_descriptions(self, *args, **kwargs):
		return self._FeatureExtractor.get_DeltaFeatureDescriptions(self, *args, **kwargs)
 
	def get_delta_delta_feature_descriptions(self, *args, **kwargs):
		return self._FeatureExtractor.get_DeltaDeltaFeatureDescriptions(self, *args, **kwargs)
 
	def get_frame_duration(self, *args, **kwargs):
		return self._FeatureExtractor.get_FrameDuration(self, *args, **kwargs)
 
	def set_frame_duration(self, *args, **kwargs):
		return self._FeatureExtractor.set_FrameDuration(self, *args, **kwargs)
 
	def get_hop_duration(self, *args, **kwargs):
		return self._FeatureExtractor.get_HopDuration(self, *args, **kwargs)
 
	def set_hop_duration(self, *args, **kwargs):
		return self._FeatureExtractor.set_HopDuration(self, *args, **kwargs)
 
	def get_frame_size(self, *args, **kwargs):
		return self._FeatureExtractor.get_FrameSize(self, *args, **kwargs)
 
	def set_frame_size(self, *args, **kwargs):
		return self._FeatureExtractor.set_FrameSize(self, *args, **kwargs)
 
	def get_hop_size(self, *args, **kwargs):
		return self._FeatureExtractor.get_HopSize(self, *args, **kwargs)
 
	def set_hop_size(self, *args, **kwargs):
		return self._FeatureExtractor.set_HopSize(self, *args, **kwargs)
 
	def get_sampling_rate(self, *args, **kwargs):
		return self._FeatureExtractor.get_SamplingRate(self, *args, **kwargs)
 
	def set_sampling_rate(self, *args, **kwargs):
		return self._FeatureExtractor.set_SamplingRate(self, *args, **kwargs)
 
	def compute_from(self, *args, **kwargs):
		return self._FeatureExtractor.ComputeFrom(self, *args, **kwargs)
 
	def time_markers(self, *args, **kwargs):
		return self._FeatureExtractor.TimeMarkers(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._FeatureExtractor.ProcessFrame(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._FeatureExtractor.Reset(self, *args, **kwargs)
 
	def is_parallelizable(self, *args, **kwargs):
		return self._FeatureExtractor.IsParallelizable(self, *args, **kwargs)
 
	def parallel_copy(self, *args, **kwargs):
		return self._FeatureExtractor.ParallelCopy(self, *args, **kwargs)
 
	def parallel_chunks_compute_from(self, *args, **kwargs):
		return self._FeatureExtractor.ParallelChunksComputeFrom(self, *args, **kwargs)
 
	def parallel_compute_from(self, *args, **kwargs):
		return self._FeatureExtractor.ParallelComputeFrom(self, *args, **kwargs)