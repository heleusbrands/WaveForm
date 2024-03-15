import numpy as np
import parselmouth as pm
from typing import Union, TypeVar
from audio_modules.xtract.XT.core import *
from audio_modules.xtract.XT.xtract_configs import *
from audio_modules.xtract.XT.commands import PraatCommands

FeatureType = TypeVar('FeatureType', bound='Feature')


class PhonationGrid(Grid):
    def __init__(self, grid):
        self.parent_grid = grid
        self.pci = PraatCommands(grid)

    def create_collection(self):
        return CollectionMatrix(
            features=[
                self.pitch,
                self.flutter,
                self.voicing_amplitude,
                self.double_pulsing,
                self.open_phase(),
                self.collision_phase(),
                self.power1(),
                self.power2()],
            name='Phonation Grid')

    @property
    def pitch(self):
        col_names = ['Time', 'Pitch: Hz']
        return Feature(self._extract(self.pci.extract_pitch().result), col_names, 'Pitch')

    @property
    def flutter(self):
        col_names = ['Time', 'Pitch: Flutter']
        return Feature(self._extract(self.pci.extract_flutter().result), col_names, 'Flutter')

    @property
    def voicing_amplitude(self):
        col_names = ['Time', 'Voicing Amp: DB SPL']
        return Feature(self._extract(self.pci.extract_voicing_amplitude().result), col_names, 'Voicing Amplitude')

    @property
    def double_pulsing(self):
        col_names = ['Time', 'Double Pulsing']
        return Feature(self._extract(self.pci.extract_double_pulsing().result), col_names, 'Double Pulsing')

    @property
    def open_phase(self):
        col_names = ['Time', 'Open Phase']
        return Feature(self._extract(self.pci.extract_open_phase().result), col_names, 'Open Phase')

    @property
    def collision_phase(self):
        col_names = ['Time', 'Collision Phase']
        return Feature(self._extract(self.pci.extract_collision_phase().result), col_names, 'Collision Phase')

    @property
    def power1(self):
        col_names = ['Time', 'Power 1']
        return Feature(self._extract(self.pci.extract_power1().result), col_names, 'Power 1')

    @property
    def power2(self):
        col_names = ['Time', 'Power 2']
        return Feature(self._extract(self.pci.extract_power2().result), col_names, 'Power 2')

class FormantFilters(Grid):
    def __init__(self, grid):
        self.parent_grid = grid
        self.pci = PraatCommands(grid)

    def create_collection(self):
        '''It creates a collection of formant filters, which are used to filter the speech signal
        
        Returns
        -------
            A CollectionMatrix object.
        
        '''

        return CollectionMatrix(
            features=[
                self.oral_formant(), 
                self.oral_formant_open_phases(), 
                self.oral_formant_amplitude(), 
                self.nasal_formant(), 
                self.nasal_formant_open_phases(), 
                self.nasal_formant_amplitude(), 
                self.nasal_antiformant(), 
                self.delta_formant(),
                self.tracheal_formant(),
                self.tracheal_formant_open_phases(),
                self.tracheal_formant_amplitude(),
                self.tracheal_antiformant(),
                self.frication_formant(),  
                self.frication_bypass(),
                self.frication_formant_amplitude(),
                self.frication_amplitude()],
            name='Formant Filters')

    def oral_formant(self):
        col_names = ['Time', 'Formant']
        return Feature(self._extract(self.pci.extract_oral_formants().result), col_names, 'Oral Formant')

    def oral_formant_open_phases(self):
        col_names = ['Time', 'Formant Open Phase']
        return Feature(self._extract(self.pci.extract_oral_formant_open_phases().result), col_names, 'Oral Formant Open Phases')

    def oral_formant_amplitude(self):
        col_names = ['Time', 'Amplitude: dB']
        return Feature(self._extract(self.pci.extract_oral_formant_amplitude().result), col_names, 'Oral Formant Amplitude')

    def nasal_formant(self):
        col_names = ['Time', 'Nasal Formant']
        return Feature(self._extract(self.pci.extract_nasal_formants().result), col_names, 'Nasal Formant')

    def nasal_formant_amplitude(self):
        col_names = ['Time', 'Nasal Formant Amplitude']
        return Feature(self._extract(self.pci.extract_nasal_formant_amplitude().result), col_names, 'Nasal Formant Amplitude')

    def nasal_antiformant(self):
        col_names = ['Time', 'Nasal Antiformant']
        return Feature(self._extract(self.pci.extract_nasal_antiformants().result), col_names, 'Nasal Antiformant')

    def delta_formant(self):
        col_names = ['Time', 'Delta Formant']
        return Feature(self._extract(self.pci.extract_delta_formants().result), col_names, 'Delta Formant')

    def tracheal_formant(self):
        col_names = ['Time', 'Tracheal Formant']
        return Feature(self._extract(self.pci.extract_tracheal_formants().result), col_names, 'Tracheal Formant')

    def tracheal_formant_amplitude(self):
        col_names = ['Time', 'Tracheal Formant Amplitude']
        return Feature(self._extract(self.pci.extract_tracheal_formant_amplitude().result), col_names, 'Tracheal Formant Amplitude')

    def tracheal_antiformant(self):
        col_names = ['Time', 'Tracheal Antiformant']
        return Feature(self._extract(self.pci.extract_tracheal_antiformants().result), col_names, 'Tracheal Antiformant')

    def frication_formant(self):
        col_names = ['Time', 'Friction Formant']
        return Feature(self._extract(self.pci.extract_frication_formant().result), col_names, 'Frication Formant')

    def frication_formant_amplitude(self):
        col_names = ['Time', 'Friction Formant Amplitude']
        return Feature(self._extract(self.pci.extract_frication_formant_amplitude().result), col_names, 'Frication Formant Amplitude')

    def frication_bypass(self):
        col_names = ['Time', 'Friction Bypass']
        return Feature(self._extract(self.pci.extract_frication_bypass().result), col_names, 'Frication Bypass')

    def frication_amplitude(self):
        col_names = ['Time', 'Friction Amplitude']
        return Feature(self._extract(self.pci.extract_frication_amplitude().result), col_names, 'Frication Amplitude')

