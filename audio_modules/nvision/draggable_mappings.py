from __future__ import annotations
from pydantic.v1 import BaseModel
from .plotly_mappings import Settings
from typing import Any
from collections import UserList
from dash import dcc, html
from random import randint
import dash_draggable
from .mapping_base import HtmlBase


class DashboardItem(Settings):
	children: Any = None
	i: Any = None
	x: Any = None
	y: Any = None
	w: Any = None
	h: Any = None
	static: Any = None
	isDraggable: Any = None
	isResizable: Any = None
	isBounded: Any = None
	maxH: Any = None
	maxW: Any = None
	minH: Any = None
	minW: Any = None
	moved: Any = None
	resizeHandles: Any = None

class DashboardItemResponsive(Settings):
	children: Any = None
	id: Any = None
	x: Any = None
	y: Any = None
	w: Any = None
	h: Any = None
	static: Any = None
	isDraggable: Any = None
	isResizable: Any = None
	isBounded: Any = None
	maxH: Any = None
	maxW: Any = None
	minH: Any = None
	minW: Any = None
	moved: Any = None
	resizeHandles: Any = None
	_DashboardItemResponsive__isDashboardItem: Any = None

class DraggableDashboard(Settings):
	children: Any = None
	id: Any = None
	layout: Any = None
	save: Any = None
	clearSavedLayout: Any = None
	ncols: Any = None
	nrows: Any = None
	width: Any = None
	height: Any = None
	className: Any = None
	style: Any = None

class DraggableDashboardResponsive(Settings):
	children: Any = None
	id: Any = None
	layouts: Any = None
	breakpoints: Any = None
	gridCols: Any = None
	save: Any = None
	clearSavedLayout: Any = None
	ncols: Any = None
	nrows: Any = None
	height: Any = None
	className: Any = None
	style: Any = None

class GridLayout(Settings):
	children: Any = None
	id: Any = None
	layout: Any = None
	save: Any = None
	clearSavedLayout: Any = None
	ncols: Any = None
	nrows: Any = None
	width: Any = None
	gridCols: Any = None
	height: Any = None
	className: Any = None
	style: Any = None
	autoSize: Any = None
	draggableCancel: Any = None
	draggableHandle: Any = None
	verticalCompact: Any = None
	compactType: Any = None
	margin: Any = None
	containerPadding: Any = None
	isDraggable: Any = None
	isResizable: Any = None
	isBounded: Any = None
	useCSSTransforms: Any = None
	transformScale: Any = None
	preventCollision: Any = None
	isDroppable: Any = None
	resizeHandles: Any = None

class ResponsiveGridLayout(Settings):
	children: Any = None
	id: Any = None
	layouts: Any = None
	breakpoints: Any = None
	gridCols: Any = None
	save: Any = None
	clearSavedLayout: Any = None
	ncols: Any = None
	nrows: Any = None
	height: Any = None
	className: Any = None
	style: Any = None
	autoSize: Any = None
	draggableCancel: Any = None
	draggableHandle: Any = None
	verticalCompact: Any = None
	compactType: Any = None
	margin: Any = None
	containerPadding: Any = None
	isDraggable: Any = None
	isResizable: Any = None
	isBounded: Any = None
	useCSSTransforms: Any = None
	transformScale: Any = None
	preventCollision: Any = None
	isDroppable: Any = None
	resizeHandles: Any = None


class DraggableContainer(HtmlBase):

	def __init__(self, parent=None):
		super().__init__()
		self.parent = parent

	@property
	def dashboarditem(self):
		self._layout_type = dash_draggable.DashboardItem
		if type(self.settings) != DashboardItem: self.settings: DashboardItem = DashboardItem()
		return self.settings

	@property
	def dashboarditemresponsive(self):
		self._layout_type = dash_draggable.DashboardItemResponsive
		if type(self.settings) != DashboardItemResponsive: self.settings: DashboardItemResponsive = DashboardItemResponsive()
		return self.settings

	@property
	def draggabledashboard(self):
		self._layout_type = dash_draggable.DraggableDashboard
		if type(self.settings) != DraggableDashboard: self.settings: DraggableDashboard = DraggableDashboard()
		return self.settings

	@property
	def draggabledashboardresponsive(self):
		self._layout_type = dash_draggable.DraggableDashboardResponsive
		if type(self.settings) != DraggableDashboardResponsive: self.settings: DraggableDashboardResponsive = DraggableDashboardResponsive()
		return self.settings

	@property
	def gridlayout(self):
		self._layout_type = dash_draggable.GridLayout
		if type(self.settings) != GridLayout: self.settings: GridLayout = GridLayout()
		return self.settings

	@property
	def responsivegridlayout(self):
		self._layout_type = dash_draggable.ResponsiveGridLayout
		if type(self.settings) != ResponsiveGridLayout: self.settings: ResponsiveGridLayout = ResponsiveGridLayout()
		return self.settings