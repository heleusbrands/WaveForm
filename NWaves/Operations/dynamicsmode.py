from ..wrapper import NWaves 


 

class DynamicsMode:

	def __init__(self, *args, **kwargs):
		self._DynamicsMode = NWaves.Operations.DynamicsMode(*args, **kwargs)
		self.NoiseGate = self._DynamicsMode.NoiseGate
		self.Expander = self._DynamicsMode.Expander
		self.Limiter = self._DynamicsMode.Limiter
		self.Compressor = self._DynamicsMode.Compressor
		self.value__ = self._DynamicsMode.value__