class KlattGrid:
    
    def __init__(self, sound: pm.Sound, args: Union[list, None]=None, create_on_init=True):
        '''The function takes a sound object and a list of arguments, and creates a KlattGrid object
        
        Parameters
        ----------
        sound : pm.Sound
            pm.Sound
        args : Union[list, None]
            list of arguments to pass to the Praat script
        create_on_init, optional
            bool = True
        
        '''
       
        self.sound = sound
        self.pci = PraatCommands(self.sound)
        self._grid = self.pci.to_klatt_grid_simple(arguments=args).result
        self.PhonationGrid = PhonationGrid(self._grid)
        self.FormantFilters = FormantFilters(self._grid)

    @property
    def collect_phonation(self):
        """
        Collects the phonation data from the phonation grid and returns it as a collection
        :return: The collection of phonation data.
        """
        return self.PhonationGrid.create_collection()
    
    @property
    def collect_formant_filters(self):
        """
        Creates a collection of formant filters from the formant filters in the current object
        :return: The collection of formant filters.
        """
        return self.FormantFilters.create_collection()
    
    @property
    def collect_all(self):
        """
        It returns a tuple of collections that are defined in the class
        :return: A tuple of functions.
        """
        return (self.collect_phonation, self.collect_formant_filters)

class ManipulationGrid(Grid):
    def __init__(self, sound: pm.Sound, *args):
        '''The function takes a sound object and a list of arguments, and returns a Manipulation object
        
        Parameters
        ----------
        sound : pm.Sound
            the sound object
        
        '''
        self.sound = sound
        self.pci = PraatCommands(self.sound)
        self.time_step = 0.01
        self.pitch_floor = 75.0
        self.pitch_ceiling = 600.0
        if args: self._manipulation = self.pci.to_manipulation(arguments=args).result
        else: self._manipulation = self.pci.to_manipulation(
                self.time_step, 
                self.pitch_floor, 
                self.pitch_ceiling
                ).result
            
    @property
    def pulses(self):
        '''It takes the Praat output of the pulses command and converts it into a feature
        
        Returns
        -------
            A feature containing a dataframe with the pulse time index.
        
        '''
        pci = PraatCommands(self._manipulation)
        col_names = ['Pulse Time Index']
        name = 'Pulses'
        return self._to_feature(pci.extract_pulses().result, col_names, name, 'data')
    
    @property
    def pitch(self):
        pci = PraatCommands(self._manipulation)
        col_names = ['Time', 'Pitch']
        name = 'Pitch'
        return self._to_feature(pci.extract_pitch().result, col_names, name, 'data')
    
    @property
    def time(self):
        pci = PraatCommands(self._manipulation)
        col_names = ['Time']
        name = 'Time'
        return self._to_feature(pci.extract_duration_tier().result, col_names, name)
    
    @property
    def adjust_voicing(
            self, 
            pitch_curve=None,
            pitch_floor=75.0,
            pitch_ceiling=600.0,
            pitch_median=0.0,
            pitch_range_ratio=1.0,
            formant_shift_ratio=1.0, 
            duration_ratio=1.0
            ):
        '''This function takes a sound object and returns a new sound object with the pitch curve, pitch
        floor, pitch ceiling, pitch median, pitch range ratio, formant shift ratio, and duration ratio
        adjusted
        
        Parameters
        ----------
        pitch_curve
            a pitch feature
        pitch_floor
            The lowest pitch in Hz that the pitch curve can reach.
        pitch_ceiling
            The highest pitch in Hz that the sound can be adjusted to.
        pitch_median
            The median pitch of the output sound.
        pitch_range_ratio
            The ratio of the pitch range of the output sound to the pitch range of the input sound.
        formant_shift_ratio
            The ratio of the formant shift. 1.0 means no change.
        duration_ratio
            The ratio of the duration of the output sound to the duration of the input sound.
        
        Returns
        -------
            A Feature object
        
        '''
        pci = PraatCommands(self.sound)
        col_names = ['Samples']
        name = 'Adjusted Sound'
        return self._to_feature(
            pci.change_gender(
                pitch=pitch_curve, 
                min_pitch=pitch_floor, 
                max_pitch=pitch_ceiling, 
                fmt_shift_ratio=formant_shift_ratio, 
                pitch_median=pitch_median, 
                pitch_range=pitch_range_ratio, 
                duration=duration_ratio
            ).result, col_names, name, 'sound'
        )


