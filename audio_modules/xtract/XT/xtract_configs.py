import pydantic as pdc
from pydantic import BaseModel, PrivateAttr, Field
from typing import Union, Any, TypeVar, Iterable
from enum import Enum
from plotly import graph_objects as go
import pandas as pd
import numpy as np
from threading import Event
from collections import UserDict, UserList
from tempfile import NamedTemporaryFile
from multipledispatch import dispatch
from functools import update_wrapper, wraps
import os


class ObjectX:
    pass

class PraatCommand(pdc.BaseModel): 
    name: str
    arguments: Union[list, None]
    arg_help: Union[list, None]
    result: Union[Any, None]

class Unit(Enum):
    Hertz: str = 'Hertz'
    LogHertz: str = 'logHertz'
    HertzLogarithmic: str = 'Hertz (logarithmic)'
    Mel: str = 'mel'
    Semitones: str = 'semitones'
    SemitonesRe1Hz: str = 'semitones re 1 Hz'
    SemitonesRe100Hz: str = 'semitones re 100 Hz'
    SemitonesRe200Hz: str = 'semitones re 200 Hz'
    SemitonesRe440Hz: str = 'semitones re 440 Hz'
    ERB: str = 'ERB'

class ReportConfig(pdc.BaseModel):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True

class FormReportConfig(ReportConfig):
    duration: float
    max: float
    dBFS: float
    max_dBFS: float
    rms: float
    array_type: str = None

class PitchReportConfig(ReportConfig):
    Median: str
    Mean: str
    StandardDeviation: str
    Minimum: str
    Maximum: str

class XtPitchReportConfig(PitchReportConfig):
    PitchFeature: Union[object, None]
    TimeOfMax: str
    TimeOfMin: str
    VoicedFrames: str
    MeanAbsSlope_hz: str
    MeanAbsSlope_semitones: str
    MeanAbsSlope_mel: str
    MeanAbsSlope_erbs: str

class PulseReportConfig(ReportConfig):
    PulseCount: str
    PulsePeriods: str
    PulsePeriodsMean: str
    PulsePeriodsStandardDeviation: str

class VoicingReportConfig(ReportConfig):
    UnvoicedFrames: str
    VoiceBreaksCount: str
    VoiceBreaksDegree: str

class JitterReportConfig(ReportConfig):
    Local: str
    LocalAbsolute: str
    Rap: str
    Ppq5: str
    Ddp: str

class ShimmerReportConfig(ReportConfig):
    Local: str
    LocalDb: str
    Apq3: str
    Apq5: str
    Apq11: str
    Dda: str

class HarmonicityReportConfig(ReportConfig):
    AcMean: str
    Noise2HarmRatio: str
    Harm2NoiseRatio: str

class VoiceReportConfig(ReportConfig):
    Pitch: PitchReportConfig
    Pulses: PulseReportConfig
    Voicing: VoicingReportConfig
    Jitter: JitterReportConfig
    Shimmer: ShimmerReportConfig
    Harmonicity: HarmonicityReportConfig

class XpressionSummaryReportConfig(ReportConfig):
    Pitch: PitchReportConfig
    Pulses: PulseReportConfig
    Voicing: VoicingReportConfig
    Jitter: JitterReportConfig
    Shimmer: ShimmerReportConfig
    Harmonicity: HarmonicityReportConfig

class XpressionReportConfig(ReportConfig):
    Summary: XpressionSummaryReportConfig

class Settings(pdc.BaseModel):
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed =True
        underscore_attrs_are_private = True  
        allow_mutation = True  

