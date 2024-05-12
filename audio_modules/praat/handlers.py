from __future__ import annotations
from parselmouth import Matrix
from parselmouth.praat import call
from pydantic.v1 import dataclasses
import numpy as np
from .configs import *
from ..air import WaveArray as wa
from ..air import AirMatrix


"""
class Handler:
    def __init__(self):
        self.result = None

    def __check__(self, result):
        pass

    def __call__(self, result):
        pass

    def __set_data_attributes__(self, samples: np.ndarray, data):
        data.length = len(samples)
        data.shape = samples.shape
        return data
    
    @classmethod
    def register_handler(cls):
        global Handlers
        #Handlers.__setattr__(cls.__name__, cls())
        setattr(Handlers, cls.__name__, cls())
        #Handlers = Handlers
        print(f'Registered handler {cls.__name__}.')
        print(f'Handlers: {Handlers.dict()}')
"""
class MatrixArrayHandler:
    def __init__(self):
        self.result = None
    
    def __check__(self, result):
        return True if type(result) == Matrix or hasattr(result, 'values') else False

    def __call__(self, result):
        self.result = result
        time = wa.time_array(result.xs())
        rows = wa.audio_data_array(result.ys())
        values = wa.audio_data_array(result.values)
        return AirMatrix(**{'x': time, 'y': rows, 'z': values})

 
class Handler:
    handles = {}
    
    def __new__(cls, new_handle = None):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Handler, cls).__new__(cls)
        if new_handle:
            cls.handles.update({new_handle.__name__: new_handle()})
        return cls.instance
    
    @classmethod
    def dict(cls):
        return cls.handles


    
Handlers = Handler()
Handler(MatrixArrayHandler)
