from __future__ import annotations
from pydantic.v1 import BaseModel
from .plotly_mappings import Settings
from .mapping_base import HtmlBase
from typing import Any
from collections import UserList
from dash import dcc
from random import randint

import dash_daq


class BooleanSwitch(Settings):
	id: Any = None
	on: Any = None
	color: Any = None
	vertical: Any = None
	disabled: Any = None
	theme: Any = None
	label: Any = None
	labelPosition: Any = None
	className: Any = None
	style: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class ColorPicker(Settings):
	id: Any = None
	value: Any = None
	disabled: Any = None
	size: Any = None
	theme: Any = None
	label: Any = None
	labelPosition: Any = None
	className: Any = None
	style: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class DarkThemeProvider(Settings):
	children: Any = None
	theme: Any = None

class Gauge(Settings):
	id: Any = None
	value: Any = None
	size: Any = None
	min: Any = None
	max: Any = None
	base: Any = None
	logarithmic: Any = None
	showCurrentValue: Any = None
	units: Any = None
	theme: Any = None
	label: Any = None
	labelPosition: Any = None
	scale: Any = None
	color: Any = None
	className: Any = None
	style: Any = None

class GraduatedBar(Settings):
	id: Any = None
	value: Any = None
	color: Any = None
	size: Any = None
	vertical: Any = None
	min: Any = None
	max: Any = None
	step: Any = None
	showCurrentValue: Any = None
	theme: Any = None
	label: Any = None
	labelPosition: Any = None
	className: Any = None
	style: Any = None

class Indicator(Settings):
	id: Any = None
	value: Any = None
	color: Any = None
	size: Any = None
	width: Any = None
	height: Any = None
	theme: Any = None
	label: Any = None
	labelPosition: Any = None
	className: Any = None
	style: Any = None

class Joystick(Settings):
	id: Any = None
	disabled: Any = None
	angle: Any = None
	force: Any = None
	size: Any = None
	theme: Any = None
	label: Any = None
	labelPosition: Any = None
	className: Any = None
	style: Any = None

class Knob(Settings):
	id: Any = None
	value: Any = None
	color: Any = None
	size: Any = None
	min: Any = None
	max: Any = None
	disabled: Any = None
	theme: Any = None
	label: Any = None
	labelPosition: Any = None
	scale: Any = None
	className: Any = None
	style: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class LEDDisplay(Settings):
	id: Any = None
	value: Any = None
	color: Any = None
	backgroundColor: Any = None
	size: Any = None
	theme: Any = None
	label: Any = None
	labelPosition: Any = None
	className: Any = None
	style: Any = None

class NumericInput(Settings):
	id: Any = None
	value: Any = None
	size: Any = None
	min: Any = None
	max: Any = None
	disabled: Any = None
	theme: Any = None
	label: Any = None
	labelPosition: Any = None
	className: Any = None
	style: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class PowerButton(Settings):
	id: Any = None
	on: Any = None
	color: Any = None
	size: Any = None
	disabled: Any = None
	theme: Any = None
	label: Any = None
	labelPosition: Any = None
	className: Any = None
	style: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class PrecisionInput(Settings):
	id: Any = None
	value: Any = None
	size: Any = None
	min: Any = None
	max: Any = None
	precision: Any = None
	disabled: Any = None
	theme: Any = None
	label: Any = None
	labelPosition: Any = None
	className: Any = None
	style: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class Slider(Settings):
	id: Any = None
	marks: Any = None
	color: Any = None
	value: Any = None
	className: Any = None
	labelPosition: Any = None
	disabled: Any = None
	dots: Any = None
	included: Any = None
	min: Any = None
	max: Any = None
	step: Any = None
	vertical: Any = None
	size: Any = None
	targets: Any = None
	theme: Any = None
	handleLabel: Any = None
	updatemode: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class StopButton(Settings):
	children: Any = None
	id: Any = None
	size: Any = None
	buttonText: Any = None
	n_clicks: Any = None
	disabled: Any = None
	theme: Any = None
	label: Any = None
	labelPosition: Any = None
	className: Any = None
	style: Any = None

class Tank(Settings):
	id: Any = None
	value: Any = None
	height: Any = None
	width: Any = None
	color: Any = None
	min: Any = None
	max: Any = None
	base: Any = None
	logarithmic: Any = None
	showCurrentValue: Any = None
	units: Any = None
	label: Any = None
	labelPosition: Any = None
	scale: Any = None
	className: Any = None
	style: Any = None

