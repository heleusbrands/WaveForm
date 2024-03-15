from ..wrapper import NWaves 


 

class SpnccExtractor:

	def __init__(self, options):
		self._SpnccExtractor = NWaves.FeatureExtractors.SpnccExtractor(options)
		self.FilterBank = self._SpnccExtractor.FilterBank
		self.LambdaMu = self._SpnccExtractor.LambdaMu
		self.FeatureDescriptions = self._SpnccExtractor.FeatureDescriptions
 
	def get_feature_descriptions(self, *args, **kwargs):
		return self._SpnccExtractor.get_FeatureDescriptions(self, *args, **kwargs)
 
	def get_lambda_mu(self, *args, **kwargs):
		return self._SpnccExtractor.get_LambdaMu(self, *args, **kwargs)
 
	def set_lambda_mu(self, *args, **kwargs):
		return self._SpnccExtractor.set_LambdaMu(self, *args, **kwargs)
 
	def get_filter_bank(self, *args, **kwargs):
		return self._SpnccExtractor.get_FilterBank(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._SpnccExtractor.ProcessFrame(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._SpnccExtractor.Reset(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._SpnccExtractor.Overloads(self, *args, **kwargs)