class AnalysisSettings(Settings):

    class _Pitch(Settings):
        _saved_feature: Union[object, None] = None
        time_step: float = 0.002
        pitch_floor: float = 75.0
        pitch_ceiling: float = 600.0
        max_number_of_candidates: int = 15
        silence_threshold: float = 0.03
        voicing_threshold: float = 0.45
        octave_cost: float = 0.01
        octave_jump_cost: float = 0.35
        voiced_unvoiced_cost: float = 0.14
        very_accurate: bool = True

    class _Formant(Settings):
        formant_shift_ratio: float = 1.0
        new_pitch_median: float = 0.0
        pitch_range_factor: float = 1.0
        duration_factor: float = 1.0

    class _Intensity(Settings):
        _saved_feature: Union[object, None] = None
        min_frequency: float = 100.0
        time_step: float = 0.002
        subtract_mean_pressure: bool = True

    class _PowerCepstrogram(Settings):
        _saved_feature: Union[object, None] = None
        time_step: float = 0.002
        pitch_floor: float = 60.0
        max_frequency: float = 5000.0
        pre_emphasis: float = 50.0

    class _Cochleagram(Settings):
        _saved_feature: ObjectX = pdc.Field(default_factory=ObjectX)
        time_step: float = 0.002
        bark_frequency_resolution: float = 0.1
        window_length: float = 0.03
        forward_mask_time: float = 0.03

    class _Silence(Settings):
        min_pitch_hz: float = 75.0
        time_step: float = 0.001
        threshold_db: float = -25.0
        min_silence_duration: float = 0.01
        min_speech_duration: float = 0.1
        silence_label: str = "silence"
        speech_label: str = "speech"

    class _VoiceDetection(Settings):
        __auto = 0.0
        time_step: float = __auto
        frequency_range: Union[tuple, list] = (70.0, 5000.0)
        short_term_window_length: float = 0.01
        long_term_window_length: float = 0.2
        flatness_threshold: float = -10.0
        threshold_db: float = -25.0
        min_silence_duration: float = 0.01
        min_speech_duration: float = 0.1
        silence_label: str = "silence"
        speech_label: str = "speech"

    class _NoiseReduction(Settings):
        noise_timerange_start: float = 0.0
        noise_timerange_end: float = 0.0
        window_length: float = 0.025
        frequency_start: float = 70.0
        frequency_end: float = 8000.0
        smoothing_bandwidth: float = 40.0
        noise_reduction_db: float = -15.0
        noice_reduction_method: str = "spectral-subtraction"
    
    Pitch = _Pitch()
    Formant = _Formant()
    Intensity = _Intensity()
    Power_Cepstrogram = _PowerCepstrogram()
    Cochleagram = _Cochleagram()
    Silence = _Silence()
    Voice_Detection = _VoiceDetection()
    NoiceReduction = _NoiseReduction()

class InterpolationType(Enum):
    no_interpolation: str = 'none'
    parabolic: str = "parabolic"
    cubic: str = "cubic"
    sinc70: str = "sinc70"
    sinc700: str = "sinc700"

class Interpolation(Settings):
    time_start: float = 0.0
    time_end: float = 0.0
    interpolation_algorithm = InterpolationType.parabolic
    

class Silence(Settings):
    min_pitch_hz: float = 75.0
    time_step: float = 0.001
    threshold_db: float = -25.0
    min_silence_duration: float = 0.01
    min_speech_duration: float = 0.1
    silence_label: str = "silence"
    speech_label: str = "speech"

class VoiceDetection(Settings):
    __auto = 0.0
    time_step: float = __auto
    frequency_range: Union[tuple, list] = (70.0, 5000.0)
    short_term_window_length: float = 0.01
    long_term_window_length: float = 0.2
    flatness_threshold: float = -10.0
    threshold_db: float = -25.0
    min_silence_duration: float = 0.01
    min_speech_duration: float = 0.1
    silence_label: str = "silence"
    speech_label: str = "speech"

class BandModulationSettings(Settings):
    Enhancement_db: float = 20.0
    Frequency_Range_hz: Union[tuple, list] = (300.0, 8000.0)
    Modulation_Slow_hz: float = 3.0
    Modulation_Fast_hz: float = 30.0
    Band_Smoothing_hz: float = 100.0

class ResamplingSettings(Settings):
    Sample_Rate_hz: float = 16000.0
    Precision: int = 50

