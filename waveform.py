import array
from collections import deque
from copy import deepcopy
from typing import TypeVar, Union

import numpy as np
import pytsmod as tsm
import tensorflow as tf
from IPython.display import Audio
from parselmouth import Sound
from pydantic import BaseConfig, BaseModel
from pydub import AudioSegment
from pyrubberband.pyrb import __rubberband as rb
import static_ffmpeg

from xpression.xtract.XT.commands import *
from xpression.xtract.XT.xtract_configs import *
from xtract import AnalysisGrid

WaveFormObject = TypeVar('WaveFormObject', bound='WaveForm')

class Comparison:
    def __init__(self, primary_series, secondary_series):
        self._series = deque([primary_series, secondary_series])
        self.in_place = False

    @property
    def primary_series(self):
        return self._series[0]
    
    @property
    def secondary_series(self):
        return self._series[1]

    @property
    def reverse(self):
        if self.in_place:
            self._series.reverse()
            return self
        else:
            comp = deepcopy(self)
            comp.reverse
            return comp
    
    @property
    def diff(self):
        return self.primary_series - self.secondary_series
    
    @property
    def ratio(self):
        return self.primary_series / self.secondary_series
    
    @property
    def means_diff(self):
        return self.primary_series.mean() - self.secondary_series.mean()
    
    @property
    def deviation_from_mean(self):
        d1 = self.primary_series / self.primary_series.mean()
        d2 = self.secondary_series / self.secondary_series.mean()
        return (d1, d2)
    
    @property
    def mean_deviation_difference(self):
        d1, d2 = self.deviation_from_mean
        return d1 - d2
    
    @property
    def align(self):
        return self.primary_series.align(self.secondary_series)
    
    @property
    def compare(self):
        if len(self.primary_series) != len(self.secondary_series):
            primary, secondary = self.align
            return primary.compare(secondary)
        return self.primary_series.compare(self.secondary_series)

class WaveConfig(BaseConfig):
    arbitrary_types_allowed = True
    underscore_attrs_are_private = True

class WaveSettings(BaseModel):
    class Config(WaveConfig):
        pass

    channels: int
    rate: int
    width: int = 2
    array: np.ndarray = None

class FormFeature:
    pass

class Informer:
    def __init__(self, waveform: WaveFormObject = None):
        self._waveform: WaveForm = deepcopy(waveform)
        self._settings = None
        self._form = None
        self._features = {}

    def __call__(self):
        self.__extract__()
        return self
    
    @property
    def settings(self):
        return self._settings

    def __extract__(self):
        pass

    def __form_audiosegment__(self) -> AudioSegment:
        return self._waveform.forms.audio_segment

    def __form_sound__(self) -> Sound:
        return self._waveform.forms.sound

    def create_comparison(self, first_feature, second_feature):
        return Comparison(first_feature, second_feature)
    
    @property
    def dataframe(self):
        if not self._features:
            self.__extract__()
        return pd.DataFrame(self._features)

class Reformer:

    def __init__(self, waveform: WaveFormObject = None):
        '''A non-destructive audio waveform manipulator.
        
        This is a class that initializes from a waveform object and has methods to modify and compile
        the new waveform. It's not meant to be initialized directly, but rather to be launched from it's
        parent waveform object as needed. It's a non-destructive waveform manipulator, meaning that it
        doesn't modify the original waveform, but rather creates a new one from it.
        
        Parameters
        ----------
        waveform : WaveFormObject
            A WaveFormObject, which is a Base object that represents an audio waveform. It contains 
            an array of audio samples and information about the audio such as sample rate, number of 
            channels, and bit depth.
        
        '''
        self._settings = None
        self._waveform: WaveForm = waveform
        self._array = self._waveform._array
    
    def __call__(self):
        return self._modifier() 
    
    @property
    def settings(self):
        return self._settings

    def _modifier(self):
        pass

    def _compile(self, audio):
        waveform = WaveForm(
            audio, 
            self._waveform.settings.rate, 
            self._waveform.settings.channels
            )
        waveform.settings.width = self._waveform.settings.width
        return waveform

