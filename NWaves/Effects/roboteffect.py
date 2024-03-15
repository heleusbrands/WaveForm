from ..wrapper import NWaves 


 

class RobotEffect:

	def __init__(self, h: int, fftSize: int=0):
		self._RobotEffect = NWaves.Effects.RobotEffect(hopSize, fftSize)
 
	def process_spectrum(self, *args, **kwargs):
		return self._RobotEffect.ProcessSpectrum(self, *args, **kwargs)
 
	def overloads(self, *args, **kwargs):
		return self._RobotEffect.Overloads(self, *args, **kwargs)