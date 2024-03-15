import plotly.graph_objects as go
import pandas as pd
import numpy as np
from audio_modules.xtract.XT.xtract_configs import *
from dataclasses import asdict, dataclass
from typing import Union
from array import array
from enum import Enum
from collections import deque

@dataclass
class SettingsConfiguration:
	class _GConfig:
		excluded_keys: list = ["_GConfig", "allsettings"]
		_excluded_defaults: list = ['dict', 'allsettings']

		@staticmethod
		def _filter(kv):
			k, v = kv
			return k not in Layout._GConfig.excluded_keys and v is not None

	def dict(self):
		cd = self.__class__.__dict__
		cd = dict(filter(lambda k: k[0] not in self._GConfig._excluded_defaults and k[1] is not None and not k[0].startswith("_"), cd.items()))
		d = self.__dict__

		cd.update(d)
		cd = dict(filter(lambda k: k[0] not in self._GConfig._excluded_defaults and k[1] is not None and not k[0].startswith("_"), cd.items()))
		d = filter(self._GConfig._filter, cd.items())
		d = {k: (v.dict() if (isinstance(v, SettingsConfiguration) or issubclass(v, SettingsConfiguration)) else v) for k, v in d}
		return dict(d)


@dataclass
class XAxis(SettingsConfiguration):

	zerolinewidth = None
	zerolinecolor = None
	zeroline = None
	visible = None
	uirevision = None
	type = None
	titlefont = None
	title = None
	tickwidth = None
	tickvalssrc = None
	tickvals = None
	ticktextsrc = None
	ticktext = None
	ticksuffix = None
	tickson = None
	ticks = None
	tickprefix = None
	tickmode = None
	ticklen = None
	ticklabelstep = None
	ticklabelposition = None
	ticklabeloverflow = None
	ticklabelmode = None
	tickformatstopdefaults = None
	tickformatstops = None
	tickformat = None
	tickfont = None
	tickcolor = None
	tickangle = None
	tick0 = None
	spikethickness = None
	spikesnap = None
	spikemode = None
	spikedash = None
	spikecolor = None
	side = None
	showticksuffix = None
	showtickprefix = None
	showticklabels = None
	showspikes = None
	showline = None
	showgrid = None
	showexponent = None
	showdividers = None
	separatethousands = None
	scaleratio = None
	scaleanchor = None
	rangeslider = None
	rangeselector = None
	rangemode = None
	rangebreakdefaults = None
	rangebreaks = None
	range = None
	position = None
	overlaying = None
	nticks = None
	mirror = None
	minor = None
	minexponent = None
	matches = None
	linewidth = None
	linecolor = None
	layer = None
	hoverformat = None
	gridwidth = None
	griddash = None
	gridcolor = None
	fixedrange = None
	exponentformat = None
	dtick = None
	domain = None
	dividerwidth = None
	dividercolor = None
	constraintoward = None
	constrain = None
	color = None
	categoryorder = None
	categoryarraysrc = None
	categoryarray = None
	calendar = None
	autotypenumbers = None
	autorange = None
	automargin = None
	anchor = None
	arg = None


@dataclass
class YAxis(SettingsConfiguration):

	zerolinewidth = None
	zerolinecolor = None
	zeroline = None
	visible = None
	uirevision = None
	type = None
	titlefont = None
	title = None
	tickwidth = None
	tickvalssrc = None
	tickvals = None
	ticktextsrc = None
	ticktext = None
	ticksuffix = None
	tickson = None
	ticks = None
	tickprefix = None
	tickmode = None
	ticklen = None
	ticklabelstep = None
	ticklabelposition = None
	ticklabeloverflow = None
	ticklabelmode = None
	tickformatstopdefaults = None
	tickformatstops = None
	tickformat = None
	tickfont = None
	tickcolor = None
	tickangle = None
	tick0 = None
	spikethickness = None
	spikesnap = None
	spikemode = None
	spikedash = None
	spikecolor = None
	side = None
	showticksuffix = None
	showtickprefix = None
	showticklabels = None
	showspikes = None
	showline = None
	showgrid = None
	showexponent = None
	showdividers = None
	shift = None
	separatethousands = None
	scaleratio = None
	scaleanchor = None
	rangemode = None
	rangebreakdefaults = None
	rangebreaks = None
	range = None
	position = None
	overlaying = None
	nticks = None
	mirror = None
	minor = None
	minexponent = None
	matches = None
	linewidth = None
	linecolor = None
	layer = None
	hoverformat = None
	gridwidth = None
	griddash = None
	gridcolor = None
	fixedrange = None
	exponentformat = None
	dtick = None
	domain = None
	dividerwidth = None
	dividercolor = None
	constraintoward = None
	constrain = None
	color = None
	categoryorder = None
	categoryarraysrc = None
	categoryarray = None
	calendar = None
	autotypenumbers = None
	autoshift = None
	autorange = None
	automargin = None
	anchor = None
	arg = None