class Form:

    def __init__(self, waveform: WaveFormObject = None):
        '''This is a base class for classes that initialize and convert audio waveform data into a specified format.

        The intention is to make audio data easier to work with and to provide a single interface for commonly used audio
        formats.
        
        Parameters
        ----------
        waveform : WaveFormObject
            A WaveFormObject, which is an object that represents an audio waveform and contains information
        such as the audio data, sample rate, and number of channels.
        
        '''
        self._waveform: WaveForm = waveform
        self.audio = waveform.audio
        self.settings: WaveSettings = self._waveform.settings
        self.converter_type = None
        
    
    def __call__(self):

        if self.converter_type == AudioSegment:
            self._waveform._array = np.array(self._waveform.audio.get_array_of_samples())
            self._waveform.settings.rate = self._waveform.audio.frame_rate
            self._waveform.settings.channels = self._waveform.audio.channels
            self._waveform.settings.width = self._waveform.audio.sample_width

        elif self.converter_type == Sound:
            self._waveform._array = self._waveform.audio.values
            self._waveform.settings.rate = self._waveform.audio.sampling_frequency
            self._waveform.settings.channels = self._waveform.audio.n_channels

        elif self.converter_type == np.ndarray:
            self._waveform._array = self._waveform.audio

        elif self._waveform.type == array.array:
            self._waveform._array = self._waveform.audio

        return self.converter() 

    @property
    def audio_type(self):
        return self._waveform.type

    def converter(self):
        pass

    def _update(self, audio: Union[AudioSegment, Sound, np.ndarray, array.array]):
        self._waveform.audio = audio
        if self._waveform.type == AudioSegment:
            self._waveform._array = self._waveform.audio.get_array_of_samples()
            self._waveform.settings.rate = self._waveform.audio.frame_rate
            self._waveform.settings.channels = self._waveform.audio.channels
            self._waveform.settings.width = self._waveform.audio.sample_width
        elif self._waveform.type == Sound:
            self._waveform._array = self._waveform.audio.values
            self._waveform.settings.rate = self._waveform.audio.sampling_frequency
            self._waveform.settings.channels = self._waveform.audio.n_channels
        elif self._waveform.type == np.ndarray:
            self._waveform._array = self._waveform.audio
        elif self._waveform.type == array.array:
            self._waveform._array = self._waveform.audio
        return self._waveform

class InformPitch(Informer):
    def __init__(self, waveform: WaveFormObject = None):
        super().__init__(waveform)
        self._settings = AnalysisSettings().Pitch
        self._pitch_array = None
        self._frequency_array = None
        self._decibel_array = None
        self._time_array = None
        self._frame_array = None
        self._form = self.__form_sound__()

        self.engine = PitchDetectionEngines.NetCastCC

    def __extract__(self):
        if self.engine == self.engine.CrossCorrelation:
            pitch = self.__crosscorr__()
        elif self.engine == self.engine.NetCastCC:
            pitch, pmin, pmax  = self.__netcastcc__()
        self._pitch_array = pitch.selected_array
        self._frequency_array = pitch.selected_array['frequency']
        self._decibel_array = pitch.selected_array['strength']
        self._time_array = pitch.xs()
        self._frame_array = np.array([round(t * self._waveform.rate) for t in self._time_array])
        self._features = {'time': self._time_array, 'frequency': self._frequency_array, 'decibel': self._decibel_array, 'frame': self._frame_array}
        

    def __netcastcc__(self, runs = 4, i = 0):
        if i == 0: self._settings = AnalysisSettings().Pitch
        pitch = self._form.to_pitch_cc(**self.settings.dict())
        pmax = round(pitch.selected_array['frequency'].max())
        pmin = round(pitch.selected_array['frequency'].min())
        i += 1
        if i != runs:
            self.settings.pitch_ceiling = float(pmax * 2)
            self.settings.pitch_floor = float(round(pmin / 2)) if round(pmin / 2) > 0 else 50.0
            pitch, pmin, pmax = self.__netcastcc__(runs, i)
        return pitch, pmin, pmax
    
    def __crosscorr__(self):
        return self._form.to_pitch_cc(**self.settings.dict())
    
    @property
    def frequency(self):
        return self.dataframe['frequency']
    
    @property
    def time(self):
        return self.dataframe['time']
    
    @property
    def decibel(self):
        return self.dataframe['decibel']
    
    @property
    def frame(self):
        return self.dataframe['frame']
    