class PitchDetectionEngines(Enum):
    CrossCorrelation: str = "CrossCorrelation"
    NetCastCC: str = "NetCastCC"

class GraphOptions(Settings):

    class Type(Settings):
        Heatmap = go.Heatmap
        Scatter = go.Scatter
        Scatter3D = go.Scatter3d
        Mesh3D = go.Mesh3d
        Marker = go.Marker
        Violin = go.Violin
        Surface = go.Surface
        
    class GraphGradient(Settings):
        agsunset: str = "agsunset"
        plasma: str = "plasma"
        magma: str = "magma"
        inferno: str = "inferno"
        viridis: str = "viridis"
        cividis: str = "cividis"
        thermal: str = "thermal"

    class LayoutColors(Settings):
        gridcolor: str = "#515467"
        color: str = "#8D91AA"
        paper_bgcolor: str = 'rgba(0,0,0,0)'
        plot_bgcolor: str = 'rgba(0,0,0,0)'

    class BasicColors(Settings):
        crimsonrose: str = '#F41C5E'
        blueviolet: str = '#A029F3'
        dodgerblue: str = '#297AF3'
        turquoise: str = '#29ECF3'
        aquamarine: str = '#52EFA0'
        khaki: str = '#EFDE52'
        coral: str = '#EF8D52'
        chocolatesunrise: str = '#E75116'

    class OptionSets(Settings):
        pass

    class Line(Settings):
        color: str = '#F41C5E'
        width: int = 2
        shape: str = 'spline'
        smoothing: float = 1.3

    class Camera(Settings):
        
        class Eye(Settings):
            x: float = 1
            y: float = 1
            z: float = 0.5
        
        eye = Eye()
    
    class Axis(Settings):

        class X(Settings):
            gridcolor="#515467"
            color='#8D91AA'
        
        class Y(Settings):
            gridcolor="#515467"
            color='#8D91AA'

        xaxis = X()
        yaxis = Y()

    class Scene(Settings):
        
        class XAxis(Settings):
            showgrid: bool = False
            backgroundcolor: str = 'rgba(0,0,0,0)'

        class YAxis(Settings):
            showgrid: bool = False
            backgroundcolor: str = 'rgba(0,0,0,0)'

        class ZAxis(Settings):
            showgrid: bool = False
            backgroundcolor: str = 'rgba(0,0,0,0)'

        class AspectRatio(Settings):
            x: float = 1
            y: float = 2
            z: float = 0.95

        xaxis = XAxis()
        yaxis = YAxis()
        zaxis = ZAxis()
        aspectratio = AspectRatio()
        bgcolor: str = 'rgba(0,0,0,0)'
    
    scene = Scene()
    camera = Camera()
    axis = Axis()
    gtypes = Type()
    gradients = GraphGradient()
    layout_colors = LayoutColors()
    basic_colors = BasicColors()
    option_sets = OptionSets()
    line = Line()


class SurfaceSettings(Settings):
    data: pd.DataFrame = None
    gset = GraphOptions()
    layout = go.Layout(
        paper_bgcolor=gset.layout_colors.paper_bgcolor,
        plot_bgcolor=gset.layout_colors.plot_bgcolor,
        height=500,
        width=800,
        xaxis=gset.axis.xaxis.dict(),
        yaxis=gset.axis.yaxis.dict(),
        scene=gset.scene.dict()
    )
    kwargs = dict(
        z=data,
        colorscale=gset.gradients.thermal,
        opacity=0.7
    )
    graph = go.Surface

class HeatmapSettings(Settings):
    data: pd.DataFrame = None
    gset = GraphOptions()
    layout = go.Layout(
        paper_bgcolor=gset.layout_colors.paper_bgcolor,
        plot_bgcolor=gset.layout_colors.plot_bgcolor,
        height=500,
        width=800,
        xaxis=gset.axis.xaxis.dict(),
        yaxis=gset.axis.yaxis.dict()  
    )
    kwargs = dict(
        z=data,
        colorscale=gset.gradients.inferno
    )
    graph = go.Heatmap

