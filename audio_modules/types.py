import pandas as pd
import numpy as np
from . import air
from array import array
from typing import Union




class _FrequencyDomain:

	def __repr__(self) -> str:
		return f'FrequencyDomain()'
		
	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		if (
			np.iterable(value[0]) 
			and isinstance(value[0], (list, tuple, np.ndarray, array))
			):
			value = air.flatten(value)
		try:
			return True if all([(x < 20000 and x > 0) for x in value].append(self._decibel_differentiator(value))) else False
		except:
			return False
		
	def _decibel_differentiator(self, values):
		return True if any([x > 100 for x in values]) else False
		
		
	def __matmul__(self, value):
		return self.__eq__(value)

class _PitchDomain:

	def __repr__(self) -> str:
		return f'PitchDomain()'

	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		if (
			np.iterable(value[0]) 
			and isinstance(value[0], (list, tuple, np.ndarray, array))
			):
			value = air.flatten(value)
		try:
			return True if all([(x < 800 and x > 40) for x in value if x != 0]) else False
		except:
			return False
		
	def __matmul__(self, value):
		return self.__eq__(value)

class _DecibelDomain:

	def __repr__(self) -> str:
		return f'DecibelDomain()'

	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		if (
			np.iterable(value[0]) 
			and isinstance(value[0], (list, tuple, np.ndarray, array))
			):
			value = air.flatten(value)
		try:
			return True if all([(x < 100 and x > -100) for x in value]) else False
		except:
			return False
	
	def __matmul__(self, value):
		return self.__eq__(value)
	
class _PascalDomain:

	def __repr__(self) -> str:
		return f'PascalDomain()'

	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		if (
			np.iterable(value[0]) 
			and isinstance(value[0], (list, tuple, np.ndarray, array))
			):
			value = air.flatten(value)
		try:
			return True if all([(x < 12 and x > 0) for x in value]) else False
		except:
			return False
	
	def __matmul__(self, value):
		return self.__eq__(value)


class _TimeDomain:
	"""
	This class is a custom type, used to check if a given sequence is a valid time domain.

	The __eq__ method first checks if value is not iterable and if it is not, it returns False. If value is iterable, it checks if the first element of value is iterable. If it is, it air.flattens value using the air.flatten function.

	The method then tries to return True if all elements in the air.pairwise comparison of value are in ascending order. If there is an exception, it returns False.

	Example Usage:
	>>> from xpression.types import TimeDomain
	>>> x = [1, 2, 3, 4, 5]
	>>> x == TimeDomain
	True	
	"""

	def __repr__(self) -> str:
		return f'TimeDomain()'
	
	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		if (
			np.iterable(value[0]) 
			and isinstance(value[0], (list, tuple, np.ndarray, array))
			):
			value = air.flatten(value)
		try:

			return True if all([a < b for a, b in air.pairwise(value)]) else False
		except:
			return False
		
	def __matmul__(self, value):
		return self.__eq__(value)
		

class Incompatible: pass

DomainType = Union[_TimeDomain, _DecibelDomain, _PascalDomain, _PitchDomain, _FrequencyDomain]

ValidTimeDomain = _TimeDomain()

ValidDecibelDomain = _DecibelDomain()

ValidPascalDomain = _PascalDomain()

ValidPitchDomain = _PitchDomain()

ValidFrequencyDomain = _FrequencyDomain()

class DOMtype:
	def __init__(self, data):
		self.data = data
		if ValidTimeDomain @data: self.domtype = _TimeDomain
		elif ValidDecibelDomain @data: self.domtype = _DecibelDomain
		elif ValidPascalDomain @data: self.domtype = _PascalDomain
		elif ValidPitchDomain @data: self.domtype = _PitchDomain
		elif ValidFrequencyDomain @data: self.domtype = _FrequencyDomain
		else: self.domtype = Incompatible

	def __repr__(self):
		return self.domtype.__repr__()

