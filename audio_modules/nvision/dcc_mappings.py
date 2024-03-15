from __future__ import annotations
from pydantic.v1 import BaseModel
from .plotly_mappings import Settings
from .mapping_base import HtmlBase
from typing import Any
from collections import UserList
from dash import dcc
from random import randint


class Checklist(Settings):
	options: Any = None
	value: Any = None
	inline: Any = None
	className: Any = None
	style: Any = None
	inputStyle: Any = None
	inputClassName: Any = None
	labelStyle: Any = None
	labelClassName: Any = None
	id: Any = None
	loading_state: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class Clipboard(Settings):
	id: Any = None
	target_id: Any = None
	content: Any = None
	n_clicks: Any = None
	title: Any = None
	style: Any = None
	className: Any = None
	loading_state: Any = None

class ConfirmDialog(Settings):
	id: Any = None
	message: Any = None
	submit_n_clicks: Any = None
	submit_n_clicks_timestamp: Any = None
	cancel_n_clicks: Any = None
	cancel_n_clicks_timestamp: Any = None
	displayed: Any = None

class ConfirmDialogProvider(Settings):
	children: Any = None
	id: Any = None
	message: Any = None
	submit_n_clicks: Any = None
	submit_n_clicks_timestamp: Any = None
	cancel_n_clicks: Any = None
	cancel_n_clicks_timestamp: Any = None
	displayed: Any = None
	loading_state: Any = None

class DatePickerRange(Settings):
	start_date: Any = None
	end_date: Any = None
	min_date_allowed: Any = None
	max_date_allowed: Any = None
	disabled_days: Any = None
	minimum_nights: Any = None
	updatemode: Any = None
	start_date_placeholder_text: Any = None
	end_date_placeholder_text: Any = None
	initial_visible_month: Any = None
	clearable: Any = None
	reopen_calendar_on_clear: Any = None
	display_format: Any = None
	month_format: Any = None
	first_day_of_week: Any = None
	show_outside_days: Any = None
	stay_open_on_select: Any = None
	calendar_orientation: Any = None
	number_of_months_shown: Any = None
	with_portal: Any = None
	with_full_screen_portal: Any = None
	day_size: Any = None
	is_RTL: Any = None
	disabled: Any = None
	start_date_id: Any = None
	end_date_id: Any = None
	style: Any = None
	className: Any = None
	id: Any = None
	loading_state: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class DatePickerSingle(Settings):
	date: Any = None
	min_date_allowed: Any = None
	max_date_allowed: Any = None
	disabled_days: Any = None
	placeholder: Any = None
	initial_visible_month: Any = None
	clearable: Any = None
	reopen_calendar_on_clear: Any = None
	display_format: Any = None
	month_format: Any = None
	first_day_of_week: Any = None
	show_outside_days: Any = None
	stay_open_on_select: Any = None
	calendar_orientation: Any = None
	number_of_months_shown: Any = None
	with_portal: Any = None
	with_full_screen_portal: Any = None
	day_size: Any = None
	is_RTL: Any = None
	disabled: Any = None
	style: Any = None
	className: Any = None
	id: Any = None
	loading_state: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class Download(Settings):
	id: Any = None
	data: Any = None
	base64: Any = None
	type: Any = None

class Dropdown(Settings):
	options: Any = None
	value: Any = None
	multi: Any = None
	clearable: Any = None
	searchable: Any = None
	search_value: Any = None
	placeholder: Any = None
	disabled: Any = None
	optionHeight: Any = None
	maxHeight: Any = None
	style: Any = None
	className: Any = None
	id: Any = None
	loading_state: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class Geolocation(Settings):
	id: Any = None
	local_date: Any = None
	timestamp: Any = None
	position: Any = None
	position_error: Any = None
	show_alert: Any = None
	update_now: Any = None
	high_accuracy: Any = None
	maximum_age: Any = None
	timeout: Any = None

class Graph(Settings):
	id: Any = None
	responsive: Any = None
	clickData: Any = None
	clickAnnotationData: Any = None
	hoverData: Any = None
	clear_on_unhover: Any = None
	selectedData: Any = None
	relayoutData: Any = None
	extendData: Any = None
	prependData: Any = None
	restyleData: Any = None
	figure: Any = None
	style: Any = None
	className: Any = None
	mathjax: Any = None
	animate: Any = None
	animation_options: Any = None
	config: Any = None
	loading_state: Any = None

