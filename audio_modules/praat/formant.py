import numpy as np
import pandas as pd
from parselmouth import Sound, Data
from parselmouth.praat import call
from typing import Optional, Union
from .configs import Formant, FormantGrid, FormantStats
from pydantic.v1 import PositiveFloat
from .core import PraatBase
from .processor import PraatProcessor
from typing import TypeVar
from .handlers import Handler, Handlers

FormantPathHandle = TypeVar("FormantPathHandle", bound="FormantPathHandler")

class FormantBurg(PraatBase):
    """
    Initialize the Formant object.

    Parameters
    ----------
    audio : Union[Sound, str, np.ndarray]
        The audio input as a Sound object, file path, or numpy array.
    rate : PositiveFloat, optional
        The sample rate of the audio.
    time_step : Optional[PositiveFloat], optional
        The time step for formant analysis.
    max_number_of_formants : PositiveFloat, optional
        The maximum number of formants to analyze. Default is 5.0.
    maximum_formant : float, optional
        The maximum formant frequency to analyze. Default is 5500.0.
    window_length : PositiveFloat, optional
        The length of the analysis window in seconds. Default is 0.025.
    pre_emphasis_from : PositiveFloat, optional
        The pre-emphasis frequency. Default is 50.0.

    Returns
    -------
    None

    Raises
    ------
    None
    """

    def __init__(
        self, 
        audio: Union[Sound, str, np.ndarray],
        rate: PositiveFloat = None,
        time_step: Optional[PositiveFloat] = None, 
        max_number_of_formants: PositiveFloat = 5.0, 
        maximum_formant: float = 5500.0, 
        window_length: PositiveFloat = 0.025, 
        pre_emphasis_from: PositiveFloat = 50.0
        ):
        super().__init__(audio, rate)
        self.sound = audio
        self.time_step = time_step
        self.window_length = window_length
        self.max_number_of_formants = max_number_of_formants
        self.maximum_formant = maximum_formant
        self.pre_emphasis_from = pre_emphasis_from
        self._call = self.sound.to_formant_burg(
            time_step=self.time_step,
            window_length=self.window_length,
            max_number_of_formants=self.max_number_of_formants,
            maximum_formant=self.maximum_formant,
            pre_emphasis_from=self.pre_emphasis_from
            )
        self.total_formants_max = call(self._call, "Get maximum number of formants")
        self.total_formants_min = call(self._call, "Get minimum number of formants")
        self.formants = self._get_formant_stack()

    def _get_formant_stack(self):
        grid = FormantGrid()
        formant_arrays = []
        for i in range(self.total_formants_max):
            formant_arrays.append(np.array(call(self._call, "To Matrix", i+1).values))
            formant = Formant(formant_id=i+1, data=formant_arrays[i])
            formant.stats = FormantStats(
                min=np.min(formant_arrays[i]),
                max=np.max(formant_arrays[i]),
                mean=np.mean(formant_arrays[i]),
                min_max_range=np.max(formant_arrays[i]) - np.min(formant_arrays[i])
                )
            grid.__setattr__(f'F{i+1}', formant)
        stack = np.vstack(formant_arrays)
        grid.stack = stack
        return grid
    
    @property
    def dataframe(self):
        return pd.DataFrame(self.formants.stack.T, columns=self.formants.as_dict().keys())
                
class Formants(PraatBase):
    """
    Formants class.

    Parameters
    ----------
    audio : Union[Sound, str, np.ndarray]
        The audio input as a Sound object, file path, or numpy array.
    rate : PositiveFloat, optional
        The sample rate of the audio.

    Methods
    -------
    formants_burgepath(time_step=None, max_number_of_formants=5.0, middle_formant_ceiling=5500.0, window_length=0.025, pre_emphasis_from=50.0, ceiling_step_size=0.05, number_steps_updown=4)
        Perform formant analysis using the burg algorithm and return the result as a FormantPath object.

    formants_burge(time_step=None, max_number_of_formants=5.0, maximum_formant=5500.0, window_length=0.025, pre_emphasis_from=50.0)
        Perform formant analysis using the burg algorithm and return the result as a FormantBurg object.

    formants_keepall()
        Placeholder method.

    formants_sl()
        Placeholder method.

    formants_robust()
        Placeholder method.

    formant_path()
        Placeholder method.
    """

    def __init__(
        self, 
        audio: Union[Sound, str, np.ndarray],
        rate: PositiveFloat = None,
        ):
        super().__init__(audio, rate)
    
    @PraatProcessor
    def formants_burgepath(
            self, 
            time_step: Optional[PositiveFloat] = 0.005,
            max_number_of_formants: PositiveFloat = 5.0,
            middle_formant_ceiling: PositiveFloat = 5500.0,
            window_length: PositiveFloat = 0.025,
            pre_emphasis_from: PositiveFloat = 50.0,
            ceiling_step_size: PositiveFloat = 0.05,
            number_steps_updown: int = 4
            ):
        return 'To FormantPath (burg)...'
    
    def formants_burge(
            self, 
            time_step: Optional[PositiveFloat] = None, 
            max_number_of_formants: PositiveFloat = 5.0, 
            maximum_formant: float = 5500.0, 
            window_length: PositiveFloat = 0.025, 
            pre_emphasis_from: PositiveFloat = 50.0):
        return FormantBurg(self.sound, self.rate, time_step, max_number_of_formants, maximum_formant, window_length, pre_emphasis_from)

    def formants_keepall(
            self
            ):
        pass

    def formants_sl(self):
        pass

    def formants_robust(self):
        pass

    def formant_path(self):
        return 