@dataclass
class ZAxis(SettingsConfiguration):

	zerolinewidth = None
	zerolinecolor = None
	zeroline = None
	visible = None
	type = None
	titlefont = None
	title = None
	tickwidth = None
	tickvalssrc = None
	tickvals = None
	ticktextsrc = None
	ticktext = None
	ticksuffix = None
	ticks = None
	tickprefix = None
	tickmode = None
	ticklen = None
	tickformatstopdefaults = None
	tickformatstops = None
	tickformat = None
	tickfont = None
	tickcolor = None
	tickangle = None
	tick0 = None
	spikethickness = None
	spikesides = None
	spikecolor = None
	showticksuffix = None
	showtickprefix = None
	showticklabels = None
	showspikes = None
	showline = None
	showgrid = None
	showexponent = None
	showbackground = None
	showaxeslabels = None
	separatethousands = None
	rangemode = None
	range = None
	nticks = None
	mirror = None
	minexponent = None
	linewidth = None
	linecolor = None
	hoverformat = None
	gridwidth = None
	gridcolor = None
	exponentformat = None
	dtick = None
	color = None
	categoryorder = None
	categoryarraysrc = None
	categoryarray = None
	calendar = None
	backgroundcolor = None
	autotypenumbers = None
	autorange = None
	arg = None


@dataclass
class Font(SettingsConfiguration):

	size = None
	family = None
	color = None
	arg = None


@dataclass
class Marker(SettingsConfiguration):

	symbolsrc = None
	symbol = None
	standoffsrc = None
	standoff = None
	sizesrc = None
	sizeref = None
	sizemode = None
	sizemin = None
	size = None
	showscale = None
	reversescale = None
	opacitysrc = None
	opacity = None
	maxdisplayed = None
	line = None
	gradient = None
	colorsrc = None
	colorscale = None
	colorbar = None
	coloraxis = None
	color = None
	cmin = None
	cmid = None
	cmax = None
	cauto = None
	autocolorscale = None
	anglesrc = None
	angleref = None
	angle = None
	arg = None


@dataclass
class GraphLayoutExpanded:

	yaxis: YAxis = None
	xaxis: XAxis = None
	width = None
	waterfallmode = None
	waterfallgroupgap = None
	waterfallgap = None
	violinmode = None
	violingroupgap = None
	violingap = None
	updatemenudefaults = None
	updatemenus = None
	uniformtext = None
	uirevision = None
	treemapcolorway = None
	transition = None
	titlefont = None
	title = None
	ternary = None
	template = None
	sunburstcolorway = None
	spikedistance = None
	smith = None
	sliderdefaults = None
	sliders = None
	showlegend = None
	shapedefaults = None
	shapes = None
	separators = None
	selectiondefaults = None
	selections = None
	selectionrevision = None
	selectdirection = None
	scene = None
	scattermode = None
	scattergap = None
	polar = None
	plot_bgcolor = None
	piecolorway = None
	paper_bgcolor = None
	newshape = None
	newselection = None
	modebar = None
	minreducedwidth = None
	minreducedheight = None
	metasrc = None
	meta = None
	margin = None
	mapbox = None
	legend = None
	imagedefaults = None
	images = None
	iciclecolorway = None
	hovermode = None
	hoverlabel = None
	hoverdistance = None
	hidesources = None
	hiddenlabelssrc = None
	hiddenlabels = None
	height = None
	grid = None
	geo = None
	funnelmode = None
	funnelgroupgap = None
	funnelgap = None
	funnelareacolorway = None
	font: Font = None
	extendtreemapcolors = None
	extendsunburstcolors = None
	extendpiecolors = None
	extendiciclecolors = None
	extendfunnelareacolors = None
	editrevision = None
	dragmode = None
	datarevision = None
	computed = None
	colorway = None
	colorscale = None
	coloraxis = None
	clickmode = None
	calendar = None
	boxmode = None
	boxgroupgap = None
	boxgap = None
	barnorm = None
	barmode = None
	bargroupgap = None
	bargap = None
	autotypenumbers = None
	autosize = None
	annotationdefaults = None
	annotations = None
	activeshape = None
	activeselection = None
	arg = None
	

