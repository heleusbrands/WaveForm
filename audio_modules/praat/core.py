
import numpy as np
import pandas as pd
from parselmouth import Sound
from parselmouth.praat import call
from functools import singledispatchmethod
from .configs import *
from pydantic import PositiveFloat




class PraatBase:

    @singledispatchmethod
    def __init__(
        self,
        audio,
        rate: PositiveFloat = None
        ):
        raise TypeError(f"Type {type(audio)} not supported.")
    
    @__init__.register(Sound)
    def _(
        self, 
        audio: Sound, 
        rate: PositiveFloat = None
        ):
        self.sound: Sound = audio
        self._target = self.sound
        self.audio = audio
        self.rate = self.sound.get_sampling_frequency()
        self.data = None

    @__init__.register(str)
    def _(
        self, 
        audio: str,
        rate: PositiveFloat = None
        ):
        self.sound: Sound = Sound(audio)
        self._target = self.sound
        self.audio = audio
        self.rate = self.sound.get_sampling_frequency()
        self.data = None

    @__init__.register(np.ndarray)
    def _(
        self,
        audio: np.ndarray,
        rate: PositiveFloat
        ):
        self._target = None
        self.sound: Sound = Sound(audio, sampling_frequency=rate)
        self.audio = audio
        self.rate = self.sound.get_sampling_frequency()
        self.data = None

    @property
    def dataframe(self):
        if self.data is None:
            self.__call__()
            if self.data is None: return None
        return pd.DataFrame(self.data.dict())
    


