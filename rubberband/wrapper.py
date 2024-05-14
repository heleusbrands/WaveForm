import os
import clr
from msl.loadlib import LoadLibrary
import sys

rubberband_path = os.path.abspath('rubberband_builds/rubberbandsharp.dll')
_RubberBand = LoadLibrary(rubberband_path, 'net')
clr.AddReference('rubberbandsharp')

import RubberBand as CRubberBand