class ScatterSettings:
    data: Union[pd.DataFrame, None] = pd.DataFrame()
    gset = GraphOptions()
    layout = go.Layout(
        paper_bgcolor=gset.layout_colors.paper_bgcolor,
        plot_bgcolor=gset.layout_colors.plot_bgcolor,
        height=500,
        width=800,
        xaxis=gset.axis.xaxis.dict(),
        yaxis=gset.axis.yaxis.dict()
    )
    kwargs = dict(
        x=data.index,
        y=data,
        mode='lines',
        line=gset.line.dict()
    )
    graph = go.Scatter

class Coordinates(Settings):
    x: Union[list, tuple, np.ndarray, pd.DataFrame, pd.Series] = None
    y: Union[list, tuple, np.ndarray, pd.DataFrame, pd.Series] = None
    z: Union[list, tuple, np.ndarray, pd.DataFrame, pd.Series] = None

class G3Data(BaseModel):
    
    class Config:
        orm_mode = True
        extra = 'allow'
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
    
    x: pd.Series
    y: pd.Series
    z: pd.Series
    name: str = Field(default=None, exclude=True)
    color: str = Field(default=None, exclude=True)

class G2Data(BaseModel):
        
    class Config:
        orm_mode = True
        extra = 'allow'
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
    
    x: pd.Series
    y: pd.Series
    name: str = Field(default=None, exclude=True)
    color: str = Field(default=None, exclude=True)


class GxData:
    def __init__(self):
        self._data = []

    def Data(self, name, value):
        self.__setattr__(name, value)
        self._data.append(value)
        return self

    def __add__(self, value):
        if type(value) is not str:
            self._data.append(value)
            return self
        else:
            self.__setattr__(value, GxData())
            return self.__getattribute__(value)

class FormFluxSettings(Settings):
    class _FluxAlgorithms(Settings):
        wsola: str = "wsola"
        hpps: str = "hpps"
        phasevocoder: str = "phasevocoder"

    class _FluxWsolaSettings(Settings):
        window_type: str = "hann"
        window_size: int = 1024
        slide_distance: int = 512
        tolerance: int = 512

    class _FluxHppsSettings(Settings):
        hp_len_harm: int=10
        hp_len_perc: int=10
        hp_mask_mode: str='binary'
        hp_win_type: str='hann'
        hp_win_size: int=1024
        hp_hop_size: int=256
        hp_zero_pad: int=0
        hp_fft_shift: bool=True
        pv_win_type: str='hann'
        pv_win_size: int=2048
        pv_syn_hop_size: int=512
        pv_zero_pad: int=0
        pv_restore_energy: bool=True
        pv_fft_shift: bool=True
        pv_phase_lock: bool=True
        ola_win_type: str='hann'
        ola_win_size: int=256
        ola_syn_hop_size: int=128

    class _FluxPhaseVocoderSettings(Settings):
        win_type: str = "hann"
        win_size: int = 2048
        syn_hop_size: int = 512
        zero_pad: int = 0
        restore_energy: bool = True
        fft_shift: bool = False
        phase_lock: bool = True



    Factor: float = 1.0
    Algorithm = _FluxAlgorithms().wsola
    WsolaSettings = _FluxWsolaSettings()
    HppsSettings = _FluxHppsSettings()
    PhaseVocoderSettings = _FluxPhaseVocoderSettings()
    algorithms = _FluxAlgorithms()


class RubberBandTimeSettings(Settings):
    time: Union[str, float, int, None] = None
    tempo: Union[str, float, int, None] = None
    duration: Union[str, float, int, None] = None


class RubberBandPitchSettings(Settings):
    pitch: Union[str, float, int, None] = None
    frequency: Union[str, float, int, None] = None