class FilterGrid(Grid):
    def __init__(self, sound):
        super().__init__(sound)

    def hann_stop(self, start_frequency, end_frequency, smoothing:float = 100) -> pm.Sound:
        """
        This function takes a start and end value and creates a Hann stop filter
        :param start: The start value of the filter
        :param end: The end value of the filter
        :return: A Hann stop filter
        """
        return self.pci.filter_hann_stop(start_frequency, end_frequency, smoothing).result
    
    def hann_pass(self, start_frequency, end_frequency, smoothing:float = 100) -> pm.Sound:
        """
        This function takes a start and end value and creates a Hann pass filter
        :param start: The start value of the filter
        :param end: The end value of the filter
        :return: A Hann pass filter
        """
        return self.pci.filter_hann_pass(start_frequency, end_frequency, smoothing).result
    
    def pre_emphasis(self, from_frequency=50) -> pm.Sound:
        """
        This function takes a coefficient and creates a pre-emphasis filter
        :param coefficient: The coefficient of the filter
        :return: A pre-emphasis filter
        """
        return self.pci.filter_pre_emphasis(from_frequency).result
    
    def de_emphasis(self, from_frequency=50) -> pm.Sound:
        """
        This function takes a coefficient and creates a de-emphasis filter
        :param coefficient: The coefficient of the filter
        :return: A de-emphasis filter
        """
        return self.pci.filter_de_emphasis(from_frequency).result