@dataclass
class Layout:
	class _GConfig:
		excluded_keys: list = ["_GConfig", "allsettings"]
		_excluded_defaults: list = ['dict', 'allsettings']

		@staticmethod
		def _filter(kv):
			k, v = kv
			return k not in Layout._GConfig.excluded_keys and v is not None


	allsettings = GraphLayoutExpanded()
	yaxis = None
	xaxis = None
	width = None
	height = None
	autosize = None
	font = None
	title = None
	titlefont = None
	legend = None
	showlegend = None
	margin = None
	annotations = None
	grid = None
	scene = None
	plot_bgcolor = "#121212"
	paper_bgcolor = "#121212"

	def dict(self):
		cd = self.__class__.__dict__
		cd = dict(filter(lambda k: k[0] not in self._GConfig._excluded_defaults and k[1] is not None and not k[0].startswith("_"), cd.items()))
		d = self.__dict__
		cd.update(d)
		cd = dict(filter(lambda k: k[0] not in self._GConfig._excluded_defaults and k[1] is not None and not k[0].startswith("_"), cd.items()))
		d = filter(self._GConfig._filter, cd.items())
		return dict(d)


@dataclass
class Figure(SettingsConfiguration):

	skip_invalid = False
	frames = None
	layout: Layout = None
	data = None


@dataclass
class Rotation(SettingsConfiguration):
	arg = None
	lat = None
	lon = None
	roll = None


@dataclass
class Eye(SettingsConfiguration):
	arg = None
	x = None
	y = None
	z = None


@dataclass
class Center(SettingsConfiguration):
	arg = None
	x = None
	y = None
	z = None


@dataclass
class Projection(SettingsConfiguration):
	arg = None
	distance = None
	parallels = None
	rotation: Rotation = None
	scale = None
	tilt = None
	type = None


@dataclass
class Up(SettingsConfiguration):
	arg = None
	x = None
	y = None
	z = None


@dataclass
class Camera(SettingsConfiguration):
	arg = None
	center: Center = None
	eye: Eye = None
	projection: Projection = None
	up: Up = None


@dataclass
class Lighting(SettingsConfiguration):
	arg = None
	ambient = None
	diffuse = None
	facenormalsepsilon = None
	fresnel = None
	roughness = None
	specular = None
	vertexnormalsepsilon = None


@dataclass
class Lightposition(SettingsConfiguration):
	arg = None
	x = None
	y = None
	z = None


@dataclass
class Aspectratio(SettingsConfiguration):
	arg = None
	x = None
	y = None
	z = None


@dataclass
class Activeselection(SettingsConfiguration):
	arg = None
	fillcolor = None
	opacity = None


@dataclass
class Transition(SettingsConfiguration):
	arg = None
	duration = None
	easing = None
	ordering = None


@dataclass
class Frame(SettingsConfiguration):
	arg = None
	baseframe = None
	data = None
	group = None
	layout: Layout = None
	name = None
	traces = None