class RubberBandDynamicSettings(Settings):
    timemap: Union[list, np.ndarray, None] = None
    pitchmap: Union[list, np.ndarray, None] = None
    freqmap: Union[list, np.ndarray, None] = None


class RubberBandEngineSettings(Settings):
    class _Engines(Settings):
        fast: str = "fast"
        fine: str = "fine"

    available_engines = _Engines()
    engine: str = available_engines.fast
    crisp: int = 5


class RBSetting(Settings):
    flag: str
    value: Union[str, float, int, None] = None


class _Activator:
    def __init__(self):
        self.__active = Event()

    @property
    def activate(self):
        self.__active.set()

    @property
    def deactivate(self):
        self.__active.clear()

    @property
    def active(self):
        return self.__active.is_set()


class RBFlag(Settings):
    Activation: _Activator = Field(default_factory=_Activator, exclude=True)
    flag: str
    value = ''

class RubberBandOtherFlags:
    formant: RBFlag = RBFlag(flag="--formant")
    realtime: RBFlag = RBFlag(flag="--realtime")
    no_threads: RBFlag = RBFlag(flag="--no-threads")
    threads: RBFlag = RBFlag(flag="--threads")
    no_transients: RBFlag = RBFlag(flag="--no-transients")
    bi_transients: RBFlag = RBFlag(flag="--bi-transients")
    no_lamination: RBFlag = RBFlag(flag="--no-lamination")
    window_long: RBFlag = RBFlag(flag="--window-long")
    window_short: RBFlag = RBFlag(flag="--window-short")
    smoothing: RBFlag = RBFlag(flag="--smoothing")
    detector_perc: RBFlag = RBFlag(flag="--detector-perc")
    detector_soft: RBFlag = RBFlag(flag="--detector-soft")
    pitch_hq: RBFlag = RBFlag(flag="--pitch-hq")
    centre_focus: RBFlag = RBFlag(flag="--centre-focus")
    ignore_clipping: RBFlag = RBFlag(flag="--ignore-clipping")


class R2Engine:
    def __init__(self):
        #super().__init__(**kwargs)
        self._rb_flags = RubberBandOtherFlags()
        self.flag = "--fast"
        self.value = ''
        #______________________________________________________
        self.time = RBSetting(flag="--time")
        self.tempo = RBSetting(flag="--tempo")
        self.duration = RBSetting(flag="--duration")
        self.pitch = RBSetting(flag="--pitch")
        self.frequency = RBSetting(flag="--frequency")
        #______________________________________________________
        self.timemap = RBSetting(flag="--timemap")
        self.pitchmap = RBSetting(flag="--pitchmap")
        self.freqmap = RBSetting(flag="--freqmap")
        #______________________________________________________
        self.formant = self._rb_flags.formant
        self.crisp = RBSetting(flag="--crisp", value=5)
        self.realtime = self._rb_flags.realtime
        self.no_threads = self._rb_flags.no_threads
        self.threads = self._rb_flags.threads
        self.no_transients = self._rb_flags.no_transients
        self.bi_transients = self._rb_flags.bi_transients
        self.no_lamination = self._rb_flags.no_lamination
        self.window_long = self._rb_flags.window_long
        self.window_short = self._rb_flags.window_short
        self.smoothing = self._rb_flags.smoothing
        self.detector_perc = self._rb_flags.detector_perc
        self.detector_soft = self._rb_flags.detector_soft
        self.pitch_hq = self._rb_flags.pitch_hq
        self.centre_focus = self._rb_flags.centre_focus
        self.ignore_clipping = self._rb_flags.ignore_clipping
        
        