class AnalysisGrid(Grid):

    """
    This is a class that is used to store information about the grid that is used for analysis.
    It stores information about the sound that is being analyzed, as well as the settings
    for the analysis. 

    AnalysisGrid.settings:
        Use this to configure the settings for the different analysis functions. 
            AnalysisGrid.settings.Pitch
            AnalysisGrid.settings.Intensity
            AnalysisGrid.settings.Power_Cepstrogram
            AnalysisGrid.settings.Cochleagram
            AnalysisGrid.settings.Silence
            AnalysisGrid.settings.Voice_Detection
    """

    def __init__(self, sound: Union[pm.Sound, pm.Matrix]):
        '''The class takes a sound or a matrix as an argument and assigns it to the sound attribute of
        the class, and offers a large number of analysis functions and features, acting as a conduit to the
        PraatCommands interface. 

        Use AnalysisGrid.settings to configure the settings for the analysis functions.
        
        Parameters
        ----------
        sound : Union[pm.Sound, pm.Matrix]
            Union[pm.Sound, pm.Matrix]
        
        '''
        if type(sound) == pm.Sound: self.sound: pm.Sound = sound
        elif type(sound) == str: self.sound = pm.Sound(sound)
        elif type(sound) == pm.Matrix: self.sound = sound
        else: raise TypeError(f'The sound must be a sound object, a string, or a matrix object. Type is: {type(sound)}')
        # Creates a PraatCommands object called pci, which is preloaded with the sound. 
        self.pci = PraatCommands(self.sound)
        # Creates an instance of the AnalysisSettings class.
        self.settings = AnalysisSettings()
        self.interpolation_settings = Interpolation()
        self.interpolation_types = InterpolationType
        self.unit_types = Unit

    @property
    def set(self):
        """Returns the settings for the analysis functions."""
        return self.settings
    
    def set_universal_time_step_to(self, value):
        """Sets the time step for all analysis functions to the same value."""
        for k in self.settings.dict().keys():
            subsetting = getattr(self.settings, k)
            if hasattr(subsetting, 'time_step'):
                subsetting.time_step = value

    @property
    def voice_report(self):
        return VoiceReport(self.sound)
    
    @property
    def filters(self):
        return FilterGrid(self.sound)

    @property
    def pitch(self):
        """
        It takes a sound object, and returns a feature object. 
        
        The feature object contains the following: 
        
        - A pandas dataframe with the following columns: Time, Frequency, Strength
        - A name for the feature
        - A numpy array with the same data as the dataframe
        
        The feature is also saved in the settings object. 
        
        The settings object is a class that contains all the settings for the feature extraction. 
        
        :return: A Feature object.
        """
        pitch = self.sound.to_pitch_cc(
            self.settings.Pitch.time_step, 
            self.settings.Pitch.pitch_floor, 
            self.settings.Pitch.max_candidates, 
            self.settings.Pitch.very_accurate, 
            self.settings.Pitch.silence_threshold, 
            self.settings.Pitch.voicing_threshold, 
            self.settings.Pitch.octave_cost, 
            self.settings.Pitch.octave_jump_cost, 
            self.settings.Pitch.voiced_unvoiced_cost, 
            self.settings.Pitch.pitch_ceiling
        )
        pitch_time = pitch.xs()
        pitch_frequency = pitch.selected_array['frequency']
        pitch_strength = pitch.selected_array['strength']
        pitch_array = np.array([pitch_time, pitch_frequency, pitch_strength]).T
        col_names = ['Time', 'Frequency', 'Strength']
        feat = Feature(pitch, col_names, 'Pitch', pitch_array)
        self.settings.Pitch._saved_feature = feat
        return feat

    def pulses(self, pitch: Feature=None):
        if pitch is not None: pitch = pitch._matrix
        elif self.settings.Pitch._saved_feature is not None: pitch = self.settings.Pitch._saved_feature._matrix
        else: pitch = self.pitch()._matrix
        pci = PraatCommands(self.sound)
        pulses = pci.to_pointprocess_cc(pitch).result
        pulses = self._extract(pulses, 'data')
        col_names = ['Pulse Time']
        feat = Feature(pulses, col_names, 'Pulses')
        return feat

    @property
    def intensity(self):
        intensity = self.sound.to_intensity(
            self.settings.Intensity.min_frequency, 
            self.settings.Intensity.time_step, 
            self.settings.Intensity.subtract_mean_pressure
            )
        col_names = ['Intensity']
        feat = Feature(intensity, col_names, 'Intensity')
        self.settings.Intensity._saved_feature = feat
        return feat
    
    def intensity_peaks(self):
        intensity = self.intensity._matrix
        pci = PraatCommands(intensity)
        peaks = pci.to_intensitytier_peaks().result
        pci = PraatCommands(peaks)
        point_count = pci.get_number_of_points().result
        peaks = [pci.get_value_at_index(i+1).result for i in range(point_count)]
        times = [pci.get_time_at_index(i+1).result for i in range(point_count)]
        peaks = np.array([times, peaks]).T
        col_names = ['Time', 'Peak Intensity']
        feat = Feature(peaks, col_names, 'Intensity Peaks', manual_array=peaks)
        return feat

    @property
    def power_cepstrogram(self):
        """
        What is a power cepstrogram?
            The power cepstrogram is a 2D representation of the power spectrum of a sound. 
            It is calculated by taking the log of the power spectrum and then taking the 
            discrete cosine transform. 
            
        Why use a power cepstrogram?
            It is a very useful representation of the spectrum for 
            visualizing the spectral peaks of a sound.
        """

        pci = PraatCommands(self.sound)
        cepstrogram = pci.to_power_cepstrogram(
            self.settings.PowerCepstrogram.pitch_floor, 
            self.settings.PowerCepstrogram.time_step, 
            self.settings.PowerCepstrogram.max_frequency, 
            self.settings.PowerCepstrogram.pre_emphasis
            ).result
        cepstrogram = self._extract(cepstrogram, 'data')
        x, y = cepstrogram.values.shape
        col_count = y
        col_names = [f'Band_{i}' for i in range(col_count)]
        feat = Feature(cepstrogram, col_names, 'Power Cepstrogram')
        self.settings.PowerCepstrogram._saved_feature = feat
        return feat 

    @property
    def cochleagram(self):
        """
        What is a cochleagram?
            The cochleagram is a 2D representation of the sound in terms of 
            frequency and time. It is produced by applying a series of bandpass 
            filters to the sound, and then summing the output of each filter. 
            The result is a 2D matrix of values in which the rows represent 
            the frequency of the bandpass filters, and the columns represent 
            time. The values in the matrix represent the energy of the sound 
            at each frequency and time. 
        
        Why a Cochleagram instead of Spectrogram?
            The cochleagram is a useful representation 
            of the sound because it is similar to the way that the human ear 
            processes sound.
        """
        coch = self.pci.to_cochleagram(
            self.settings.Cochleagram.time_step, 
            self.settings.Cochleagram.bark_frequency_resolution, 
            self.settings.Cochleagram.window_length, 
            self.settings.Cochleagram.forward_mask_time
            ).result
        coch = self._extract(coch, 'data')
        x, y = coch.values.shape
        col_count = y
        col_names = [f'Band_{i}' for i in range(col_count)]
        feat = Feature(coch, col_names, 'Cochleagram')
        self.settings.Cochleagram._saved_feature = feat
        return feat
    
    @property
    def silence_detection_settings(self):
        return self.settings.Silence
    
    @property
    def voice_detection_settings(self):
        return self.settings.Voice_Detection

    @property
    def silence(self):
        pci = PraatCommands(self.sound)
        tg = pci.annotate_silence(self.settings.Silence).result
        pci = PraatCommands(tg)
        tb = pci.down_to_table().result
        pci = PraatCommands(tb)
        mx = pci.down_to_matrix().result
        col_names = ['index', 'start', 'tier', 'label', 'end']
        feat = Feature(mx, col_names, 'Silence')
        drop = ['index', 'tier']
        replace = {1.0: 'Silence', 2.0: 'Speech'}
        feat._drop = drop
        feat._replace = replace
        return feat

    @property
    def voicing(self):
        pci = PraatCommands(self.sound)
        tg = pci.annotate_voiced(self.settings.Voice_Detection).result
        pci = PraatCommands(tg)
        tb = pci.down_to_table().result
        pci = PraatCommands(tb)
        mx = pci.down_to_matrix().result
        col_names = ['index', 'start', 'tier', 'label', 'end']
        feat = Feature(mx, col_names, 'Voicing')
        drop = ['index', 'tier']
        replace = {'label': {1.0: 'Silence', 2.0: 'Speech'}}
        feat._drop = drop
        feat._replace = replace
        return feat
    
    @property
    def voiced_pitch_frames_count(self):
        pitch = self.pitch()._matrix
        pci = PraatCommands(pitch)
        count = pci.count_voiced_frames().result
        return count
    
    @property
    def time_of_minimum_pitch(self, interpolation: Interpolation = None, unit: Unit = None):
        if interpolation is None: interpolation = self.interpolation_settings
        pitch = self.pitch()._matrix
        pci = PraatCommands(pitch)
        time = pci.time_of_minimum(interpolation, unit).result
        return time

    @property
    def time_of_maximum_pitch(self, interpolation: Interpolation = None, unit: Unit = None):
        if interpolation is None: interpolation = self.interpolation_settings
        pitch = self.pitch()._matrix
        pci = PraatCommands(pitch)
        time = pci.time_of_maximum(interpolation, unit).result
        return time
    
    def comparison(
            self, 
            first: Union[Feature, pd.Series, pd.DataFrame], 
            second: Union[Feature, pd.Series, pd.DataFrame], 
            series_name=None
            ):
        is_Feature = isinstance(first, Feature) and isinstance(second, Feature)
        is_Dataframe = isinstance(first, pd.DataFrame) and isinstance(second, pd.DataFrame)
        if is_Feature: 
            first = first.dataframe
            second = second.dataframe
        if is_Dataframe:
            first, second = first.align(second)
            first = first[series_name]
            second = second[series_name]
        return ComparisonGrid(first, second)