class ReformFlux(Reformer):
    def __init__(self, waveform: WaveFormObject = None):
        super().__init__(waveform)

    def __call__(self, warping_factor: float = None):
        if warping_factor: self.warping_factor = warping_factor
        return self._modifier() 

    @property
    def settings(self):
        return self._waveform._FluxSettings

    @property
    def use_wsola(self):
        self.settings.Algorithm = self.settings.algorithms.wsola
        return self
    
    @property
    def use_hpps(self):
        self.settings.Algorithm = self.settings.algorithms.hpps
        return self
    
    @property
    def use_phase_vox(self):
        self.settings.Algorithm = self.settings.algorithms.phasevocoder
        return self 
    
    @property
    def warping_factor(self):
        return self.settings.Factor
    
    @warping_factor.setter
    def warping_factor(self, value):
        self.settings.Factor = value
        return self
    
    def warp_to_match(self, waveform: WaveFormObject):
        self.warping_factor = waveform.info.duration / self._waveform.info.duration
        return self._modifier()
    
    def _modifier(self) -> WaveFormObject:
        if type(self._array) != np.ndarray:
            array = np.asarray(self._array)
        else:
            array = self._array
        if array.dtype != np.float64:
            array = array.astype(np.float64)

        settings = self.settings
        algorithm = settings.Algorithm
        factor = settings.Factor

        if algorithm == settings.algorithms.wsola:
            win_type = settings.WsolaSettings.window_type
            win_size = settings.WsolaSettings.window_size
            slide = settings.WsolaSettings.slide_distance
            tolerance = settings.WsolaSettings.tolerance
            flux = tsm.wsola(array, factor, win_type, win_size, slide, tolerance)

        elif algorithm == settings.algorithms.hpps:
            hppssettings = settings.HppsSettings.dict().values()
            flux = tsm.hptsm(array, factor, *hppssettings)

        elif algorithm == settings.algorithms.phasevocoder:
            flux = tsm.phase_vocoder(array, factor, **settings.PhaseVocoderSettings.dict())

        flux = np.expand_dims(flux, axis=1)
        return self._compile(flux)
    
