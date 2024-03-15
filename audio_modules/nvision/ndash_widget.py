from .dcc_mappings import *
from .html_mappings import *
from .draggable_mappings import *
from .daq_mappings import *


class NDashDrag:
    
	def __init__(self, callable: callable, **kwargs):
		self.callable = callable
		self.kwargs = kwargs
		self._drag = None