from .waveform import *
from.audio_modules.extraction.core import *
from pydub import AudioSegment
import numpy as np
from multipledispatch import dispatch
from pyrubberband import pitch_shift, time_stretch

class ReformWarp(Reformer):

    @dispatch(np.ndarray, int)
    def __init__(self, nparray: np.ndarray, sr: int):
        self.array = nparray
        self.rate = sr
        self.settings = RubberBandSettings()
        self.pitch_shift_steps = 0

    @dispatch(WaveForm)
    def __init__(self, waveform: WaveForm):
        self.array = waveform._array
        self.rate = waveform._rate
        self.settings: RubberBandSettings = RubberBandSettings()
        self.pitch_shift_steps = 0
        self._pitch_map = None
        self._time_map = None
        self._frequency_map = None

    @property
    def engine(self):
        return self.settings.engine
    
    @property
    def pitch_map(self):
        if self._pitch_map is None:
            self._pitch_map = PitchMap()
        return self._pitch_map
    
    @engine.setter
    def engine(self, engine):
        self.settings.engine = engine

    def shift_pitch(self, steps = None):
        if steps is None:
            steps = self.pitch_shift_steps
        else:
            self.pitch_shift_steps = steps
        rbargs = self.settings.__compile__()
        return pitch_shift(self.array, self.rate, steps, rbargs)
    
    @SourceMapping
    def map_pitch(self, pitchmap: PitchMap = None):
        if pitchmap is None:
            if self._pitch_map:
                pitchmap = self._pitch_map
            else:
                raise ValueError("No pitch map provided")
        f = pitchmap.__source_to_file__()
        self.settings.engine.pitchmap.value = f
        rbargs = self.settings.__compile__()
        return pitch_shift(self.array, self.rate, 0, rbargs), pitchmap

        

        
        