class ReformPitch(Reformer):
    def __init__(self, waveform: WaveFormObject = None):
        super().__init__(waveform)
        #self._analysis_grid = AnalysisGrid(waveform.forms.sound)
        #self.settings = self._waveform.forms.form_analysis.settings.Pitch
        self._simplify = False
        self._settings = AnalysisSettings().Pitch
        self._use_net_caster = True      

    @property
    def settings(self):
        return self._settings
    
    @property
    def simplify(self):
        self._simplify = True
        return self

    @property
    def _manipulation(self):
        return self._create_manipulation(self._waveform)
    
    @property
    def _pitch_tier(self):
        return self._extract_pitch_tier(self._waveform)

    def _extract_pitch_tier(self, waveform: WaveFormObject):
        pci = PraatCommands(self.extract_pitch(waveform))
        return pci.down_to_pitch_tier().result
    
    def pitch_net_caster(self, runs = 4, i = 0, simplify = False, waveform = None):
        if i == 0: self._settings = AnalysisSettings().Pitch
        if not waveform: waveform = self._waveform
        pitch = waveform.forms.S.to_pitch_cc(**self.settings.dict())
        pmax = round(pitch.selected_array['frequency'].max())
        pmin = round(pitch.selected_array['frequency'].min())
        i += 1
        if i != runs:
            self.settings.pitch_ceiling = float(pmax * 2)
            self.settings.pitch_floor = float(round(pmin / 2)) if round(pmin / 2) > 0 else 50.0
            pitch, pmin, pmax = self.pitch_net_caster(runs, i, waveform=waveform)
        if i == runs and simplify:
            pitch = pitch.smooth()
        return pitch, pmin, pmax
    
    def extract_pitch(self, waveform: WaveFormObject):
        if not self._use_net_caster:
            pitch = waveform.forms.sound.to_pitch_cc(
                self.settings.time_step,
                self.settings.pitch_floor,
                self.settings.max_number_of_candidates,
                self.settings.very_accurate,
                self.settings.silence_threshold,
                self.settings.voicing_threshold,
                self.settings.octave_cost,
                self.settings.octave_jump_cost,
                self.settings.voiced_unvoiced_cost,
                self.settings.pitch_ceiling
            )
        else:
            pitch, pmin, pmax = self.pitch_net_caster(waveform=waveform)
        if self._simplify:
            pitch = pitch.smooth()
        return pitch
    
    def _create_manipulation(self, waveform: WaveFormObject):
        pitch = self.extract_pitch(waveform)
        pci = PraatCommands(waveform.forms.sound)
        return pci.to_manipulation(from_pitch=pitch).result
    
    def match_pitch(self, from_waveform: WaveFormObject):
        """
        Create a modified waveform from a given waveform, by extracting the pitch from
        the provided reference waveform, and using it to replace the current waveforms pitch.

        Parameters
        ----------
        from_waveform : WaveForm
            The reference waveform from which to extract the pitch tier.

        Returns
        -------
        WaveForm
            A waveform with the pitch tier modified.
        """
        pci = PraatCommands(self._manipulation)
        modified_manipulation = pci.replace_pitch_tier(self._extract_pitch_tier(from_waveform)).result

        if type(modified_manipulation) == list:
            print(type(modified_manipulation))
            pci = PraatCommands(self._manipulation)
        else: pci = PraatCommands(modified_manipulation)
        result = pci.get_resynthesis_with_overlap().result
        return self._compile(result)

class ReformWarp(Reformer):

    def __init__(self, waveform: WaveFormObject):
        super().__init__(waveform)
        self._settings: RubberBandSettings = RubberBandSettings()

        self._pitch_map = None
        self._time_map = None
        self._frequency_map = None

        self.array = waveform._array
        self.rate = waveform.rate
        

    def __call__(self, 
                 pitch=None, 
                 time=None, 
                 tempo=None, 
                 frequency=None, 
                 pitch_map: Union[tuple, PitchMap, None]=None, 
                 time_map=None, 
                 frequency_map=None,
                 engine_R3=False
                 ):
        if pitch: self.pitch = pitch
        if time: self.time = time
        if tempo: self.tempo = tempo
        if frequency: self.frequency = frequency
        if pitch_map and type(pitch_map) == PitchMap: self._pitch_map = pitch_map
        if pitch_map and type(pitch_map) == tuple:
            a, b = pitch_map
            self.pitch_map.add_to_map(a, b)
        if time_map and type(time_map) == TimeMap: self._time_map = time_map
        if time_map and type(time_map) == tuple:
            a, b = time_map
            self.time_map.add_to_map(a, b)
        if frequency_map and type(frequency_map) == FrequencyMap: self._frequency_map = frequency_map
        if frequency_map and type(frequency_map) == tuple:
            a, b = frequency_map
            self.frequency_map.add_to_map(a, b)
        #COMPLETE: Add time_map and frequency_map handlers
        #COMPLETE: Add time_map and frequency_map properties
        if engine_R3: self.engine = self._settings.engines.R3

        return self._modifier() 

    def _modifier(self):
        if self._pitch_map is not None: self.engine.pitchmap.value = self._pitch_map.__source_to_file__()
        if self._time_map is not None: self.engine.timemap.value = self._time_map.__source_to_file__()
        if self._frequency_map is not None: self.engine.freqmap.value = self._frequency_map.__source_to_file__()
        rbargs = self._settings.__compile__() 
        print(rbargs)
        modified = rb(self.array, self.rate, **rbargs)
        if self._pitch_map: self._pitch_map.__del_file__()
        if self._time_map: self._time_map.__del_file__()
        if self._frequency_map: self._frequency_map.__del_file__()
        return self._compile(modified)

    @property
    def engine(self):
        return self.settings.engine

    @engine.setter
    def engine(self, engine):
        self.settings.engine = engine

    @property
    def time(self):
        return self.engine.time.value
    
    @time.setter
    def time(self, value):
        self.engine.time.value = value

    @property
    def tempo(self):
        return self.engine.tempo.value
    
    @tempo.setter
    def tempo(self, value):
        self.engine.tempo.value = value
    
    @property
    def duration(self):
        return self.engine.duration.value
    
    @duration.setter
    def duration(self, value):
        self.engine.duration.value = value

    @property
    def pitch(self):
        return self.engine.pitch.value
    
    @pitch.setter
    def pitch(self, value):
        self.engine.pitch.value = value

    @property
    def pitch_map(self):
        if self._pitch_map is None:
            self._pitch_map = PitchMap()
        return self._pitch_map

    @property
    def time_map(self):
        if self._time_map is None:
            self._time_map = TimeMap()
        return self._time_map
    
    @property
    def frequency_map(self):
        if self._frequency_map is None:
            self._frequency_map = FrequencyMap()
        return self._frequency_map

