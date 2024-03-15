import ctypes as ct
import os
import clr
from msl.loadlib import LoadLibrary

NWaves = LoadLibrary(r'C:\Users\ryanw\Documents\Code\Modules\NX\nwaves.0.9.6\lib\netstandard2.0\NWaves.dll', 'net')
clr.AddReference(NWaves)
import NWaves