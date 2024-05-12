import plotly.graph_objects as go
import pandas as pd
import numpy as np
from audio_modules.extraction.extract_configs import *
from pydantic.v1 import BaseModel
from pydantic.v1.dataclasses import dataclass
from typing import Union
from array import array
from collections import deque
from ..air import *
from .plotly_mappings import Layout, Transition, Gradient, Scatter, Line, Marker, Bar, Box, Histogram, Heatmap, Contour, Surface, Mesh3d, Scatter3d, Scene, XAxis, YAxis, ZAxis, Figure, Project, Frame, Settings

GraphType = Union[go.Scatter, go.Line, go.Bar, go.Box, go.Histogram, go.Heatmap, go.Contour, go.Surface, go.Mesh3d, go.Scatter3d]

class CoordinateDomType(Settings):
	x: DomainType = None
	y: DomainType = None
	z: DomainType = None

class NGtype(BaseModel):
	"""
	domain: DomainType
		if the data is consistent with an audio domain type, the domain type will be added here.
	dimension: DimensionalType
		attempts to determin the audio shape configuration, in order to determine the graph type.
		dimension types are - Iso, Uni, Twin, Tri, Eso, and Elon
	coordinates: Project
		coordinates of the graph, if the graph is 3D, the coordinates will be 3D, otherwise 2D.
	isair: bool
		whether or not the data is already in the form of an AirArray object, as this reduces the 
		number of calculations needed.
	isconfigured: bool
		whether or not the NGtype has already be configured for the data. If data is changed, this
		gets set to False to signal that it needs to be reevaluated.
	gtype: GraphType
		the graph type, determined by the dimension type and/or the domain type.
	data: Union[None, pd.DataFrame, pd.Series, np.ndarray, array, list, tuple, deque]
		the data to be graphed.
	"""
	class Config:
		arbitrary_types_allowed = True
		allow_mutations = True
		extra = 'allow'
		orm_mode = True
		underscore_attrs_are_private = True
		exclude_none = True

	domain: DomainType = None
	dimensions: CoordinateDomType = CoordinateDomType()
	coordinates: Project = Project()
	isair: bool = False
	isconfigured: bool = False
	gtype: GraphType = None
	data: Union[None, pd.DataFrame, pd.Series, np.ndarray, array, list, tuple, deque] = None

class NGraphBase:

	def __init__(self, data = None):
		self._data = data
		self._layout = Layout()
		self._figure = Figure()
		self._transition = self._layout.transition
		self._line = Line()
		self._marker = Marker()
		self._gradient = self._marker.gradient
		self._scene = self._layout.scene
		self._xaxis = self._layout.xaxis
		self._yaxis = self._layout.yaxis
		self._zaxis = self._scene.zaxis
		self._ngtype = NGtype()

	@property
	def ngtype(self) -> NGtype:
		if self._ngtype.isconfigured:
			return self._ngtype
		else:
			self._ngtype.data = self._data
			self._ngtype.dimension = NDtype(self._data)
			self._ngtype.isair = any((isinstance(self._data, AirArray) or issubclass(type(self._data), AirArray)))
		return self._ngtype

	@property
	def graph_figure(self) -> Figure:
		return self._figure

	@property
	def layout(self) -> Layout:
		return self._layout
	
	@property
	def transition(self) -> Transition:
		return self._transition
	
	@property
	def gradient(self) -> Gradient:
		return self._gradient
	
	@property
	def line(self) -> Line:
		return self._line
	
	@property
	def marker(self) -> Marker:
		return self._marker
	
	@property
	def scene(self) -> Scene:
		return self._scene
	
	@property
	def xaxis(self) -> XAxis:
		return self._xaxis
	
	@property
	def yaxis(self) -> YAxis:
		return self._yaxis
	
	@property
	def zaxis(self) -> ZAxis:
		return self._zaxis


	def __set_defaults__(self):
		pass