class VoiceReport:
    def __init__(
            self, 
            sound: pm.Sound,
            time_range_start=0.0, 
            time_range_end=0.0,
            pitch_floor=75.0,
            pitch_ceiling=600.0,
            max_period_factor=1.3,
            max_amp_factor=1.6,
            silence_threshold=0.03,
            voicing_threshold=0.45
            ):
        self.sound = sound
        self.pci = PraatCommands(self.sound)
        self.raw_report = {}
        self.report: VoiceReportConfig = None
        self.create_report(
            time_range_start=time_range_start, time_range_end=time_range_end, pitch_floor=pitch_floor, pitch_ceiling=pitch_ceiling, max_period_factor=max_period_factor, max_amp_factor=max_amp_factor, silence_threshold=silence_threshold, voicing_threshold=voicing_threshold)

    def create_report(self, **kwargs):
        voice_report = self.pci.voice_report(**kwargs).result
        self._get_items(voice_report)
        pitch = self.raw_report['Pitch']
        pitch_report = self._compile_to_report(pitch, PitchReportConfig)
        pulses = self.raw_report['Pulses']
        pulses_report = self._compile_to_report(pulses, PulseReportConfig)
        voicing = self.raw_report['Voicing']
        voicing_report = self._compile_to_report(voicing, VoicingReportConfig)
        jitter = self.raw_report['Jitter']
        jitter_report = self._compile_to_report(jitter, JitterReportConfig)
        shimmer = self.raw_report['Shimmer']
        shimmer_report = self._compile_to_report(shimmer, ShimmerReportConfig)
        harmonicity = self.raw_report['Harmonicity of the voiced parts only']
        harmonicity_report = self._compile_to_report(harmonicity, HarmonicityReportConfig)
        self.report = VoiceReportConfig(
            Pitch=pitch_report, 
            Pulses=pulses_report, 
            Voicing=voicing_report, 
            Jitter=jitter_report, 
            Shimmer=shimmer_report, 
            Harmonicity=harmonicity_report
            )
    
    def _get_items(self, report):
        report = report.splitlines()
        current_item = None
        for i in report:
            if not '  ' in i and ':' in i:
                item = i.strip(':')
                self.raw_report[item] = {}
                current_item = item
            elif '  ' in i and ':' in i:
                self._get_sub_items(current_item, i)

    def _get_sub_items(self, key, item):
        if '  ' in item and ':' in item:
            if not key in self.raw_report: return
            l = str(item).strip('  ')
            k, v = l.split(':')
            s = self.raw_report[key]
            s[k] = v

    def _compile_to_report(self, raw_item: dict, config_type: type[ReportConfig]):
        values = [v.strip() for v in raw_item.values()]
        params = [k for k in config_type.__fields__.keys()]
        return config_type(**dict(zip(params, values)))
    

class XpressionGrid(Grid):
    """
    The Xpression Grid will consist of the following features:
    1. Voice Report: A basic report class that returns some valuable overall perspective information.
    2. Pulses: Timeing info for segmenting clips, and adjusting phrase timings.
    3. Pitch
    4. Time
    5. DFT/Cochleagram Envelope: To protect any frequencies essential to tonality, from being affected by the pitch shifting.
    6. Intensity
    7. Amplitude
    8. Glottal Pulses
    9. Silence Periods
    10. Voicing Periods
    """
    def __init__(self, sound: pm.Sound):
        self.sound = sound
        self.pci = PraatCommands(self.sound)

    @property
    def voice_report(self):
        return VoiceReport(self.sound)

    @property    
    def pulses(self, min_pitch=75.0, max_pitch=600.0):
        matrix = self.pci.to_pointprocess_periodic_cc(arguments=[min_pitch, max_pitch]).result
        cols = ['Pulse Timing']
        return self._to_feature(matrix, cols, 'Pulses', 'data')
    

    
