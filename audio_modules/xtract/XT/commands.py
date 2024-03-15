from __future__ import annotations
from typing import TYPE_CHECKING
from parselmouth.praat import call
from typing import TypeVar
from .xtract_configs import *
from .xtract_configs import PraatCommand
if TYPE_CHECKING: from .core import Feature

FeatureType = TypeVar('FeatureType', bound='Feature')

class PraatCommands:
    def __init__(self, input):
        self.input = input

    def unwrap(self, settings: Settings):
        args = [s for k, s in settings.dict().items() if not k.startswith('__')]
        return args
    
    def annotate_silence(self, settings: Settings=Silence()):
        command = PraatCommand(
            name='To TextGrid (silences)...', 
            arguments=self.unwrap(settings)
        )
        return self._run(command)
    
    def annotate_voiced(self, settings: Settings=VoiceDetection()):
        command = PraatCommand(
            name='To TextGrid (voice activity)...', 
            arguments=self.unwrap(settings)
        )
        return self._run(command)
    
    def count_voiced_frames(self):
        command = PraatCommand(
            name='Count voiced frames'
        )
        return self._run(command)
    
    def get_value_at_time(self, time: float):
        command = PraatCommand(
            name='Get value at time...', 
            arguments=[time]
        )
        return self._run(command)
    
    def get_value_at_index(self, index: int):
        command = PraatCommand(
            name='Get value at index...', 
            arguments=[index]
        )
        return self._run(command)
    
    def get_time_at_index(self, index: int):
        command = PraatCommand(
            name='Get time from index...', 
            arguments=[index]
        )
        return self._run(command)
    
    def get_number_of_points(self):
        command = PraatCommand(
            name='Get number of points'
        )
        return self._run(command)
    
    def get_nearest_index_from_time(self, time: float):
        command = PraatCommand(
            name='Get nearest index from time...', 
            arguments=[time]
        )
        return self._run(command)
    
    def get_resynthesis_with_overlap(self):
        command = PraatCommand(
            name='Get resynthesis (overlap-add)'
        )
        return self._run(command)

    def filter_hann_stop(self, start_freq: float, stop_freq: float, smoothing: float=100.0):
        command = PraatCommand(
            name='Filter (stop Hann band)...', 
            arguments=[start_freq, stop_freq, smoothing]
        )
        return self._run(command)
    
    def filter_hann_pass(self, start_freq: float, stop_freq: float, smoothing: float=100.0):
        command = PraatCommand(
            name='Filter (pass Hann band)...', 
            arguments=[start_freq, stop_freq, smoothing]
        )
        return self._run(command)
    
    def filter_reduce_noice(self, settings: Settings = None):
        if not settings: settings = AnalysisSettings.NoiceReduction
        command = PraatCommand(
            name='Reduce noise...', 
            arguments=self.unwrap(settings)
        )

    def filter_pre_emphasis(self, start_frequency: float=50.0):
        command = PraatCommand(
            name='Filter (pre-emphasis)...', 
            arguments=[start_frequency]
        )
        return self._run(command)
    
    def filter_de_emphasis(self, start_frequency: float=50.0):
        command = PraatCommand(
            name='Filter (de-emphasis)...', 
            arguments=[start_frequency]
        )
        return self._run(command)

    def time_of_minimum(
            self, 
            interpolation: Interpolation = Interpolation(), 
            unit: Unit = Unit.Hertz
            ):
        args = self.unwrap(interpolation)
        args.insert(2, unit.value)
        command = PraatCommand(
            name='Time of minimum...',
            arguments=args
        )
        return self._run(command)
    
    def time_of_maximum(
            self, 
            interpolation: Interpolation = Interpolation(), 
            unit: Unit = Unit.Hertz
            ):
        accepted_units = [
            Unit.Hertz,
            Unit.HertzLogarithmic,
            Unit.LogHertz, 
            Unit.SemitonesRe1Hz,
            Unit.SemitonesRe100Hz,
            Unit.SemitonesRe200Hz,
            Unit.SemitonesRe440Hz,
            Unit.Mel, 
            Unit.ERB
            ]
        if unit not in accepted_units:
            raise Exception(f'Unit {unit} not supported for time of maximum')
        args = self.unwrap(interpolation)
        args.insert(2, unit.value)
        command = PraatCommand(
            name='Time of maximum...',
            arguments=args
        )
        return self._run(command)
    
    def mean_absolute_slope(self, unit: Unit = Unit.Hertz):
        accpeted_units = [Unit.Hertz, Unit.Semitones, Unit.Mel, Unit.ERB]
        if unit not in accpeted_units:
            raise Exception(f'Unit {unit} not supported for mean absolute slope')
        command = PraatCommand(
            name='Get mean absolute slope...',
            arguments=[unit.value]
        )
        return self._run(command)

    def to_klatt_grid_simple(self, arguments=None):
        if not arguments: arguments = [0.005, 5, 5500, 0.025, 50.0, 60.0, 600.0, 100.0, 'yes']
        command = PraatCommand(
            name='To KlattGrid (simple)...', 
            arguments=arguments,
            arg_help=[
            f'1. Time Step: {arguments[0]}',
            f'2. Max Number of Formants: {arguments[1]}',
            f'3. Formant Ceiling (Hz): {arguments[2]}',
            f'4. Window Length: {arguments[3]}',
            f'5. Pre-emphasis from: {arguments[4]} Hz',
            f'6. Pitch Floor: {arguments[5]} Hz',
            f'7. Pitch Ceiling: {arguments[6]} Hz',
            f'8. Minimum Pitch: {arguments[7]} Hz',
            f'9. Subtract Mean?: {arguments[8]}'
            ]
        )
        return self._run(command)
    
    def to_manipulation(self, Tstep=0.01, Pmin= 75.0, Pmax=600.0, from_pitch=None):
        if from_pitch:
            self.input = [self.input, from_pitch]
            arguments = None
            command = PraatCommand(
                name='To Manipulation',
                arguments=arguments
            )
            return self._run(command)

        arguments = [Tstep, Pmin, Pmax]
        command = PraatCommand(
            name='To Manipulation...', 
            arguments=arguments,
            arg_help=[
            f'1. Time Step: {arguments[0]}',
            f'2. Pitch Floor: {arguments[1]} Hz',
            f'3. Pitch Ceiling: {arguments[2]} Hz',
            ]
        )
        return self._run(command)
    
    def to_matrix(self, column_index=None):
        arguments = [column_index]
        if column_index:
            command = PraatCommand(
                name='To Matrix...', 
                arguments=arguments
            )
            return self._run(command)
        command = PraatCommand(
            name='To Matrix', 
            arguments=None
        )
        return self._run(command)
    
    def to_formant(self, arguments=None):
        if not arguments: arguments = [0.01, 0.1]
        command = PraatCommand(
            name='To Formant...', 
            arguments=arguments
        )
        return self._run(command)
    
    def to_text_grid_vuv(self, arguments=None):
        if not arguments: arguments = [0.02, 0.01]
        command = PraatCommand(
            name='To TextGrid (vuv)...', 
            arguments=arguments
        )
        return self._run(command)
    
    def to_table(self, arguments=None):
        if not arguments: arguments = ['Index']
        command = PraatCommand(
            name='To Table...', 
            arguments=['Index']
        )
        return self._run(command)
    
    def to_pointprocess_cc(self, pitch):
        self.input = [self.input, pitch]
        command = PraatCommand(
            name='To PointProcess (cc)', 
            arguments=None
        )
        return self._run(command)
    
    def to_pointprocess_periodic_cc(self, pitch=None, pitch_floor=75.0, pitch_ceiling=600.0):
        arguments = None
        if pitch: 
            self.input = [self.input, pitch]
            command_name = 'To PointProcess (cc)'
        else: 
            arguments = [pitch_floor, pitch_ceiling]
            command_name = 'To PointProcess (periodic, cc)...'
        command = PraatCommand(
            name=command_name, 
            arguments=arguments
        )
        return self._run(command)
    
    def to_cochleagram(self, Tstep=0.01, BarkFR=0.1, Wlen=0.03, FwMaskT=0.03):
        arguments = [Tstep, BarkFR, Wlen, FwMaskT]
        command = PraatCommand(
            name='To Cochleagram...', 
            arguments=arguments
        )
        return self._run(command)
    
    def to_pitch_fb_spectrogram(
            self, 
            Pitch = None,
            analysis_Wdur=0.015, 
            Tstep=0.005, 
            pos_filter1=100.0, 
            filter_distance=50.0, 
            max_Freq=0, 
            relative_band=1.1
            ):
        if Pitch: self.input = [self.input, Pitch]
        arguments = [analysis_Wdur, Tstep, pos_filter1, filter_distance, max_Freq, relative_band]
        command = PraatCommand(
            name='To Spectrogram (pitch-dependent)...',
            arguments=arguments
        )
        return self._run(command)
    
    def to_bark_spectrogram(
            self, 
            Wlen=0.015, 
            Tstep=0.005, 
            pos_filter1=1.0, 
            filter_distance=1.0, 
            max_freq=0.0
            ):
        arguments = [Wlen, Tstep, pos_filter1, filter_distance, max_freq]
        command = PraatCommand(
            name='To BarkSpectrogram...',
            arguments=arguments
        )
        return self._run(command)
    
    def to_mel_spectrogram(
            self, 
            Wlen=0.015, 
            Tstep=0.005, 
            pos_filter1=100.0, 
            filter_distance=100.0, 
            max_freq=0.0
            ):
        arguments = [Wlen, Tstep, pos_filter1, filter_distance, max_freq]
        command = PraatCommand(
            name='To MelSpectrogram...',
            arguments=arguments
        )
        return self._run(command)
    
    def to_power_cepstrogram(self, Pfloor=60.0, Tstep=0.002, max_freq=5000.0, pre_emphasis=50.0):
        arguments = [Pfloor, Tstep, max_freq, pre_emphasis]
        command = PraatCommand(
            name='To PowerCepstrogram...',
            arguments=arguments
        )
        return self._run(command)
    
    def to_intensitytier_peaks(self):
        command = PraatCommand(
            name='To IntensityTier (peaks)',
            arguments=None
        )
        return self._run(command)
    
    def to_intensitytier_valleys(self):
        command = PraatCommand(
            name='To IntensityTier (valleys)',
            arguments=None
        )
        return self._run(command)
    
    def to_amplitudetier(self):
        command = PraatCommand(
            name='To AmplitudeTier',
            arguments=None
        )
        return self._run(command)
    
    def down_to_intensitytier(self):
        command = PraatCommand(
            name='Down to IntensityTier',
            arguments=None
        )
        return self._run(command)

    def change_gender(
            self, 
            pitch=None, 
            min_pitch=75.0,
            max_pitch=600.0,
            fmt_shift_ratio=1.1, 
            pitch_median=0.0, 
            pitch_range=1.0, 
            duration=1.0
            ):
        if pitch: self.input = [self.input, pitch]
        if pitch or len(self.input) == 2: arguments = [fmt_shift_ratio, pitch_median, pitch_range, duration]
        else: arguments = [min_pitch, max_pitch, fmt_shift_ratio, pitch_median, pitch_range, duration]
        command = PraatCommand(
            name='Change gender...',
            arguments=arguments
        )
        return self._run(command)

    
    def voice_report(
            self, 
            pitch_and_pointprocess = None,
            time_range_start=0.0, 
            time_range_end=0.0,
            pitch_floor=75.0,
            pitch_ceiling=600.0,
            max_period_factor=1.3,
            max_amp_factor=1.6,
            silence_threshold=0.03,
            voicing_threshold=0.45
            ):
        arguments = [
            time_range_start,
            time_range_end,
            pitch_floor,
            pitch_ceiling,
            max_period_factor,
            max_amp_factor,
            silence_threshold,
            voicing_threshold
        ]
        if pitch_and_pointprocess: self.input = pitch_and_pointprocess.append(self.input)
        else: 
            pitch = self.input.to_pitch_cc()
            pointprocess = self.to_pointprocess_cc(pitch).result
            self.input = self.input + [pointprocess]
        command = PraatCommand(
            name='Voice report', 
            arguments=arguments
        )
        return self._run(command)
    
    def down_to_matrix(self):
        command = PraatCommand(
            name='Down to Matrix', 
            arguments=None
        )
        return self._run(command)
    
    def down_to_pointprocess(self):
        command = PraatCommand(
            name='Down to PointProcess', 
            arguments=None
        )
        return self._run(command)
    
    def down_to_pitch_tier(self):
        command = PraatCommand(
            name='Down to PitchTier', 
            arguments=None
        )
        return self._run(command)
    
    def down_to_table_of_real(self, arguments=None):
        if not arguments: arguments = ['Hertz']
        command = PraatCommand(
            name='Down to TableOfReal...', 
            arguments=['Hertz']
        )
        return self._run(command)
    
    def down_to_table(self):
        arguments = ['yes', 6, 'yes', 'no']
        command = PraatCommand(
            name='Down to Table...', 
            arguments=arguments
        )
        return self._run(command)
    
    def extract_pitch(self):
        command = PraatCommand(
            name='Extract pitch tier', 
            arguments=None
        )
        return self._run(command)
    
    def extract_pitch_tier(self):
        command = PraatCommand(
            name='Extract pitch tier', 
            arguments=None
        )
        return self._run(command)
    
    def extract_pulses(self):
        command = PraatCommand(
            name='Extract pulses', 
            arguments=None
        )
        return self._run(command)
    
    def extract_duration_tier(self):
        command = PraatCommand(
            name='Extract duration tier', 
            arguments=None
        )
        return self._run(command)

    def extract_voicing_amplitude(self):
        command = PraatCommand(
            name='Extract voicing amplitude tier',
            arguments=None
        )
        return self._run(command)
    
    def extract_flutter(self):
        command = PraatCommand(
            name='Extract flutter tier',
            arguments=None
        )
        return self._run(command)
    
    def extract_power1(self):
        command = PraatCommand(
            name='Extract power1 tier',
            arguments=None
        )
        return self._run(command)
    
    def extract_power2(self):
        command = PraatCommand(
            name='Extract power2 tier',
            arguments=None
        )
        return self._run(command)
    
    def extract_open_phase(self):
        command = PraatCommand(
            name='Extract open phase tier',
            arguments=None
        )
        return self._run(command)
    
    def extract_collision_phase(self):
        command = PraatCommand(
            name='Extract collision phase tier',
            arguments=None
        )
        return self._run(command)
    
    def extract_double_pulsing(self):
        command = PraatCommand(
            name='Extract double pulsing tier',
            arguments=None
        )
        return self._run(command)
    
    def extract_spectral_tilt(self):
        command = PraatCommand(
            name='Extract spectral tilt tier',
            arguments=None
        )
        return self._run(command)
    
    def extract_aspiration_amplitude(self):
        command = PraatCommand(
            name='Extract aspiration amplitude tier',
            arguments=None
        )
        return self._run(command)
    
    def extract_breathiness_amplitude(self):
        command = PraatCommand(
            name='Extract breathiness amplitude tier',
            arguments=None
        )
        return self._run(command)
    
    def extract_oral_formants(self):
        command = PraatCommand(
            name='Extract oral formant grid',
            arguments=None
        )
        return self._run(command)

    def extract_oral_formant_open_phases(self, arguments=None):
        if not arguments: arguments = ['0.1']
        command = PraatCommand(
            name='Extract oral formant grid (open phases)...',
            arguments=arguments,
            arg_help=[f'1. Fade fraction:{arguments}']
        )
        return self._run(command)

    def extract_oral_formant_amplitude(self, arguments=None):
        if not arguments: arguments = ['1']
        command = PraatCommand(
            name='Extract oral formant amplitude tier...',
            arguments=arguments,
            arg_help=[f'1. Number of Formants:{arguments}']
        )
        return self._run(command)

    def extract_nasal_formants(self):
        command = PraatCommand(
            name='Extract nasal formant grid',
            arguments=None
        )
        return self._run(command)

    def extract_nasal_formant_amplitude(self, arguments=None):
        if not arguments: arguments = ['1']
        command = PraatCommand(
            name='Extract nasal formant amplitude tier...',
            arguments=arguments,
            arg_help=[f'1. Number of Formants:{arguments}']
        )
        return self._run(command)

    def extract_nasal_antiformants(self):
        command = PraatCommand(
            name='Extract nasal antiformant grid',
            arguments=None
        )
        return self._run(command)

    def extract_delta_formants(self):
        command = PraatCommand(
            name='Extract delta formant grid',
            arguments=None
        )
        return self._run(command)

    def extract_tracheal_formants(self):
        command = PraatCommand(
            name='Extract tracheal formant grid',
            arguments=None
        )
        return self._run(command)

    def extract_tracheal_formant_amplitude(self, arguments=None):
        if not arguments: arguments = ['1']
        command = PraatCommand(
            name='Extract tracheal formant amplitude tier...',
            arguments=arguments,
            arg_help=[f'1. Number of Formants:{arguments}']
        )
        return self._run(command)

    def extract_tracheal_antiformants(self):
        command = PraatCommand(
            name='Extract tracheal antiformant grid',
            arguments=None
        )
        return self._run(command)

    def extract_frication_formant(self):
        command = PraatCommand(
            name='Extract frication formant grid',
            arguments=None
        )
        return self._run(command)

    def extract_frication_formant_amplitude(self, arguments=None):
        if not arguments: arguments = ['1']
        command = PraatCommand(
            name='Extract frication formant amplitude tier...',
            arguments=arguments,
            arg_help=[f'1. Number of Formants:{arguments}']
        )
        return self._run(command)

    def extract_frication_bypass(self):
        command = PraatCommand(
            name='Extract frication bypass tier',
            arguments=None
        )
        return self._run(command)
    
    def extract_frication_amplitude(self):
        command = PraatCommand(
            name='Extract frication amplitude tier',
            arguments=None
        )
        return self._run(command)
    
    def get_number_of_formants_in_frame(self, arguments=None):
        if not arguments: arguments = ['1']
        command = PraatCommand(
            name='Get number of formants...',
            arguments=arguments,
            arg_help=[f'1. Frame to pull formants from:{arguments}']
        )
        return self._run(command)
    
    def multiply(self, intensity, scale='yes'):
        self.input = [self.input, intensity]
        arguments = [scale]
        command = PraatCommand(
            name='Multiply...',
            arguments=arguments
        )
        return self._run(command)

    def replace_pitch_tier(self, Ptier2):
        manipulation = self.input
        self.input = [self.input, Ptier2]
        command = PraatCommand(
            name='Replace pitch tier',
            arguments=None
        )
        result = self._run(command)
        if result.result is None:
            result.result = manipulation
            print(type(result.result))
        return result

    def replace_duration_tier(self, Dtier2):
        self.input = [self.input, Dtier2]
        command = PraatCommand(
            name='Replace duration tier',
            arguments=None
        )
        return self._run(command)
    
    def replace_pulses(self, Pprocess):
        self.input = [self.input, Pprocess]
        command = PraatCommand(
            name='Replace pulses',
            arguments=None
        )
        return self._run(command)
    
    def shift_time_by(self, Tamount):
        arguments = [Tamount]
        command = PraatCommand(
            name='Shift times by...',
            arguments=arguments,
        )
        return self._run(command)
    
    def shift_time_to(self, pos, newT):
        pos_options = ['start time', 'centre time', 'end time']
        if pos not in pos_options:
            raise ValueError(f'pos must be one of {pos_options}')
        arguments = [pos, newT]
        command = PraatCommand(
            name='Shift times to...',
            arguments=arguments,
            arg_help=['1. Position to shift to:', '2. New time:']
        )
        return self._run(command)
    
    def scale_time_by(self, Sfactor):
        arguments = [Sfactor]
        command = PraatCommand(
            name='Scale times by...',
            arguments=arguments,
        )
        return self._run(command)
    
    def scale_time_to(self, newSTime, newETime):
        arguments = [newSTime, newETime]
        command = PraatCommand(
            name='Shift times to...',
            arguments=arguments
        )
        return self._run(command)

    def _run(self, command: PraatCommand):
        if command.arguments:
            command.result = call(self.input, command.name, *command.arguments)
            return command
        else:
            command.result = call(self.input, command.name)
            return command