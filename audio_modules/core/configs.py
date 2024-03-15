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
import types


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


class MethodDecoratorBase:
    
    def __init__(self, method):
        self.method = method
        self.args = None
        self.kwargs = None
        

    def __call__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        
    @property
    def instance(self):
        if not self.is_instance:
            raise TypeError("Method must be accessed from instance")
        return self.args[0]

    def __get__(self, instance, objtype=None):
        if instance is None:
            self.is_instance = False
            return self  # Accessed from class, return unchanged
        self.is_instance = True
        return types.MethodType(self, instance)  # Accessed from instance, bind to instance