class FormantPath:
    """
    FormantPath class.

    Parameters
    ----------
    formant_path : object
        The formant path object.

    Methods
    -------
    number_of_candidates()
        Get the number of candidates.

    ceiling_frequencies()
        List the ceiling frequencies.

    stress_of_candidate(time_start=0.0, time_end=0.0, candidate_number=5, coefficients_by_track='3 3 3', power=1.25)
        Get the stress of a specific candidate.

    stress_of_candidates(time_start=0.0, time_end=0.0, coefficients_by_track='3 3 3', power=1.25)
        List the stress of all candidates.

    optimal_ceiling(time_start=0.0, time_end=0.0, coefficients_by_track='3 3 3', power=1.25)
        Get the optimal ceiling.

    stress_array(window_length=0.025, coefficient_by_track='3 3 3', power=1.25)
        Convert the formant path to a stress matrix.

    qsums_array(number_of_tracks=4)
        Convert the formant path to a qsums matrix.

    transitions_array(number_of_tracks=4)
        Convert the formant path to a transitions matrix.

    deltas_array(fb_weight=1.0, frequency_change_weight=1.0, stress_weight=1.0, ceiling_change_weight=1.0, intensity_modulation_stepsize=5.0, global_stress_window_length=0.035, coefficient_by_track='3 3 3', power=1.25)
        Convert the formant path to a deltas matrix.
    """

    def __init__(self, formant_path):
        self._path = formant_path
        self._target = formant_path

    @PraatProcessor
    def number_of_candidates(self):
        return 'Get number of candidates'
    
    @PraatProcessor
    def ceiling_frequencies(self):
        return 'List ceiling frequencies'
    
    @PraatProcessor
    def stress_of_candidate(
        self, time_start: float=0.0, 
        time_end: float=0.0, 
        candidate_number: int=5, 
        coefficients_by_track: str = '3 3 3',
        power: float = 1.25
        ):
        return 'Get stress of candidate...'
    
    @PraatProcessor
    def stress_of_candidates(
        self,
        time_start: float=0.0,
        time_end: float=0.0,
        coefficients_by_track: str = '3 3 3',
        power: float = 1.25
        ):
        return 'List stress of candidates...'
    
    @PraatProcessor
    def optimal_ceiling(
        self,
        time_start: float=0.0,
        time_end: float=0.0,
        coefficients_by_track: str = '3 3 3',
        power: float = 1.25
        ):
        return 'Get optimal ceiling...'
    
    @PraatProcessor
    def stress_array(
        self,
        window_length: float = 0.025,
        coefficient_by_track: str = '3 3 3',
        power: float = 1.25
        ):
        return 'To Matrix (stress)...'
    
    @PraatProcessor
    def qsums_array(
        self,
        number_of_tracks: int = 4,
        ):
        return 'To Matrix (qsums)...'
    
    @PraatProcessor
    def transitions_array(
        self,
        number_of_tracks: int = 4,
        ):
        return 'To Matrix (transitions)...'
    
    @PraatProcessor
    def deltas_array(
        self,
        fb_weight: float = 1.0,
        frequency_change_weight: float = 1.0,
        stress_weight: float = 1.0,
        ceiling_change_weight: float = 1.0,
        intensity_modulation_stepsize: float = 5.0,
        global_stress_window_length: float = 0.035,
        coefficient_by_track: str = '3 3 3',
        power: float = 1.25
        ):
        return 'To Matrix (deltas)...'
    
class FormantPathHandler:
    def __init__(self):
        self.result = None
    
    def __check__(self, result):
        if not type(result) == Data and not hasattr(result, 'class_name'): return False
        return True if result.class_name == 'FormantPath' else False
        

    def __call__(self, result):
        self.result = result
        return FormantPath(result)
    
Handler(FormantPathHandler)