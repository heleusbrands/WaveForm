from dash import Dash, dash_table, Patch
import pandas as pd
from dash.dependencies import Input, Output, State
from plotly import graph_objs as go
from plotly.express import scatter, line
import plotly.io as pio
import numpy as np
import soundfile as sf
import dash
import dash_core_components as dcc
import dash_html_components as html
from pydub import AudioSegment
from collections import deque
from pydantic import BaseModel
from tempfile import NamedTemporaryFile
from itertools import islice, repeat, chain
from air import *
from waveform import WaveForm

FILE = 'xpression\\xtract\\03-01-05-02-02-01-01.wav'
DATA: AudioSegment = AudioSegment.from_wav(FILE)

WINDOWLEN = 1000
SLIDELEN = 100
BINLEN = 100
SECONDS = DATA.duration_seconds
FRAMES = int(SECONDS * 30)
BANDS = 32

LOADBUFFER: deque[np.ndarray] = deque()
POSITIONBUFFER: deque[tuple] = deque()

XMIN = 0
XMAX = None
YMIN = None
YMAX = None

CSSFILE = None

class LineSettings(BaseModel):
    color: str = '#F41C5E'
    width: int = 2
    shape: str = 'spline'
    smoothing: float = 1.3

class AppStyles(BaseModel):
    backgroundColor: str = '#121212'
    textAlign: str = 'center'
    color: str = '#474A5D'

class App(AppStyles):
    width: str = '100%'
    height: str = '100vh'
    margin: str = '0'
    padding: str = '0'
class Layout(BaseModel):
    class Config:
        orm_mode = True
        extra = 'allow'
        arbitrary_types_allowed = True
        allow_population_by_field_name = True

class MainLayout(Layout):
    children: list[Layout] = []
    style: dict = None

class XpressionDashboard:

    def __init__(self):
        self._layout = []
        self.app = Dash(self.__class__.__name__)
        self.set_index()
        self.main_layout = MainLayout(style=App().dict(exclude={'textAlign'}))

    def set_index(self):
        self.app.index_string ='''
        <!DOCTYPE html>
        <html>
            <head>
                {%metas%}
                <title>{%title%}</title>
                {%favicon%}
                {%css%}
                <style>
                    body {
                        background-color: #121212;
                        margin: 0;
                        padding: 0;
                    }
                </style>
            </head>
            <body>
                <div>My Custom header</div>
                {%app_entry%}
                <footer>
                    {%config%}
                    {%scripts%}
                    {%renderer%}
                </footer>
                <div>My Custom footer</div>
            </body>
        </html>
        '''



def create_figure():
    global XMIN
    global XMAX
    global YMIN
    global YMAX
    global WINDOWLEN
    global SLIDELEN

    data = DATA.get_array_of_samples()
    rate = DATA.frame_rate # The sampling rate for the audio, in samples per second.
    msrate = rate / 1000 # The sampling rate per millisecond.
    x = np.arange(len(data)) / rate # The entire time scale for the audio, in seconds.
    y = np.array(data) # The entire signal for the audio, in samples.

    XMIN = 0
    XMAX = 100 * msrate # Meaning that we'll be displaying 100ms of audio at a time. This would result in 30s frame for a 3 second audio file, so it might need to be reduced a bit so we have more frames.
    WINDOWLEN = XMAX # As it happens, the XMAX is also the window length, as it's the number of samples we want to display at a time.
    YMIN = min(data)
    YMAX = DATA.max
    frame_sliced = adumpwindow(abatched(y, FRAMES))
    frames = [adumpwindow(abatched(a, BANDS)) for a in adumpwindow(abatched(y, FRAMES))]
    yframes = np.array([blur(i) for i in frames])
    aframe = np.array([i for i in range(len(yframes))])
    
    
    dataframe = pd.DataFrame({'Time': xbins, 'Signal': ybins, 'Frame': aframe})
    fig = scatter(dataframe, x=dataframe['Time'], y=dataframe['Signal'], animation_frame='Frame', animation_group='Frame', color='Signal',color_continuous_scale='plasma', template='plotly_dark', range_x=[XMIN, XMAX], range_y=[YMIN, YMAX])
    return fig


app = Dash(__name__)
fig = create_figure()

app.index_string ='''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            body {
                background-color: #121212;
                margin: 0;
                padding: 0;
            }
        </style>
    </head>
    <body>
        <div>My Custom header</div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>My Custom footer</div>
    </body>
</html>
'''

app.layout = html.Main(
    style=App().dict(exclude={'textAlign'}),
    children=[

        html.Div(
            style=App().dict(exclude={'textAlign'}), 
            children=[
                
                dcc.Store(id='memory'),
                dcc.Store(id='session', storage_type='session'),

                html.H1(
                    children='XPRESS DASHBOARD',
                    style=AppStyles().dict(exclude={'backgroundColor'})
                ),

                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
                    ]),
                    style={
                        'width': '100%',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                    },
                ),

                dcc.Graph(
                    id='live-update-graph', 
                    figure=fig
                ), 

                dcc.Interval(
                    id='interval-component',
                    interval=SLIDELEN,  # in milliseconds
                    n_intervals=0
                )
    ])])
    

if __name__ == '__main__':
    app.run_server(debug=True, port=8051)