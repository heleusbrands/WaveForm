from ...wrapper import NWaves 


 

class BiQuadFilter:

	def __init__(self, b0, b1, b2, a0, a1, a2):
		self._BiQuadFilter = NWaves.Filters.BiQuad.BiQuadFilter(b0, b1, b2, a0, a1, a2)
 
	def process(self, *args, **kwargs):
		return self._BiQuadFilter.Process(self, *args, **kwargs)
 
	def reset(self, *args, **kwargs):
		return self._BiQuadFilter.Reset(self, *args, **kwargs)
 
	def change(self, *args, **kwargs):
		return self._BiQuadFilter.Change(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._BiQuadFilter.Overloads(self, *args, **kwargs)