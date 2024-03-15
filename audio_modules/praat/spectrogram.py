from .core import *
from .configs import *


class Spectrogram(PraatBase):
    def __init__(
        self,
        audio,
        rate: PositiveFloat = None
        ):
        super().__init__(audio, rate)
        self._spec = None
        self.data = None
        self.window_info = None
        self.settings = WindowConfig()

    def __call__(self):
        win_shape = self.settings._pmtypes.get(self.settings.window_shape._value_, None)
        spec = self.sound.to_spectrogram(
            window_length=self.settings.window_length,
            time_step=self.settings.time_step,
            maximum_frequency=self.settings.max_frequency,
            frequency_step=self.settings.frequency_step,
            window_shape=win_shape
            )
        self._spec = spec
        frequencies = np.array(spec.ys())
        frame_times = np.array(spec.xs())
        power = spec.values.T
        self.data = SpectrogramBaseData(power=power, frequency=frequencies, time=frame_times)
        return self.data
    
    @property
    def window_data(self):
        if self._spec is None:
            self.__call__()
        window_data = BasicWindowData(_spec = self._spec)
        return window_data
    
    @property
    def dataframe(self):
        if self.data is None:
            self.__call__()
        frequencies = self.data.frequency
        frame_times = self.data.time
        power = self.data.power
        pairs = [pd.Series(list(zip(np.round(frequencies, 5), np.round(x, 5)))) for x in power]
        pairs = pd.DataFrame({
            'Frequency Hz': frequencies.round(-1),
            **dict(zip((pd.Series(frame_times, name='Time_MS')*1000).round(), pairs))
            })
        return pairs