class R3Engine:
    def __init__(self):
        self._rb_flags = RubberBandOtherFlags
        self.flag = "--fine"
        #______________________________________________________
        self.time = RBSetting(flag="--time")
        self.tempo = RBSetting(flag="--tempo")
        self.duration = RBSetting(flag="--duration")
        self.pitch = RBSetting(flag="--pitch")
        self.frequency = RBSetting(flag="--frequency")
        #______________________________________________________
        self.timemap = RBSetting(flag="--timemap")
        self.pitchmap = RBSetting(flag="--pitchmap")
        self.freqmap = RBSetting(flag="--freqmap")
        #______________________________________________________
        self.realtime = self._rb_flags.realtime
        self.pitch_hq = self._rb_flags.pitch_hq
        self.centre_focus = self._rb_flags.centre_focus
        self.ignore_clipping = self._rb_flags.ignore_clipping
        


class Engine(Enum):
    R2 = R2Engine
    R3 = R3Engine


class OptionManager(UserList):
    def __init__(self, options = None):
        super().__init__()
        self._options = options

    @property
    def options(self):
        return self._options

    @property
    def _types(self):
        return [type(item) for item in self.data]
    
    def __getitem__(self, item):
        type_exists = type(item) in self._types
        item_exists = item in self.data
        idx = self._types.index(type(item)) if type_exists else None
        if item_exists: self.data.remove(item)
        elif type_exists: self.data.remove(self.data[idx]), self.data.append(item)
        else: self.data.append(item)
        return self
    