@dataclass
class Scene(SettingsConfiguration):
	arg = None
	annotations = None
	annotationdefaults = None
	aspectmode = None
	aspectratio = None
	bgcolor = None
	camera = None
	domain = None
	dragmode = None
	hovermode = None
	uirevision = None
	xaxis: XAxis = None
	yaxis: YAxis = None
	zaxis: ZAxis = None


@dataclass
class Currentvalue(SettingsConfiguration):
	arg = None
	font: Font = None
	offset = None
	prefix = None
	suffix = None
	visible = None
	xanchor = None


@dataclass
class Slider(SettingsConfiguration):
	arg = None
	active = None
	activebgcolor = None
	bgcolor = None
	bordercolor = None
	borderwidth = None
	currentvalue: Currentvalue = None
	font: Font = None
	len = None
	lenmode = None
	minorticklen = None
	name = None
	pad = None
	steps = None
	stepdefaults = None
	templateitemname = None
	tickcolor = None
	ticklen = None
	tickwidth = None
	transition: Transition = None
	visible = None
	x = None
	xanchor = None
	y = None
	yanchor = None


class DimensionalType:

	def __init__(self, array=None):
		self._a = array
		self._d1 = array.shape[0] if array is not None else None
		self._d2 = array.shape[1] if array is not None and (len(array.shape) > 1) else None

	def step_into(self, arr):
		if arr is None:
			return self._a[0] if self.ndimensions > 1 else None
		else:
			return arr[0] if len(arr.shape) > 1 else arr
	
	def __floor_level__(self, a):
		if len(a.shape) == 1:
			return a
		else:
			return self.__floor_level__(self.step_into(a))
	
	def __setup__(self, value):
		if not isinstance(value, np.ndarray):
			value = np.array(value)
		self._d1 = value.shape[0]
		self._d2 = value.shape[1] if len(value.shape) > 1 else None
		self._a = value
		return value
	
	def __eq__(self, __value: object) -> bool:
		pass

	def __matmul__(self, __value: object) -> bool:
		return self.__eq__(__value)

	@property
	def ndimensions(self):
		return len(self._a.shape)
	
	@property
	def height(self):
		return len(self._a) if self.ndimensions > 1 else 0
	
	@property
	def width(self):
		if self.ndimensions == 1:
			return len(self._a)
		else:
			return len(self.__floor_level__(self._a))
	
	@property
	def depth(self):
		if self.ndimensions == 1:
			return 0
		lvl = 0
		arr = self._a
		while len(arr.shape) > 1:
			if len(arr.shape) == 1: break
			arr = self.step_into(arr)
			lvl += 1
		return lvl

class Iso(DimensionalType):
	"""
	Describes a 1 dimensional array that has a single row. 
	"""
	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		value = self.__setup__(value)
		return True if self.ndimensions == 1 else False
		
		def __matmul__(self, __value: object) -> bool:
			return self.__eq__(__value)
	
class Uni(DimensionalType):
	"""
	Describes a 2 dimensional array that is rectangular and has 1 row and 1 column.

	Example useage might be to determine if an audio signal is mono or if an array needs to be squeezed.
	"""
	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		value = self.__setup__(value)
		return True if self.ndimensions == 2 and self.height == 1 else False
		
	def __matmul__(self, __value: object) -> bool:
		return self.__eq__(__value)

class Twin(DimensionalType):
	"""
	Describes a 2 dimensional array that has 2 rows and 1 column.
	
	Example useage might be to determine if an audio signal is stereo.
	"""
	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		value = self.__setup__(value)
		return True if (self.ndimensions == 2 and self.height == 2) else False
	
	def __matmul__(self, __value: object) -> bool:
		return self.__eq__(__value)

class Tri(DimensionalType):
	"""
	Describes a 2 dimensional array that is rectangular and has 3 rows and 1 column.

	Example useage might be to determine if an array has the right size to be plotted
	onto a 3D graph.
	"""
	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		value = self.__setup__(value)
		return True if (self.ndimensions == 2 and self.height == 3 and self.depth == 1) else False
	
	def __matmul__(self, __value: object) -> bool:
		return self.__eq__(__value)

