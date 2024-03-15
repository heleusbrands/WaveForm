from xtract import *
from waveform import *
from IPython.display import Audio, display, clear_output, HTML
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from typing import TypeVar
from collections import deque
from audio_modules.xtract.XT.xtract_configs import *
from pydantic import ValidationError
#import IPython.display
import array
from IPython.display import clear_output
from copy import deepcopy
import time
import pandas as pd
import itertools
import os


class LockPick:
    def __init__(self, waveform: WaveForm, base_settings, reference: WaveForm, algorithm = 'hpps'):
        self._last_error = None
        self._last_changed = None
        self._last_settings = None
        self._errors = 0
        self._runs = 0

        self._int_multiplier = 2
        self._int_zero_increment = 10
        self._int_increment_keys = ['pad']
        self._int_multiplier_keys = ['len', 'size']
        self._str_options = {'type': ['hann', 'sin'], 'mode': ['binary', 'relative']}

        self.waveform = waveform
        self.reference = reference
        self.base_settings = base_settings
        if algorithm == 'hpps': self.settings = self.base_settings._FluxHppsSettings()
        self.results = deque()
        self.effect = 'flux'
        self.filters = []
        self.keys = list(self.settings.dict().keys())
        self.defaults = list(self.settings.dict().values())
        self.default_overrides = {}

    def filter(self, settings_combos):
        settings = {self.keys[i]: i for i in range(len(self.keys))}
        for f in self.filters:
            if f in settings:
                if self.default_overrides and f in self.default_overrides.keys():
                    settings_combos[settings[f]] = deque([self.default_overrides[f]])
                else: settings_combos[settings[f]] = deque([self.defaults[settings[f]]])
        return settings_combos
    
    def settings_options(self):
        settings_combos = []

        for k, v in self.settings.dict().items():

            if type(v) == bool: settings_combos.append([True, False])

            elif type(v) == int:

                for m in self._int_multiplier_keys:
                    if m in k:
                        settings_combos.append([
                            v, 
                            v * self._int_multiplier, 
                            v * self._int_multiplier * self._int_multiplier
                            ])
                        break

                for i in self._int_increment_keys:
                    if i in k:
                        settings_combos.append([
                            v, 
                            v + self._int_zero_increment, 
                            v + self._int_zero_increment * self._int_multiplier
                            ])
                        break

            if type(v) == str:
                for o in self._str_options:
                    if o in k: 
                        settings_combos.append(self._str_options[o])
                        break

        return settings_combos
    
    def clear_run_history(self):
        self.results = deque()

    @property
    def xplore(self):
        return Xplore(self.results)
    
    def manual_run(self, settings_combos: list):
        #settings_combos = itertools.product(*settings_combos)
        self.waveform.reformers.flux.use_hpps
        for settings in settings_combos:
            waveform = deepcopy(self.waveform)
            current_settings = dict(zip(self.keys, settings))
            print(current_settings)
            if self._last_settings is None: self._last_settings = current_settings
            else:
                for i in range(len(self._last_settings)):
                    if current_settings[self.keys[i]] == self._last_settings[self.keys[i]]:
                        continue
                    self._last_changed = (self.keys[i], current_settings[self.keys[i]])
                    break

            self._runs += 1

            try:
                setting = waveform.reformers.flux.settings
                setting.HppsSettings = setting.HppsSettings.__class__(**current_settings)
            except ValidationError as e:
                self._last_error = e
                self._errors += 1
                continue

            try:
                current_run = waveform.reformers.flux.warp_to_match(self.reference)
                self.results.append((current_run, setting.HppsSettings))
            except ValueError as e:
                self._last_error = e
                self._errors += 1
                continue

            self._last_settings = current_settings

            clear = 'cls'
            os.system(clear)
            print(f'Runs: {self._runs}')
            print(f'Errors: {self._errors}')
            print(f'Last Error: {self._last_error}')
            print(f'Successful Runs: {len(self.results)}')
            print(f'Last Changed: {self._last_changed}')
        return self.results
    
    def start(self, batch_size=1):
        
        settings_combos = self.settings_options()
        if self.filters: settings_combos = self.filter(settings_combos)
        settings_combos = itertools.product(*settings_combos)
        self.waveform.reformers.flux.use_hpps

        for settings in settings_combos:
            waveform = deepcopy(self.waveform)
            current_settings = dict(zip(self.keys, settings))
            if self._last_settings is None: self._last_settings = current_settings
            else:
                for i in range(len(self._last_settings)):
                    if current_settings[self.keys[i]] == self._last_settings[self.keys[i]]:
                        continue
                    self._last_changed = (self.keys[i], current_settings[self.keys[i]])
                    break

            self._runs += 1

            try:
                setting = waveform.reformers.flux.settings
                setting.HppsSettings = setting.HppsSettings.__class__(**current_settings)
            except ValidationError as e:
                self._last_error = e
                self._errors += 1
                continue

            try:
                current_run = waveform.reformers.flux.warp_to_match(self.reference)
                self.results.append((current_run, setting.HppsSettings))
            except ValueError as e:
                self._last_error = e
                self._errors += 1
                continue

            self._last_settings = current_settings

            clear = 'cls'
            os.system(clear)
            print(f'Runs: {self._runs}')
            print(f'Errors: {self._errors}')
            print(f'Last Error: {self._last_error}')
            print(f'Successful Runs: {len(self.results)}')
            print(f'Last Changed: {self._last_changed}')

            if len(self.results) == batch_size: yield self.results

