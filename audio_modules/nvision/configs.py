from pydantic.v1 import BaseModel, Field
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


class G3Data(BaseModel):
    
    class Config:
        orm_mode = True
        extra = 'allow'
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
    
    x: pd.Series
    y: pd.Series
    z: pd.Series
    name: str = Field(default=None, exclude=True)
    color: str = Field(default=None, exclude=True)

class G2Data(BaseModel):
        
        class Config:
            orm_mode = True
            extra = 'allow'
            arbitrary_types_allowed = True
            allow_population_by_field_name = True
        
        x: pd.Series
        y: pd.Series
        name: str = Field(default=None, exclude=True)
        color: str = Field(default=None, exclude=True)


class GxData:
    def __init__(self):
        self._data = []

    def Data(self, name, value):
        self.__setattr__(name, value)
        self._data.append(value)
        return self

    def __add__(self, value):
        if type(value) is not str:
            self._data.append(value)
            return self
        else:
            self.__setattr__(value, GxData())
            return self.__getattribute__(value)

class GraphOptions(Settings):

    class Type(Settings):
        Heatmap = go.Heatmap
        Scatter = go.Scatter
        Scatter3D = go.Scatter3d
        Mesh3D = go.Mesh3d
        Marker = go.Marker
        Violin = go.Violin
        Surface = go.Surface
        
    class GraphGradient(Settings):
        agsunset: str = "agsunset"
        plasma: str = "plasma"
        magma: str = "magma"
        inferno: str = "inferno"
        viridis: str = "viridis"
        cividis: str = "cividis"
        thermal: str = "thermal"

    class LayoutColors(Settings):
        gridcolor: str = "#515467"
        color: str = "#8D91AA"
        paper_bgcolor: str = 'rgba(0,0,0,0)'
        plot_bgcolor: str = 'rgba(0,0,0,0)'

    class BasicColors(Settings):
        crimsonrose: str = '#F41C5E'
        blueviolet: str = '#A029F3'
        dodgerblue: str = '#297AF3'
        turquoise: str = '#29ECF3'
        aquamarine: str = '#52EFA0'
        khaki: str = '#EFDE52'
        coral: str = '#EF8D52'
        chocolatesunrise: str = '#E75116'

    class OptionSets(Settings):
        pass

    class Line(Settings):
        color: str = '#F41C5E'
        width: int = 2
        shape: str = 'spline'
        smoothing: float = 1.3

    class Camera(Settings):
        
        class Eye(Settings):
            x: float = 1
            y: float = 1
            z: float = 0.5
        
        eye = Eye()
    
    class Axis(Settings):

        class X(Settings):
            gridcolor="#515467"
            color='#8D91AA'
        
        class Y(Settings):
            gridcolor="#515467"
            color='#8D91AA'

        xaxis = X()
        yaxis = Y()

    class Scene(Settings):
        
        class XAxis(Settings):
            showgrid: bool = False
            backgroundcolor: str = 'rgba(0,0,0,0)'

        class YAxis(Settings):
            showgrid: bool = False
            backgroundcolor: str = 'rgba(0,0,0,0)'

        class ZAxis(Settings):
            showgrid: bool = False
            backgroundcolor: str = 'rgba(0,0,0,0)'

        class AspectRatio(Settings):
            x: float = 1
            y: float = 2
            z: float = 0.95

        xaxis = XAxis()
        yaxis = YAxis()
        zaxis = ZAxis()
        aspectratio = AspectRatio()
        bgcolor: str = 'rgba(0,0,0,0)'
    
    scene = Scene()
    camera = Camera()
    axis = Axis()
    gtypes = Type()
    gradients = GraphGradient()
    layout_colors = LayoutColors()
    basic_colors = BasicColors()
    option_sets = OptionSets()
    line = Line()


class SurfaceSettings(Settings):
    data: pd.DataFrame = None
    gset = GraphOptions()
    layout = go.Layout(
        paper_bgcolor=gset.layout_colors.paper_bgcolor,
        plot_bgcolor=gset.layout_colors.plot_bgcolor,
        height=500,
        width=800,
        xaxis=gset.axis.xaxis.dict(),
        yaxis=gset.axis.yaxis.dict(),
        scene=gset.scene.dict()
    )
    kwargs = dict(
        z=data,
        colorscale=gset.gradients.thermal,
        opacity=0.7
    )
    graph = go.Surface

class HeatmapSettings(Settings):
    data: pd.DataFrame = None
    gset = GraphOptions()
    layout = go.Layout(
        paper_bgcolor=gset.layout_colors.paper_bgcolor,
        plot_bgcolor=gset.layout_colors.plot_bgcolor,
        height=500,
        width=800,
        xaxis=gset.axis.xaxis.dict(),
        yaxis=gset.axis.yaxis.dict()  
    )
    kwargs = dict(
        z=data,
        colorscale=gset.gradients.inferno
    )
    graph = go.Heatmap

class ScatterSettings(Settings):
    data: pd.DataFrame = pd.DataFrame()
    gset = GraphOptions()
    layout = go.Layout(
        paper_bgcolor=gset.layout_colors.paper_bgcolor,
        plot_bgcolor=gset.layout_colors.plot_bgcolor,
        height=500,
        width=800,
        xaxis=gset.axis.xaxis.dict(),
        yaxis=gset.axis.yaxis.dict()
    )
    kwargs = dict(
        x=data.index,
        y=data,
        mode='lines',
        line=gset.line.dict()
    )
    graph = go.Scatter

class Coordinates(Settings):
    x: Union[list, tuple, np.ndarray, pd.DataFrame, pd.Series] = None
    y: Union[list, tuple, np.ndarray, pd.DataFrame, pd.Series] = None
    z: Union[list, tuple, np.ndarray, pd.DataFrame, pd.Series] = None