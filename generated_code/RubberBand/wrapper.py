import ctypes as ct
import os
import clr
from msl.loadlib import LoadLibrary

RubberBand = LoadLibrary(r'c:\Users\ryanw\Documents\Code\Modules\NX\rubberwrapper/rubberband-sharp.dll', 'net')
clr.AddReference(RubberBand)
import RubberBand