class Thermometer(Settings):
	id: Any = None
	value: Any = None
	height: Any = None
	width: Any = None
	color: Any = None
	min: Any = None
	max: Any = None
	base: Any = None
	logarithmic: Any = None
	showCurrentValue: Any = None
	units: Any = None
	theme: Any = None
	label: Any = None
	labelPosition: Any = None
	scale: Any = None
	className: Any = None
	style: Any = None

class ToggleSwitch(Settings):
	id: Any = None
	value: Any = None
	size: Any = None
	color: Any = None
	vertical: Any = None
	disabled: Any = None
	theme: Any = None
	label: Any = None
	labelPosition: Any = None
	className: Any = None
	style: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None

class ToggleSwitch(Settings):
	id: Any = None
	value: Any = None
	size: Any = None
	color: Any = None
	vertical: Any = None
	disabled: Any = None
	theme: Any = None
	label: Any = None
	labelPosition: Any = None
	className: Any = None
	style: Any = None
	persistence: Any = None
	persisted_props: Any = None
	persistence_type: Any = None


class DaqComponent(HtmlBase):

	def __init__(self, parent=None):
		super().__init__()
		self.parent = parent

	@property
	def booleanswitch(self):
		self._layout_type = dash_daq.BooleanSwitch
		if type(self.settings) != BooleanSwitch: self.settings: BooleanSwitch = BooleanSwitch()
		return self.settings

	@property
	def colorpicker(self):
		self._layout_type = dash_daq.ColorPicker
		if type(self.settings) != ColorPicker: self.settings: ColorPicker = ColorPicker()
		return self.settings

	@property
	def darkthemeprovider(self):
		self._layout_type = dash_daq.DarkThemeProvider
		if type(self.settings) != DarkThemeProvider: self.settings: DarkThemeProvider = DarkThemeProvider()
		return self.settings

	@property
	def gauge(self):
		self._layout_type = dash_daq.Gauge
		if type(self.settings) != Gauge: self.settings: Gauge = Gauge()
		return self.settings

	@property
	def graduatedbar(self):
		self._layout_type = dash_daq.GraduatedBar
		if type(self.settings) != GraduatedBar: self.settings: GraduatedBar = GraduatedBar()
		return self.settings

	@property
	def indicator(self):
		self._layout_type = dash_daq.Indicator
		if type(self.settings) != Indicator: self.settings: Indicator = Indicator()
		return self.settings

	@property
	def joystick(self):
		self._layout_type = dash_daq.Joystick
		if type(self.settings) != Joystick: self.settings: Joystick = Joystick()
		return self.settings

	@property
	def knob(self):
		self._layout_type = dash_daq.Knob
		if type(self.settings) != Knob: self.settings: Knob = Knob()
		return self.settings

	@property
	def leddisplay(self):
		self._layout_type = dash_daq.LEDDisplay
		if type(self.settings) != LEDDisplay: self.settings: LEDDisplay = LEDDisplay()
		return self.settings

	@property
	def numericinput(self):
		self._layout_type = dash_daq.NumericInput
		if type(self.settings) != NumericInput: self.settings: NumericInput = NumericInput()
		return self.settings

	@property
	def powerbutton(self):
		self._layout_type = dash_daq.PowerButton
		if type(self.settings) != PowerButton: self.settings: PowerButton = PowerButton()
		return self.settings

	@property
	def precisioninput(self):
		self._layout_type = dash_daq.PrecisionInput
		if type(self.settings) != PrecisionInput: self.settings: PrecisionInput = PrecisionInput()
		return self.settings

	@property
	def slider(self):
		self._layout_type = dash_daq.Slider
		if type(self.settings) != Slider: self.settings: Slider = Slider()
		return self.settings

	@property
	def stopbutton(self):
		self._layout_type = dash_daq.StopButton
		if type(self.settings) != StopButton: self.settings: StopButton = StopButton()
		return self.settings

	@property
	def tank(self):
		self._layout_type = dash_daq.Tank
		if type(self.settings) != Tank: self.settings: Tank = Tank()
		return self.settings

	@property
	def thermometer(self):
		self._layout_type = dash_daq.Thermometer
		if type(self.settings) != Thermometer: self.settings: Thermometer = Thermometer()
		return self.settings

	@property
	def toggleswitch(self):
		self._layout_type = dash_daq.ToggleSwitch
		if type(self.settings) != ToggleSwitch: self.settings: ToggleSwitch = ToggleSwitch()
		return self.settings

	@property
	def toggleswitch(self):
		self._layout_type = dash_daq.ToggleSwitch
		if type(self.settings) != ToggleSwitch: self.settings: ToggleSwitch = ToggleSwitch()
		return self.settings