class Input(Settings):
	value: Any = None
	type: Any = None
	debounce: Any = None
	placeholder: Any = None
	n_submit: Any = None
	n_submit_timestamp: Any = None
	inputMode: Any = None
	autoComplete: Any = None
	readOnly: Any = None
	required: Any = None
	autoFocus: Any = None
	disabled: Any = None
	list: Any = None
	multiple: Any = None
	spellCheck: Any = None
	name: Any = None
	min: Any = None
	max: Any = None
	step: Any = None
	minLength: Any = None
	maxLength: Any = None
	pattern: Any = None
	selectionStart: Any = None
	selectionEnd: Any = None
	selectionDirection: Any = None
	n_blur: Any = None
	n_blur_timestamp: Any = None
	size: Any = None
	style: Any = None
	className: Any = None
	id: Any = None
	loading_state: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class Interval(Settings):
	id: Any = None
	interval: Interval = None
	disabled: Any = None
	n_intervals: Any = None
	max_intervals: Any = None

Interval.update_forward_refs()

class Link(Settings):
	children: Any = None
	href: Any = None
	target: Any = None
	refresh: Any = None
	title: Any = None
	className: Any = None
	style: Any = None
	id: Any = None
	loading_state: Any = None

class Loading(Settings):
	children: Any = None
	id: Any = None
	type: Any = None
	fullscreen: Any = None
	debug: Any = None
	className: Any = None
	parent_className: Any = None
	style: Any = None
	parent_style: Any = None
	color: Any = None
	loading_state: Any = None

class Location(Settings):
	id: Any = None
	pathname: Any = None
	search: Any = None
	hash: Any = None
	href: Any = None
	refresh: Any = None

class LogoutButton(Settings):
	id: Any = None
	label: Any = None
	logout_url: Any = None
	style: Any = None
	method: Any = None
	className: Any = None
	loading_state: Any = None

class Markdown(Settings):
	children: Any = None
	id: Any = None
	className: Any = None
	mathjax: Any = None
	dangerously_allow_html: Any = None
	link_target: Any = None
	dedent: Any = None
	highlight_config: Any = None
	loading_state: Any = None
	style: Any = None

class RadioItems(Settings):
	options: Any = None
	value: Any = None
	inline: Any = None
	style: Any = None
	className: Any = None
	inputStyle: Any = None
	inputClassName: Any = None
	labelStyle: Any = None
	labelClassName: Any = None
	id: Any = None
	loading_state: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class Tooltip(Settings):
	children: Any = None
	id: Any = None
	className: Any = None
	style: Any = None
	bbox: Any = None
	show: Any = None
	direction: Any = None
	border_color: Any = None
	background_color: Any = None
	loading_text: Any = None
	zindex: Any = None
	targetable: Any = None
	loading_state: Any = None

class RangeSlider(Settings):
	min: Any = None
	max: Any = None
	step: Any = None
	marks: Any = None
	value: Any = None
	drag_value: Any = None
	allowCross: Any = None
	pushable: Any = None
	disabled: Any = None
	count: Any = None
	dots: Any = None
	included: Any = None
	tooltip: Tooltip = None
	updatemode: Any = None
	vertical: Any = None
	verticalHeight: Any = None
	className: Any = None
	id: Any = None
	loading_state: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class Slider(Settings):
	min: Any = None
	max: Any = None
	step: Any = None
	marks: Any = None
	value: Any = None
	drag_value: Any = None
	disabled: Any = None
	dots: Any = None
	included: Any = None
	tooltip: Tooltip = None
	updatemode: Any = None
	vertical: Any = None
	verticalHeight: Any = None
	className: Any = None
	id: Any = None
	loading_state: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class Store(Settings):
	id: Any = None
	storage_type: Any = None
	data: Any = None
	clear_data: Any = None
	modified_timestamp: Any = None

class Tab(Settings):
	children: Any = None
	id: Any = None
	label: Any = None
	value: Any = None
	disabled: Any = None
	disabled_style: Any = None
	disabled_className: Any = None
	className: Any = None
	selected_className: Any = None
	style: Any = None
	selected_style: Any = None
	loading_state: Any = None

class Tabs(Settings):
	children: Any = None
	id: Any = None
	value: Any = None
	className: Any = None
	content_className: Any = None
	parent_className: Any = None
	style: Any = None
	parent_style: Any = None
	content_style: Any = None
	vertical: Any = None
	mobile_breakpoint: Any = None
	colors: Any = None
	loading_state: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class Textarea(Settings):
	id: Any = None
	value: Any = None
	autoFocus: Any = None
	cols: Any = None
	disabled: Any = None
	form: Any = None
	maxLength: Any = None
	minLength: Any = None
	name: Any = None
	placeholder: Any = None
	readOnly: Any = None
	required: Any = None
	rows: Any = None
	wrap: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Any = None
	n_blur: Any = None
	n_blur_timestamp: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	loading_state: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class Upload(Settings):
	children: Any = None
	id: Any = None
	contents: Any = None
	filename: Any = None
	last_modified: Any = None
	accept: Any = None
	disabled: Any = None
	disable_click: Any = None
	max_size: Any = None
	min_size: Any = None
	multiple: Any = None
	className: Any = None
	className_active: Any = None
	className_reject: Any = None
	className_disabled: Any = None
	style: Any = None
	style_active: Any = None
	style_reject: Any = None
	style_disabled: Any = None
	loading_state: Any = None