class ReFormant(Reformer):
    def __init__(self, waveform: WaveFormObject = None):
        super().__init__(waveform)
        self._settings = AnalysisSettings().Formant
    
    @property
    def settings(self):
        return self._settings
    
    @property
    def formant_shift_ratio(self):
        return self._settings.formant_shift_ratio
    
    @formant_shift_ratio.setter
    def formant_shift_ratio(self, value):
        self._settings.formant_shift_ratio = value

    def shift_formant(self, ratio = None):
        if ratio: self.settings.formant_shift_ratio = ratio
        pitch = self._waveform.reformers.pitch.extract_pitch(self._waveform)
        pci = PraatCommands([self._waveform.forms.sound, pitch])
        return pci.change_gender(None, None, None, *self.settings.dict().values()).result
    
class ReformIntensity(Reformer):
    def __init__(self, waveform: WaveFormObject = None):
        super().__init__(waveform)
        #self._analysis_grid = AnalysisGrid(waveform.forms.sound)
        #self.settings = self._waveform.forms.form_analysis.settings.Intensity

    @property
    def settings(self):
        return self._waveform.forms.form_analysis.settings.Intensity

    @property
    def intensity(self):  # sourcery skip: inline-immediately-returned-variable
        intensity = self._waveform.forms.sound.to_intensity(
            self.settings.min_frequency,
            self.settings.time_step,
            self.settings.subtract_mean_pressure
        )
        return intensity
    
    def get_intensity(self, waveform: WaveFormObject):
        # sourcery skip: inline-immediately-returned-variable
        intensity = waveform.forms.sound.to_intensity(
            self.settings.min_frequency,
            self.settings.time_step,
            self.settings.subtract_mean_pressure
        )
        return intensity
    
    def multiply_intensity(self, from_waveform: WaveFormObject):
        pci = PraatCommands(self.get_intensity(from_waveform))
        tier = pci.down_to_intensitytier().result
        pci = PraatCommands(self._waveform.forms.sound)
        result = pci.multiply(tier).result
        return self._compile(result)

