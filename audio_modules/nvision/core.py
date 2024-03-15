from pydantic import BaseModel, Field
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from functools import reduce
from .configs import *
from typing import Union
from enum import Enum
from collections import deque
from typing import TypeVar

class SecondaryDimensionSize(Enum):
    OneLevels = 1
    TwoLevels = 2
    ThreeLevels = 3
    NLevels = 4

class GraphType(Enum):
    HEATMAP = HeatmapSettings
    SURFACE = SurfaceSettings
    SCATTER = ScatterSettings

WaveGX = TypeVar('WaveGX', bound='WaveGraphX')

class WaveGraphX:
    def __init__(self, data: Union[pd.DataFrame, pd.Series, tuple], name = None):
        self._Qdata = deque()
        self._D2 = SecondaryDimensionSize
        self._dim2size = SecondaryDimensionSize.OneLevels
        self._graph_settings = None
        self._data = data
        self._signed = False
        self._trace_num = 0

        self.name = name
        self.dimensional_data = Coordinates()
        self.GraphType = GraphType.SCATTER
        self.dtype = type(data)
        self.layout = None
        self.trace = None
        self.graph = None

    def __call__(self):
        self.__create__()
        if self._trace_num == 0: 
            self.graph.add_trace(self.trace)
            self._trace_num += 1
        return self.graph
    
    def __create__(self):
        if not self._signed: self._determine_data_structure()
        if 'x' in self.settings.kwargs: self.settings.kwargs['x'] = self._Qdata[0]
        if 'y' in self.settings.kwargs: self.settings.kwargs['y'] = self._Qdata[1]
        if 'z' in self.settings.kwargs: self.settings.kwargs['z'] = self._Qdata[2]
        self.layout = self.settings.layout
        self.trace = self.settings.graph(**self.settings.kwargs)
        self.trace.name = self.name
        if self.graph is None: self.graph = go.Figure(layout=self.layout)

    def __add__(self, other: WaveGX):
        self.__create__()
        if self.gtype == self.gtype.SCATTER:
            other.settings.gset.line.color = list(GraphOptions().basic_colors.dict().values())[self._trace_num]
            other.settings.kwargs['line'] = other.settings.gset.line.dict()
        other.__create__()
        trace = other.trace
        self.graph.add_trace(trace)
        self._trace_num += 1
        return self

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data
        if self.name is None: self.name = self._data.Name
        self.dtype = type(data)
        self._signed = False
        self._trace_num = 0
        self._Qdata.clear()

    @property
    def settings(self):
        if self._graph_settings is None: self._graph_settings = self.GraphType.value()
        elif not isinstance(self._graph_settings, self.GraphType.value):
            self._graph_settings = self.GraphType.value()
        return self._graph_settings
    
    @property
    def rotate(self):
        self._Qdata.rotate(1)
        self.graph = None
        self._trace_num = 0
        return self
    
    @property
    def gtype(self):
        return self.GraphType

    @property
    def dlength(self):
        if self.dtype is pd.DataFrame:
            return len(self.data.columns)
        elif self.dtype is pd.Series:
            return 1
        elif self.dtype is tuple:
            return len(self.data)
        else:
            raise TypeError("Data type not supported")
    
    def _determine_data_structure(self):

        if self.dlength == 1:
            self._dim2size = SecondaryDimensionSize.OneLevels
        elif self.dlength == 2:
            self._dim2size = SecondaryDimensionSize.TwoLevels
        elif self.dlength == 3:
            self._dim2size = SecondaryDimensionSize.ThreeLevels
        else:
            self._dim2size = SecondaryDimensionSize.NLevels

        if self.dtype is pd.DataFrame:
            self._init_dataframe()
        elif self.dtype is pd.Series:
            self._init_series()
        elif self.dtype is tuple:
            self._init_tuple()
        else:
            raise TypeError("Data type not supported")

        self.graph = None
        for v in self.dimensional_data.dict().values(): self._Qdata.append(v)
        self._signed = True

    def _init_dataframe(self):
        if self.name is None: self.name = self.data.Name

        if self._dim2size is self._D2.OneLevels:
            self.dimensional_data.x = self.data.index
            self.dimensional_data.y = self.data.values

        elif self._dim2size is self._D2.TwoLevels:
            self.dimensional_data.x = self.data[self.data.columns[0]]
            self.dimensional_data.y = self.data[self.data.columns[1]]

        elif self._dim2size is self._D2.ThreeLevels:
            self.dimensional_data.x = self.data[self.data.columns[0]]
            self.dimensional_data.y = self.data[self.data.columns[1]]
            self.dimensional_data.z = self.data[self.data.columns[2]]

        elif self._dim2size is self._D2.NLevels:
            self.dimensional_data.x = self.data.index
            self.dimensional_data.y = self.data.columns
            self.dimensional_data.z = self.data

    def _init_series(self):
        self.dimensional_data.x = self.data.index
        self.dimensional_data.y = self.data.values

    def _init_tuple(self):
        if self._dim2size is self._D2.OneLevels:
            self.dimensional_data.x = list(range(len(self.data[0])))
            self.dimensional_data.y = self.data[0]

        elif self._dim2size is self._D2.TwoLevels:
            self.dimensional_data.x = self.data[0]
            self.dimensional_data.y = self.data[1]

        elif self._dim2size is self._D2.ThreeLevels:
            self.dimensional_data.x = self.data[0]
            self.dimensional_data.y = self.data[1]
            self.dimensional_data.z = self.data[2]
