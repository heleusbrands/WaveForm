import ctypes as ct
import os
import clr
from msl.loadlib import LoadLibrary
import sys

_RubberBand = LoadLibrary('c:\\Users\\ryanw\\Documents\\Code\\Modules\\NX\\rubberwrapper/rubberbandsharp.dll', 'net')
wrapperpath = os.path.abspath("rubberwrapper")
nwrapperpath = os.path.normpath(wrapperpath)
sys.path.append(nwrapperpath)
clr.AddReference('rubberbandsharp')

import RubberBand as CRubberBand