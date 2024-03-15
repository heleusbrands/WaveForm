from __future__ import annotations
from pydantic.v1 import BaseModel
from .plotly_mappings import Settings
from typing import Any
from collections import UserList
from dash import dcc, html
from random import randint

class HProp(Settings):
	align_content: Any = None
	align_items: Any = None
	align_self: Any = None
	all: Any = None
	animation: Any = None
	animation_delay: Any = None
	animation_direction: Any = None
	animation_duration: Any = None
	animation_fill_mode: Any = None
	animation_iteration_count: Any = None
	animation_name: Any = None
	animation_play_state: Any = None
	animation_timing_function: Any = None
	backface_visibility: Any = None
	background: Any = None
	background_attachment: Any = None
	background_blend_mode: Any = None
	background_clip: Any = None
	background_color: Any = None
	background_image: Any = None
	background_origin: Any = None
	background_position: Any = None
	background_repeat: Any = None
	background_size: Any = None
	border: Any = None
	border_bottom: Any = None
	border_bottom_color: Any = None
	border_bottom_left_radius: Any = None
	border_bottom_right_radius: Any = None
	border_bottom_style: Any = None
	border_bottom_width: Any = None
	border_collapse: Any = None
	border_color: Any = None
	border_image: Any = None
	border_image_outset: Any = None
	border_image_repeat: Any = None
	border_image_slice: Any = None
	border_image_source: Any = None
	border_image_width: Any = None
	border_left: Any = None
	border_left_color: Any = None
	border_left_style: Any = None
	border_left_width: Any = None
	border_radius: Any = None
	border_right: Any = None
	border_right_color: Any = None
	border_right_style: Any = None
	border_right_width: Any = None
	border_spacing: Any = None
	border_style: Any = None
	border_top: Any = None
	border_top_color: Any = None
	border_top_left_radius: Any = None
	border_top_right_radius: Any = None
	border_top_style: Any = None
	border_top_width: Any = None
	border_width: Any = None
	bottom: Any = None
	box_shadow: Any = None
	box_sizing: Any = None
	caption_side: Any = None
	caret_color: Any = None
	clear: Any = None
	clip: Any = None
	clip_path: Any = None
	color: Any = None
	column_count: Any = None
	column_fill: Any = None
	column_gap: Any = None
	column_rule: Any = None
	column_rule_color: Any = None
	column_rule_style: Any = None
	column_rule_width: Any = None
	column_span: Any = None
	column_width: Any = None
	columns: Any = None
	content: Any = None
	counter_increment: Any = None
	counter_reset: Any = None
	cursor: Any = None
	direction: Any = None
	display: Any = None
	empty_cells: Any = None
	filter: Any = None
	flex: Any = None
	flex_basis: Any = None
	flex_direction: Any = None
	flex_flow: Any = None
	flex_grow: Any = None
	flex_shrink: Any = None
	flex_wrap: Any = None
	float: Any = None
	font: Any = None
	font_family: Any = None
	font_kerning: Any = None
	font_size: Any = None
	font_size_adjust: Any = None
	font_stretch: Any = None
	font_style: Any = None
	font_variant: Any = None
	font_weight: Any = None
	grid: Any = None
	grid_area: Any = None
	grid_auto_columns: Any = None
	grid_auto_flow: Any = None
	grid_auto_rows: Any = None
	grid_column: Any = None
	grid_column_end: Any = None
	grid_column_gap: Any = None
	grid_column_start: Any = None
	grid_gap: Any = None
	grid_row: Any = None
	grid_row_end: Any = None
	grid_row_gap: Any = None
	grid_row_start: Any = None
	grid_template: Any = None
	grid_template_areas: Any = None
	grid_template_columns: Any = None
	grid_template_rows: Any = None
	height: Any = None
	hyphens: Any = None
	justify_content: Any = None
	left: Any = None
	letter_spacing: Any = None
	line_height: Any = None
	list_style: Any = None
	list_style_image: Any = None
	list_style_position: Any = None
	list_style_type: Any = None
	margin: Any = None
	margin_bottom: Any = None
	margin_left: Any = None
	margin_right: Any = None
	margin_top: Any = None
	max_height: Any = None
	max_width: Any = None
	min_height: Any = None
	min_width: Any = None
	object_fit: Any = None
	object_position: Any = None
	opacity: Any = None
	order: Any = None
	outline: Any = None
	outline_color: Any = None
	outline_offset: Any = None
	outline_style: Any = None
	outline_width: Any = None
	overflow: Any = None
	overflow_x: Any = None
	overflow_y: Any = None
	padding: Any = None
	padding_bottom: Any = None
	padding_left: Any = None
	padding_right: Any = None
	padding_top: Any = None
	page_break_after: Any = None
	page_break_before: Any = None
	page_break_inside: Any = None
	perspective: Any = None
	perspective_origin: Any = None
	pointer_events: Any = None
	position: Any = None
	quotes: Any = None
	right: Any = None
	scroll_behavior: Any = None
	table_layout: Any = None
	text_align: Any = None
	text_align_last: Any = None
	text_decoration: Any = None
	text_decoration_color: Any = None
	text_decoration_line: Any = None
	text_decoration_style: Any = None
	text_indent: Any = None
	text_justify: Any = None
	text_overflow: Any = None
	text_shadow: Any = None
	text_transform: Any = None
	top: Any = None
	transform: Any = None
	transform_origin: Any = None
	transform_style: Any = None
	transition: Any = None
	transition_delay: Any = None
	transition_duration: Any = None
	transition_property: Any = None
	transition_timing_function: Any = None
	user_select: Any = None
	vertical_align: Any = None
	visibility: Any = None
	white_space: Any = None
	width: Any = None
	word_break: Any = None
	word_spacing: Any = None
	word_wrap: Any = None
	writing_mode: Any = None
	z_index: Any = None

class HtmlBase(UserList):

	def __init__(self):
		super().__init__()
		self.id = str(randint(1000000000, 9999999999))
		self._parent = None
		self._style = HProp()
		self._layout_type = None
		self._settings = None

	@property
	def styling_properties(self):
		return self._style
	
	@property
	def styles(self):
		return self.styling_properties.dict(exclude_none = True)

	@property
	def layout(self):
		args = self._settings.dict().keys()
		self._settings.id = self.id
		if 'style' in args and self._style is not None:
			self._settings.style = self._style.dict(exclude_none=True)
		if 'children' in args and len(self) > 0:
			self._settings.children = [child.layout for child in self]
		return self._layout_type(**self._settings.dict(exclude_none=True))

	@property
	def layout_type(self):
		return self._layout_type
	
	@property
	def settings(self):
		return self._settings
	
	@settings.setter
	def settings(self, value):
		self._settings = value
	
	@property
	def parent(self):
		return self._parent
	
	@parent.setter
	def parent(self, value):
		self._parent = value

	def add(self, obj: HtmlBase):
		self.append(obj)
		return self
	
	def __add__(self, obj: HtmlBase):
		return self.add(obj)
	
	def __matmul__(self, obj: HtmlBase):
		if type(obj) != type(self):
			raise TypeError(f"Cannot add {type(obj)} to {type(self)}")
		self.parent = obj
		return obj.add(self)