class Xplore:
    def __init__(self, audio_items: list):
        self.data = audio_items
        self.current = 0
        self.current_audio = None
        self.current_settings = None
        self.set_step = 18
        self.step = 1
        self.saved_settings = None
        self.top_settings = []
        self.setting_to_remove = None
        self.settings_type = FormFluxSettings()._FluxHppsSettings()
        self.scoring = self.create_scoring_dataframe()

    def compile_settings_dataframe(self):
        settings = [s.dict() for a, s in self.data]
        return pd.DataFrame(settings)

    def create_scoring_dataframe(self, data=None):
        catagories = list(self.settings_type.dict().keys())
        catagories = catagories.append('score')
        if data: df = pd.DataFrame(data, columns=catagories, index=range(len(data)))
        else: df = pd.DataFrame(columns=catagories)
        self.scoring = df
        return df
    
    def score(self):
        for c in self.scoring.columns:
            pass
            

    def items(self):
        for a, s in self.data:
            self.current_audio = a
            self.current_settings = s
            self.current += 1
            nparray = a._array.T
            sr = a.settings.rate
            yield Audio(nparray, rate=sr)

    def get(self):
        a, s = self.data[self.current]
        self.current += self.step
        audio = Audio(a._array.T, rate=a.settings.rate)
        self.current_audio = a
        self.current_settings = s
        return audio, s
    
    def get_next_set(self):
        self.current += self.set_step
        a, s = self.data[self.current]
        audio = Audio(a._array.T, rate=a.settings.rate)
        self.current_audio = a
        self.current_settings = s
        return audio, s
    
    def autoplay(self):
        a, s = self.data[self.current]
        self.current_audio = a
        self.current_settings = s
        self.current += 1
        nparray = a._array.T
        sr = a.settings.rate
        return Audio(nparray, rate=sr, autoplay=True), s
    
    def good(self, by_set=False):
        if self.current > 0: self.add_to_saved_settings()
        scoring = self.current_settings.dict()
        scoring['score'] = 1
        if self.scoring.empty: self.create_scoring_dataframe(scoring)
        else: self.scoring.loc[len(self.scoring)] = scoring
        return self.get_next_set() if by_set else self.get()
    
    def bad(self, by_set=False):
        if self.current > 0: self.to_remove()
        scoring = self.current_settings.dict()
        scoring['score'] = 0
        if self.scoring.empty: self.create_scoring_dataframe(scoring)
        else: self.scoring.loc[len(self.scoring)] = scoring
        return self.get_next_set() if by_set else self.get()
        

    def to_remove(self):
        s = self.current_settings.dict()
        s['index'] = self.current
        if self.setting_to_remove is None:
            self.setting_to_remove = pd.DataFrame(s, index=[0])
        else:
            settings = pd.DataFrame(s, index=[0])
            self.setting_to_remove = pd.concat([self.setting_to_remove, settings], ignore_index=True)

    def add_to_saved_settings(self):
        s = self.current_settings.dict()
        s['index'] = self.current
        if self.saved_settings is None:
            self.saved_settings = pd.DataFrame(s, index=[0])
        else:
            settings = pd.DataFrame(s, index=[0])
            self.saved_settings = pd.concat([self.saved_settings, settings], ignore_index=True)

    def xplore_saved_settings(self, df: pd.DataFrame):
        data = self.data
        previous_settings = None
        for i in range(len(df)):
            settings = df.iloc[i]
            idx = settings['index']
            wf, s = data[idx]
            audio_array = wf._array.T
            rate = wf.settings.rate
            audio = Audio(audio_array, rate=rate)
            if previous_settings is not None:
                sdiff = previous_settings.compare(settings, result_names=('previous', 'current'))
            else:
                sdiff = settings
            previous_settings = settings
            yield display(audio, sdiff)

    def add_to_top_settings(self, idx):
        s = self.saved_settings.loc[self.saved_settings['index'] == idx]
        self.top_settings.append(s)