class FormAudioSegment(Form):
    def __init__(self, waveform: WaveFormObject = None):
        super().__init__(waveform)
        self.converter_type = AudioSegment
        self.converter()

    def converter(self) -> AudioSegment:

        if self.audio_type == AudioSegment:
            return self._waveform.audio
        
        if self.audio_type == np.ndarray or self.audio_type == array.array:
            audio = self._from_numpy(self._waveform.audio)
            self._waveform.audio = audio
            return audio
        
        if self.audio_type == str:
            audio = AudioSegment.from_file(self.audio)
            self._waveform.audio = audio
            return audio
        
        if self.audio_type == bytes:
            audio = AudioSegment(
                self._waveform.audio, 
                sample_width=self._waveform.settings.width, 
                frame_rate=self._waveform.settings.rate, 
                channels=self._waveform.settings.channels
                )
            self._waveform.audio = audio
            return audio
        
        if self.audio_type == Sound:
            try:
                array = self._waveform.audio.asarray()
            except:
                array = self._waveform.audio.values
            audio = self._from_numpy(array)
            self._waveform.audio = audio
            return audio
    """
    def _update(self, audio):
        self._waveform.audio = audio
        self._waveform._array = audio.get_array_of_samples()
        self._waveform.settings.channels = audio.channels
        self._waveform.settings.rate = audio.frame_rate
        self._waveform.settings.width = audio.sample_width
    """
    def _from_numpy(self, array):
        seg = AudioSegment.empty()
        seg.channels = self.settings.channels
        seg.frame_rate = self.settings.rate
        seg.sample_width = self.settings.width
        seg.frame_width = seg.channels * seg.sample_width
        samples = self._convert_array(array)
        seg = seg._spawn(samples)
        return seg

    def _convert_array(self, raw_array):
        raw_array = self._convert_dtype(raw_array)
        raw_array = self._convert_shape(raw_array)
        raw_array = self._convert_array_type(raw_array)
        return raw_array

    def _convert_dtype(self, raw_array):
        if type(raw_array) != np.ndarray: return raw_array
        if raw_array.dtype == np.int64: return raw_array.astype(np.int32)
        if raw_array.dtype == np.int32: return raw_array
        if raw_array.dtype == np.int16: return raw_array
        if raw_array.dtype == np.float64: return raw_array.astype(np.int32)
        if raw_array.dtype == np.float32: return raw_array.astype(np.int32)
        if raw_array.dtype == np.float16: return raw_array.astype(np.int16)

    def _convert_shape(self, raw_array):
        if type(raw_array) != np.ndarray: return raw_array
        if raw_array.shape[0] == 0 or raw_array.shape[0] == 1: raw_array = raw_array.T
        if type(raw_array) == np.ndarray: return raw_array.squeeze()

    def _convert_array_type(self, raw_array):
        if type(raw_array) != np.ndarray: return raw_array
        if type(raw_array) == np.ndarray: return array.array('h', raw_array)
    
class FormSound(Form):
    def __init__(self, waveform: WaveFormObject = None):
        super().__init__(waveform)
        self.converter_type = Sound
        self.converter()

    def converter(self) -> Sound:
        if self.audio_type == Sound: return self._waveform.audio
        array = self._waveform._array
        if type(array) != np.ndarray: array = np.array(array, dtype=np.float64)
        elif len(array.shape) != 1: array = array.squeeze()
        rate = self.settings.rate
        sound = Sound(array, sampling_frequency=rate)
        self._waveform.audio = sound
        return self._waveform.audio

class FormFile(Form):
    def __init__(self, waveform: WaveFormObject = None, file_name: str = None, format: str = None):
        super().__init__(waveform)
        self.converter_type = str
        self.file_name = file_name
        self.format = format
        self.converter()

    def converter(self) -> str:
        if self.audio_type == str: return self._waveform.audio
        file_name = self.file_name
        format = self.format
        audio = AudioSegment(self._waveform._array, frame_rate=self.settings.rate, sample_width=2, channels=self.settings.channels)
        self._waveform.audio =  audio.export(file_name, format=format)
        return self._waveform.audio
        
class ReForm(Form):
    def __init__(self, waveform: WaveFormObject, new_rate: int):
        super().__init__(waveform)
        self.converter_type = AudioSegment
        self.new_rate = new_rate
        self.converter()

    def converter(self) -> Sound:
        segment: AudioSegment = self._waveform.forms.A
        resampled = segment.set_frame_rate(self.new_rate)
        self._update(resampled)
        #self._waveform.loader()
        return self._waveform.audio