class OptionGroup(Enum):
    
    @classmethod
    def set_option_manager(cls, option_manager: OptionManager):
        cls._option_manager = option_manager

    def __getattr__(self, name):
        """
        Return the enum member matching `name`

        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            self._option_manager[self._member_map_[name]]
            return self._member_map_[name]
        except KeyError:
            raise AttributeError(name) from None

    def __getitem__(self, name):
        return self._member_map_[name]


class Option:
    def __init__(self, option_manager: OptionManager, option: Iterable = None):
        self._option_manager = option_manager
        self._option = option

    def __call__(self):
        self._option_manager[self._option]
        return self     


class SettingsManager(UserDict):
    def __init__(self, settings: Union[dict, Settings, pdc.BaseModel, None] = None):
        super().__init__()
        if settings is None: self.__settings__ = {}
        if isinstance(settings, dict): self.__settings__ = settings
        if isinstance(settings, Settings): self.__settings__ = settings.dict()
        if isinstance(settings, pdc.BaseModel): self.__settings__ = settings.dict()
    
    @property
    def as_dictionary(self):
        return self.__settings__

    def __add__(self, other):
        if isinstance(other, SettingsManager):
            return SettingsManager({**self.__settings__, **other.__settings__})
        return SettingsManager({**self.__settings__, **other})

    def __iadd__(self, other):
        if isinstance(other, SettingsManager):
            self.__settings__ = {**self.__settings__, **other.__settings__}
        elif isinstance(other, dict):
            self.__settings__ = {**self.__settings__, **other}
        elif isinstance(other, (Settings, pdc.BaseModel)):
            self.__settings__ = {**self.__settings__, **other.dict()}
        return self
    
    def __sub__(self, other):
        if isinstance(other, SettingsManager):
            return SettingsManager({k: v for k, v in self.__settings__.items() if k not in other.__settings__})
        elif isinstance(other, (Settings, pdc.BaseModel)):
            return SettingsManager({k: v for k, v in self.__settings__.items() if k not in other.dict()})
        elif isinstance(other, str):
            return SettingsManager({k: v for k, v in self.__settings__.items() if k != other})
        return SettingsManager({k: v for k, v in self.__settings__.items() if k not in other})
    
    def __isub__(self, other):
        if isinstance(other, SettingsManager):
            self.__settings__ = {k: v for k, v in self.__settings__.items() if k not in other.__settings__}
        elif isinstance(other, (Settings, pdc.BaseModel)):
            self.__settings__ = {k: v for k, v in self.__settings__.items() if k not in other.dict()}
        elif isinstance(other, str):
            self.__settings__ = {k: v for k, v in self.__settings__.items() if k != other}
        else:
            self.__settings__ = {k: v for k, v in self.__settings__.items() if k not in other}
        return self
    
    def __setitem__(self, key, item):
        self.__settings__[key] = item
        
    
    @property
    def storage(self):
        return self.__settings__
    

class SourceMap:
    def __init__(self):
        self._source_map = None
        self._file = NamedTemporaryFile(delete=False)
        self._file_name = self._file.name

    
    def __map_to_source__(self, a, b):

        if isinstance(a, Iterable) and isinstance(b, Iterable):
            if len(a) == len(b): data = np.transpose(np.vstack((a, b)))
        else: data = np.array([[a, b]])

        if self._source_map is None: self._source_map = data
        else: self._source_map = np.vstack((self._source_map, data))

        return self._source_map
    
    def __source_to_file__(self):
        if self._file.closed: self._file = NamedTemporaryFile(delete=False)
        self._file.seek(0)
        for row in self._source_map:
            if len(row) == 2: self._file.write(f"{row[0]} {row[1]}\n".encode())
            else:
                for i in range(len(row)):
                    self._file.write(f"{row[i]} ".encode())
                self._file.write("\n".encode())
        self.__close_file__()
        return self._file.name

    def __close_file__(self):
        self._file.close()
    
    def __del_file__(self):
        if not self._file.closed: self.__close_file__()
        os.remove(self._file_name)

class SourceMapping:
    def __init__(self, func):
        wraps(func)(self)
    
    def __call__(self, wrapped_self, *args, **kwargs):
        
        result, sourcemap = self.__wrapped__(wrapped_self, *args, **kwargs)
        sourcemap.__del_file__()
        return result

class PitchMap(SourceMap):
    def __init__(self):
        super(PitchMap, self).__init__()
        self.temp_file = self._file

    @property
    def file_name(self):
        return self._file_name

    def add_to_map(self, sample_position: Union[int, list], semitone_offset: Union[int, list]):
        if sample_position and semitone_offset:
            self.__map_to_source__(sample_position, semitone_offset)

    @property
    def get_map_array(self):
        return self._source_map
    
class TimeMap(SourceMap):
    def __init__(self):
        super(TimeMap, self).__init__()
        self.temp_file = self._file

    @property
    def file_name(self):
        return self._file_name

    def add_to_map(self, origin_sample: Union[int, list], destination_sample: Union[int, list]):
        if origin_sample and destination_sample:
            self.__map_to_source__(origin_sample, destination_sample)

    @property
    def get_map_array(self):
        return self._source_map
    
class FrequencyMap(SourceMap):
    def __init__(self):
        super(FrequencyMap, self).__init__()
        self.temp_file = self._file

    @property
    def file_name(self):
        return self._file_name

    def add_to_map(self, sample_position: Union[int, list], frequency_multiplier: Union[int, list]):
        if sample_position and frequency_multiplier:
            self.__map_to_source__(sample_position, frequency_multiplier)

    @property
    def get_map_array(self):
        return self._source_map

class RubberBandSettings:

    def __init__(self):
        self.engines = Engine
        self._settings = SettingsManager()
        self._engine = self.engines.R2.value()
        
    @property
    def use_R2_engine(self):
        self._engine = self.engines.R2.value()
        flag = self._engine.flag
        null_val = self._engine.value
        self._settings[flag] = null_val
        return self._engine

    @property
    def use_R3_engine(self):
        self._engine = self.engines.R3.value()
        flag = self._engine.flag
        null_val = self._engine.value
        self._settings[flag] = null_val
        return self._engine
    
    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, engine):
        if isinstance(engine, Engine):
            self._engine = engine()
        else:
            raise TypeError(f"Engine must be of type {Engine}")
    
    def __compile__(self):
        engine_settings = self._engine.__dict__
        for s in engine_settings.values():
            if isinstance(s, (RBFlag, RBSetting)):
                if isinstance(s, RBFlag): selected = bool(s.Activation.active)
                elif isinstance(s, RBSetting): selected = bool(s.value)
            else: selected = False
            if selected:
                fv = {s.flag: s.value}
                self._settings += fv

        return self._settings.as_dictionary


