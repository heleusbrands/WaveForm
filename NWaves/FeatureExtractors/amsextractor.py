from ..wrapper import NWaves 


 

class AmsExtractor:

	def __init__(self, options):
		self._AmsExtractor = NWaves.FeatureExtractors.AmsExtractor(options)
		self.Envelopes = self._AmsExtractor.Envelopes
		self.Filterbank = self._AmsExtractor.Filterbank
		self.FeatureDescriptions = self._AmsExtractor.FeatureDescriptions
 
	def get_feature_descriptions(self, *args, **kwargs):
		return self._AmsExtractor.get_FeatureDescriptions(self, *args, **kwargs)
 
	def get_filterbank(self, *args, **kwargs):
		return self._AmsExtractor.get_Filterbank(self, *args, **kwargs)
 
	def get_envelopes(self, *args, **kwargs):
		return self._AmsExtractor.get_Envelopes(self, *args, **kwargs)
 
	def compute_from(self, *args, **kwargs):
		return self._AmsExtractor.ComputeFrom(self, *args, **kwargs)
 
	def make_spectrum2_d(self, *args, **kwargs):
		return self._AmsExtractor.MakeSpectrum2D(self, *args, **kwargs)
 
	def vectors_at_herz(self, *args, **kwargs):
		return self._AmsExtractor.VectorsAtHerz(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._AmsExtractor.ProcessFrame(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._AmsExtractor.Overloads(self, *args, **kwargs)