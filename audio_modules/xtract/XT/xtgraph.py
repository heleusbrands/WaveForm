import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from .xtract_configs import *

class GraphX:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.settings = None
        self.layout = None
        self.trace = None
        self.graph = None


    def update_settings(self, settings):
        if 'z' in settings.kwargs:
            settings.kwargs['z'] = self.data
        if 'x' in settings.kwargs:
            settings.kwargs['x'] = self.data.index
        if 'y' in settings.kwargs:
            settings.kwargs['y'] = self.data.columns
        if 'data' in settings.kwargs:
            settings.kwargs['data'] = self.data
        return settings
    
    def _create_graph(self, settings):
        self.layout = self.settings.layout
        self.trace = self.settings.graph(**self.settings.kwargs)
        self.graph = go.Figure(layout=self.layout)
        self.graph.add_trace(self.trace)
        return self.graph
    
    def heatmap(self):
        if self.settings is None:
            self.settings = self.update_settings(HeatmapSettings(data=self.data))
        return self._create_graph(self.settings)


    def surface(self):
        if self.settings is None:
            self.settings = self.update_settings(SurfaceSettings(data=self.data))
        return self._create_graph(self.settings)

    def scatter(self):
        if self.settings is None:
            self.settings = self.update_settings(ScatterSettings(data=self.data))
        return self._create_graph(self.settings)
    
    def heatmap_settings(self):
        self.settings = self.update_settings(HeatmapSettings(data=self.data))
        return self.settings
    
    def surface_settings(self):
        self.settings = self.update_settings(SurfaceSettings(data=self.data))
        return self.settings
    
    def scatter_settings(self):
        self.settings = self.update_settings(ScatterSettings(data=self.data))
        return self.settings