class Component(HtmlBase):

	def __init__(self, parent=None):
		super().__init__()
		self.parent = parent

	@property
	def checklist(self):
		self._layout_type = dcc.Checklist
		if type(self.settings) != Checklist: self.settings: Checklist = Checklist()
		return self.settings

	@property
	def clipboard(self):
		self._layout_type = dcc.Clipboard
		if type(self.settings) != Clipboard: self.settings: Clipboard = Clipboard()
		return self.settings

	@property
	def confirmdialog(self):
		self._layout_type = dcc.ConfirmDialog
		if type(self.settings) != ConfirmDialog: self.settings: ConfirmDialog = ConfirmDialog()
		return self.settings

	@property
	def confirmdialogprovider(self):
		self._layout_type = dcc.ConfirmDialogProvider
		if type(self.settings) != ConfirmDialogProvider: self.settings: ConfirmDialogProvider = ConfirmDialogProvider()
		return self.settings

	@property
	def datepickerrange(self):
		self._layout_type = dcc.DatePickerRange
		if type(self.settings) != DatePickerRange: self.settings: DatePickerRange = DatePickerRange()
		return self.settings

	@property
	def datepickersingle(self):
		self._layout_type = dcc.DatePickerSingle
		if type(self.settings) != DatePickerSingle: self.settings: DatePickerSingle = DatePickerSingle()
		return self.settings

	@property
	def download(self):
		self._layout_type = dcc.Download
		if type(self.settings) != Download: self.settings: Download = Download()
		return self.settings

	@property
	def dropdown(self):
		self._layout_type = dcc.Dropdown
		if type(self.settings) != Dropdown: self.settings: Dropdown = Dropdown()
		return self.settings

	@property
	def geolocation(self):
		self._layout_type = dcc.Geolocation
		if type(self.settings) != Geolocation: self.settings: Geolocation = Geolocation()
		return self.settings

	@property
	def graph(self):
		self._layout_type = dcc.Graph
		if type(self.settings) != Graph: self.settings: Graph = Graph()
		return self.settings

	@property
	def input(self):
		self._layout_type = dcc.Input
		if type(self.settings) != Input: self.settings: Input = Input()
		return self.settings

	@property
	def interval(self):
		self._layout_type = dcc.Interval
		if type(self.settings) != Interval: self.settings: Interval = Interval()
		return self.settings

	@property
	def link(self):
		self._layout_type = dcc.Link
		if type(self.settings) != Link: self.settings: Link = Link()
		return self.settings

	@property
	def loading(self):
		self._layout_type = dcc.Loading
		if type(self.settings) != Loading: self.settings: Loading = Loading()
		return self.settings

	@property
	def location(self):
		self._layout_type = dcc.Location
		if type(self.settings) != Location: self.settings: Location = Location()
		return self.settings

	@property
	def logoutbutton(self):
		self._layout_type = dcc.LogoutButton
		if type(self.settings) != LogoutButton: self.settings: LogoutButton = LogoutButton()
		return self.settings

	@property
	def markdown(self):
		self._layout_type = dcc.Markdown
		if type(self.settings) != Markdown: self.settings: Markdown = Markdown()
		return self.settings

	@property
	def radioitems(self):
		self._layout_type = dcc.RadioItems
		if type(self.settings) != RadioItems: self.settings: RadioItems = RadioItems()
		return self.settings

	@property
	def tooltip(self):
		self._layout_type = dcc.Tooltip
		if type(self.settings) != Tooltip: self.settings: Tooltip = Tooltip()
		return self.settings

	@property
	def rangeslider(self):
		self._layout_type = dcc.RangeSlider
		if type(self.settings) != RangeSlider: self.settings: RangeSlider = RangeSlider()
		return self.settings

	@property
	def slider(self):
		self._layout_type = dcc.Slider
		if type(self.settings) != Slider: self.settings: Slider = Slider()
		return self.settings

	@property
	def store(self):
		self._layout_type = dcc.Store
		if type(self.settings) != Store: self.settings: Store = Store()
		return self.settings

	@property
	def tab(self):
		self._layout_type = dcc.Tab
		if type(self.settings) != Tab: self.settings: Tab = Tab()
		return self.settings

	@property
	def tabs(self):
		self._layout_type = dcc.Tabs
		if type(self.settings) != Tabs: self.settings: Tabs = Tabs()
		return self.settings

	@property
	def textarea(self):
		self._layout_type = dcc.Textarea
		if type(self.settings) != Textarea: self.settings: Textarea = Textarea()
		return self.settings

	@property
	def upload(self):
		self._layout_type = dcc.Upload
		if type(self.settings) != Upload: self.settings: Upload = Upload()
		return self.settings