class Eso(DimensionalType):
	"""
	Describes a 2 dimensional array that is rectangular and has > 3 rows and 1 column.

	Example Useaage might be to determine if an array is over the size limit to be plotted to a 3D graph. 
	"""
	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		value = self.__setup__(value)
		return True if (self.ndimensions == 2 and self.height > 3 and self.depth == 1) else False
	
	def __matmul__(self, __value: object) -> bool:
		return self.__eq__(__value)
	
class Elon(DimensionalType):
	"""
	Short for Echelon and describes an array that is multidimensional, arranged in a heirarchy of 3 or more levels.
	""" 
	def __eq__(self, value):
		if not np.iterable(value):
			return False
		if not isinstance(value, (list, tuple, np.ndarray, array)):
			return False
		value = self.__setup__(value)
		return True if (self.ndimensions == 2 and self.height > 3 and self.depth > 1) else False
	
	def __matmul__(self, __value: object) -> bool:
		return self.__eq__(__value)

@dataclass
class Dtypes:
	Iso = Iso()
	Uni = Uni()
	Twin = Twin()
	Tri = Tri()
	Eso = Eso()
	Elon = Elon()

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


class FigureConfig(BaseModel):

	class Config:
		arbitrary_types_allowed = True

	plot_bgcolor= '#121212'
	paper_bgcolor = '#121212'
	annotationdefaults = dict(font=dict(color="#ffffff"))
	font_color = 'white'
	scene = dict(
		xaxis = dict(
			showgrid = False, 
			backgroundcolor = 'rgba(0, 0, 0,0)', 
			range = [500, 3000]
			),
		yaxis = dict(
			showgrid = False,
			backgroundcolor = 'rgba(0, 0, 0,0)',
			),
		zaxis = dict(
			showgrid = False,
			backgroundcolor = 'rgba(0, 0, 0,0)'
			),
		)
	
@dataclass
class XAxisConfig:

	arg = None
	anchor = None
	automargin = None
	autorange = None
	backgroundcolor = 'rgba(0, 0, 0,0)'
	categoryarray = None
	categoryorder = None
	color = None
	dividercolor = None
	dividerwidth = None
	gridcolor = None
	gridwidth = None
	layer = None
	linecolor = None
	linewidth = None
	overlaying = None
	position = None
	range = None
	rangemode = None
	rangeselector = None
	rangeslider = None
	scaleratio = None
	showdividers = None
	showexponent = None
	showgrid = False
	showline = None
	showspikes = None
	showticklabels = None
	showtickprefix = None
	showticksuffix = None
	side = None
	spikecolor = None
	spikethickness = None
	tick0 = None
	tickangle = None
	tickcolor = None
	tickfont = None
	ticklabelposition = None
	ticklen = None
	tickmode = None
	ticks = None
	ticktext = None
	tickwidth = None
	title = None
	titlefont = None
	type = None
	uirevision = None
	visible = None
	zeroline = None
	zerolinecolor = None
	zerolinewidth = None
"""
fig_props = {
	'plot_bgcolor' = '#121212', 
	'paper_bgcolor' = '#121212', 
	'annotationdefaults' = dict(font=dict(color="#ffffff")),
	'font_color' = 'white',
	'scene' = {
	'xaxis' = {
	'showgrid' = False,
	'backgroundcolor' = 'rgba(0, 0, 0,0)',
	'range' = [500, 3000]
	},
	'yaxis' = {
	'showgrid' = False,
	'backgroundcolor' = 'rgba(0, 0, 0,0)',
	},
	'zaxis' = {
	'showgrid' = False,
	'backgroundcolor' = 'rgba(0, 0, 0,0)',
	}
	}
	}
fig = go.Figure(data=[go.Mesh3d(
	x=Tf,
	y=Hf,
	z=Af,
	intensity=Af,   # set color to an array/list of desired values
	colorscale=px.colors.sequential.Plasma[1:],   # choose a colorscale
	opacity=0.9,
	#coloraxis='coloraxis3'
	)],
	layout=fig_props
)

# tight layout
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.show()
"""