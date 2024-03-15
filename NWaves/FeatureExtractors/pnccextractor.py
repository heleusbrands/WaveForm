from ..wrapper import NWaves 


 

class PnccExtractor:

	def __init__(self, options):
		self._PnccExtractor = NWaves.FeatureExtractors.PnccExtractor(options)
		self.FilterBank = self._PnccExtractor.FilterBank
		self.MuT = self._PnccExtractor.MuT
		self.C = self._PnccExtractor.C
		self.LambdaMu = self._PnccExtractor.LambdaMu
		self.LambdaT = self._PnccExtractor.LambdaT
		self.LambdaB = self._PnccExtractor.LambdaB
		self.LambdaA = self._PnccExtractor.LambdaA
		self.N = self._PnccExtractor.N
		self.M = self._PnccExtractor.M
		self.FeatureDescriptions = self._PnccExtractor.FeatureDescriptions
 
	def get_feature_descriptions(self, *args, **kwargs):
		return self._PnccExtractor.get_FeatureDescriptions(self, *args, **kwargs)
 
	def get_m(self, *args, **kwargs):
		return self._PnccExtractor.get_M(self, *args, **kwargs)
 
	def set_m(self, *args, **kwargs):
		return self._PnccExtractor.set_M(self, *args, **kwargs)
 
	def get_n(self, *args, **kwargs):
		return self._PnccExtractor.get_N(self, *args, **kwargs)
 
	def set_n(self, *args, **kwargs):
		return self._PnccExtractor.set_N(self, *args, **kwargs)
 
	def get_lambda_a(self, *args, **kwargs):
		return self._PnccExtractor.get_LambdaA(self, *args, **kwargs)
 
	def set_lambda_a(self, *args, **kwargs):
		return self._PnccExtractor.set_LambdaA(self, *args, **kwargs)
 
	def get_lambda_b(self, *args, **kwargs):
		return self._PnccExtractor.get_LambdaB(self, *args, **kwargs)
 
	def set_lambda_b(self, *args, **kwargs):
		return self._PnccExtractor.set_LambdaB(self, *args, **kwargs)
 
	def get_lambda_t(self, *args, **kwargs):
		return self._PnccExtractor.get_LambdaT(self, *args, **kwargs)
 
	def set_lambda_t(self, *args, **kwargs):
		return self._PnccExtractor.set_LambdaT(self, *args, **kwargs)
 
	def get_lambda_mu(self, *args, **kwargs):
		return self._PnccExtractor.get_LambdaMu(self, *args, **kwargs)
 
	def set_lambda_mu(self, *args, **kwargs):
		return self._PnccExtractor.set_LambdaMu(self, *args, **kwargs)
 
	def get_c(self, *args, **kwargs):
		return self._PnccExtractor.get_C(self, *args, **kwargs)
 
	def set_c(self, *args, **kwargs):
		return self._PnccExtractor.set_C(self, *args, **kwargs)
 
	def get_mu_t(self, *args, **kwargs):
		return self._PnccExtractor.get_MuT(self, *args, **kwargs)
 
	def set_mu_t(self, *args, **kwargs):
		return self._PnccExtractor.set_MuT(self, *args, **kwargs)
 
	def get_filter_bank(self, *args, **kwargs):
		return self._PnccExtractor.get_FilterBank(self, *args, **kwargs)
 
	def process_frame(self, *args, **kwargs):
		return self._PnccExtractor.ProcessFrame(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._PnccExtractor.Reset(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PnccExtractor.Overloads(self, *args, **kwargs)