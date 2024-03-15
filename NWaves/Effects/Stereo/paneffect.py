from ...wrapper import NWaves 


 

class PanEffect:

	def __init__(self, pan, panRule):
		self._PanEffect = NWaves.Effects.Stereo.PanEffect(pan, panRule)
		self.PanRule = self._PanEffect.PanRule
		self.Pan = self._PanEffect.Pan
 
	def get_pan(self, *args, **kwargs):
		return self._PanEffect.get_Pan(self, *args, **kwargs)
 
	def set_pan(self, *args, **kwargs):
		return self._PanEffect.set_Pan(self, *args, **kwargs)
 
	def get_pan_rule(self, *args, **kwargs):
		return self._PanEffect.get_PanRule(self, *args, **kwargs)
 
	def set_pan_rule(self, *args, **kwargs):
		return self._PanEffect.set_PanRule(self, *args, **kwargs)
 
	def process(self, *args, **kwargs):
		return self._PanEffect.Process(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._PanEffect.Reset(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._PanEffect.Overloads(self, *args, **kwargs)