class Reformers:

    def __init__(self, waveform: WaveFormObject):
        self._waveform = waveform

    @property
    def pitch(self):
        return ReformPitch(self._waveform)
    
    @property
    def P(self):
        return self.pitch
    
    @property
    def intensity(self):
        return ReformIntensity(self._waveform)
    
    @property
    def I(self):
        return self.intensity
    
    @property
    def flux(self):
        return ReformFlux(self._waveform)
    
    @property
    def warp(self):
        return ReformWarp(self._waveform)
    
    @property
    def W(self):
        return self.warp
    
    @property
    def F(self):
        return self.flux
    
    @property
    def formant(self):
        return ReFormant(self._waveform)
    
    @property
    def RF(self):
        return self.formant
    
class Forms:

    def __init__(self, waveform: WaveFormObject):
        self._waveform = waveform

    @property
    def audio_segment(self):
        return FormAudioSegment(self._waveform)()
    
    @property
    def A(self):
        return self.audio_segment
    
    @property
    def sound(self):
        return FormSound(self._waveform)()
    
    @property
    def S(self):
        return self.sound
    
    def audio_file(self, file_name: str, format: str = None) -> str:
        if format is None: format = 'wav'
        audio_file = FormFile(self, file_name, format)
        return audio_file()
    
    def F(self, file_name: str, format: str = None) -> str:
        return self.audio_file(file_name, format)
    
    @property
    def tensor(self):
        return tf.convert_to_tensor(self._waveform._array)
    
    @property
    def T(self):
        return self.tensor
    
    @property
    def numpy_array(self):
        return self._waveform._array
    
    @property
    def N(self):
        return self.numpy_array
    
    @property
    def form_analysis(self):
        waveform = deepcopy(self._waveform)
        sound = waveform.forms.sound
        grid = AnalysisGrid(sound)
        return grid
    
    def reform_rate(self, new_rate: int):
        return ReForm(self._waveform, new_rate)()
    
class Informers:

    def __init__(self, waveform: WaveFormObject):
        self._waveform = waveform

    @property
    def pitch(self):
        return InformPitch(self._waveform)
    
    @property
    def P(self):
        return self.pitch

