# %% Successful RubberBand Processing Test
import numpy as np
from pydub import AudioSegment
import clr
from System.Collections.Generic import List
from System import Array, Single
import System
from rubberband import RubberBandStretcher as rbs
audio = AudioSegment.from_file(r'xpression\xtract\03-01-05-02-02-01-01.wav')
audio = audio.set_channels(1)
audio_array = audio.get_array_of_samples()

rate = audio.frame_rate
num_of_frames = len(audio_array)
singleInput = Array[Array[Single]]([
    Array[Single](
        list(audio_array)
        )
    ])

stretcher = rbs(rate, 1, initialPitchScale=1.5)
stretcher._RubberBandStretcher.Study(singleInput, num_of_frames, True)
stretcher._RubberBandStretcher.Process(singleInput, num_of_frames, True)

# %%
available = stretcher._RubberBandStretcher.Available()
singleOut = Array[Array[Single]]([
    Array.CreateInstance(Single, available)
    ])

# %%
audio_out = stretcher._RubberBandStretcher.Retrieve(singleOut, available)

# %%
np.ctypeslib.as_array(singleOut)


