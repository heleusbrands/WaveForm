from .core import *
#from .configs import *
from .processor import PraatProcessor


class BaseFilters(PraatBase):
    def __init__(
        self,
        audio,
        rate: PositiveFloat = None
        ):
        super().__init__(audio, rate)
        self._target = self.sound
        self._filtered = None
        self.data = None

    @PraatProcessor
    def hann_stopband(self, start_freq: float = 500, stop_freq: float=1000, smoothing: float=100.0):
        return 'Filter (stop Hann band)...'
    
    @PraatProcessor
    def hann_bandpass(self, start_freq: float = 500, stop_freq: float=1000, smoothing: float=100.0):
        return 'Filter (pass Hann band)...'
    
    @PraatProcessor
    def single_formant(freq: float = 1000.0, bandwidth: float = 100.0):
        return 'Filter (one formant)...'
    
    @PraatProcessor
    def pre_emphasis(self, start_freq: float = 50.0):
        return 'Filter (pre-emphasis)...'
    
    @PraatProcessor
    def de_emphasis(self, start_freq: float = 50.0):
        return 'Filter (de-emphasis)...'
    
    @PraatProcessor
    def gammatone(self, centre_freq: float = 1000.0, bandwidth: float = 150.0):
        return 'Filter (gammatone)...'