class WaveForm:
    '''
        This is a class that provides various methods for converting and manipulating audio data. The main audio data is stored as an array, which is used to switch forms depending on the method called. 
        
        i.e. When the `wf.forms.audio_segment` method is called, the array is converted to an AudioSegment object, and is accessible either through the return of the method or the `wf.audio` attribute.

        This class employs two main base class types, the `Form` and the `Reformer`. The `Form` class is used to convert the audio data to a specific type, while the `Reformer` class is used to modify the audio data in some way. These classes are available through the `wf.forms` and `wf.reformers` attributes, respectively.

        Additionally, made available by this class is the `AnalysisGrid` class, which is used to analyze the audio data and return a grid of the results. This class is used by the `WaveForm` class to provide the `wf.analyze` method, which returns the `AnalysisGrid` object.

        Last thing to mention here, is that the majority of the modifier-method parameters, are available through the settings attributes, which is an instance of the `Settings` class. This class is used to store the parameters for the various methods, and is used to provide a more concise method call. This choice was made due the incredibly complex nature of some of the methods, and the large number of parameters they require. Designing it this way, allows for the default settings to handle the majority of the setup, as the most ideal settings were chosen, and thus free the user from having to worry about the details of the method, unless they want to.

        For example: you can use `wf.reformers.flux.settings` to access settings such as the algorithm used, and the settings for that algorithm. After you set everything how you want it, you simply call `wf.reformers.flux()` to run the method with the settings you chose.

        Ease-of-use-hint:
        You can utilize any of the Forms or Reformers by using the short-hand reference, which is usually a capitalized version of the first letter of the method name. 

        i.e. `wf.forms.audio_segment` can be called by using `wf.forms.A`, and `wf.reformers.flux` can be called by using `wf.reformers.F`.
        
        Parameters
        ----------
        audio : Union[AudioSegment, Sound, np.ndarray, str, bytes]
            The audio input, which can be an instance of AudioSegment, Sound, np.ndarray, bytes or a file path
        string.
        rate
            The sampling rate of the audio signal, measured in Hz (samples per second). Only required if the audio
            input is an array or bytes.
        channels
            The number of audio channels in the audio file. For example, mono audio has one channel, while
        stereo audio has two channels.
        
        '''
    def __init__(self, audio: Union[AudioSegment, Sound, np.ndarray, str, bytes], rate = None, channels = None):
        
        self._array = None
        self._channels = channels
        self._rate = rate
        self._FluxSettings = FormFluxSettings()

        self.audio = audio
        self.settings: WaveSettings = None

        self.loader()

    @property
    def type(self):
        return type(self.audio)

    @property
    def rate(self):
        return self.settings.rate
    
    @rate.setter
    def rate(self, new_rate):
        self.settings.rate = new_rate
        self._rate = self.settings.rate
        resampled = ReForm(self, new_rate)
        return resampled()
    
    @property
    def forms(self):
        return Forms(self)
    
    @property
    def reformers(self):
        return Reformers(self)
    
    @property
    def informers(self):
        return Informers(self)

    def loader(self):
        if self.type == AudioSegment:
            self._array = np.asarray(self.audio.get_array_of_samples())
            #self._array = np.array(self.audio.get_array_of_samples())
            self.settings = WaveSettings(
                channels=self.audio.channels, 
                rate=self.audio.frame_rate, 
                width=self.audio.sample_width
                )
            
        elif self.type == Sound:
            self._array = self.audio.values
            self.settings = WaveSettings(
                channels=self.audio.get_number_of_channels(), 
                rate=self.audio.get_sampling_frequency()
                )
            
        elif self.type == np.ndarray:
            self._array = self.audio
            x, y = self._array.shape
            if (x == 1) or (y == 1):
                channels = 1
            else:
                channels = 2
            if x == 1: self._array = self._array.T
            self.audio = self._array
            self.settings = WaveSettings(
                channels=channels, 
                rate=self._rate, 
                array=self._array
                )
            
        elif self.type == str:
            self.audio = AudioSegment.from_file(self.audio)
            self.loader()

        elif self.type == bytes:
            audio = AudioSegment(self.audio, frame_rate=self._rate, sample_width=2, channels=self._channels)
            self._array = np.array(audio.get_array_of_samples())
            self.settings = WaveSettings(channels=self._channels, rate=self._rate, width=2)
        self.settings.array = self._array

    def match_xpression(self, reference_waveform: WaveFormObject):
        warped = self.reformers.flux.warp_to_match(reference_waveform)
        warped.settings.width = self.settings.width
        pitched = warped.reformers.pitch.match_pitch(reference_waveform)
        pitched.settings.width = self.settings.width
        intensified = pitched.reformers.intensity.multiply_intensity(reference_waveform)
        intensified.settings.width = self.settings.width
        return intensified

    @property
    def play(self):
        return Audio(self._array, rate=self.rate)

    @property
    def info(self) -> FormReportConfig:
        '''The "info" method returns an object of type FormReportConfig.
        This object contains the following attributes:
        - duration: The duration of the audio in seconds
        - dBFS: The dBFS value of the audio
        - rms: The rms value of the audio
        - max: The max value of the audio
        - max_dBFS: The max dBFS value of the audio
        
        '''
        if self.type == AudioSegment:
            audio = self.audio
        else:
            self.loader()
            audio = self.audio
            self.forms.audio_segment
        seconds = audio.duration_seconds
        dbfs = audio.dBFS
        rms = audio.rms
        max = audio.max
        max_dbfs = audio.max_dBFS
        info = FormReportConfig(
            duration=seconds, 
            dBFS=dbfs, 
            rms=rms, 
            max=max, 
            max_dBFS=max_dbfs
            )
        return info
    
    




