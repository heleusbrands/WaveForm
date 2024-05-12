import plotly.graph_objects as go
import pandas as pd
import numpy as np
from audio_modules.extraction.extract_configs import *
from pydantic.v1.dataclasses import dataclass
from pydantic.v1 import BaseModel
from typing import Union, Any
from array import array

class Settings(BaseModel):
	class Config:
		arbitrary_types_allowed = True
		allow_mutations = True
		extra = 'allow'
		orm_mode = True
		underscore_attrs_are_private = True
		exclude_none = True
		

class Font(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	colorsrc: Any = None
	family: Any = None
	familysrc: Any = None
	size: Any = None
	sizesrc: Any = None


class Hoverlabel(Settings):
	arg: Any = None
	align: Any = None
	alignsrc: Any = None
	bgcolor: Union[str, np.ndarray] = None
	bgcolorsrc: Any = None
	bordercolor: Union[str, np.ndarray] = None
	bordercolorsrc: Any = None
	font: Font = None
	namelength: Any = None
	namelengthsrc: Any = None
	split: Any = None


class Insidetextfont(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	colorsrc: Any = None
	family: Any = None
	familysrc: Any = None
	size: Any = None
	sizesrc: Any = None


class Legendgrouptitle(Settings):
	arg: Any = None
	font: Font = None
	text: Any = None


class Tickfont(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	family: Any = None
	size: Any = None


class Project(Settings):
	arg: Any = None
	x: Any = None
	y: Any = None
	z: Any = None


class X(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	end: Any = None
	highlight: Any = None
	highlightcolor: Union[str, np.ndarray] = None
	highlightwidth: Any = None
	project: Project = None
	show: Any = None
	size: Any = None
	start: Any = None
	usecolormap: Any = None
	width: Any = None


class Y(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	end: Any = None
	highlight: Any = None
	highlightcolor: Union[str, np.ndarray] = None
	highlightwidth: Any = None
	project: Project = None
	show: Any = None
	size: Any = None
	start: Any = None
	usecolormap: Any = None
	width: Any = None


class Pad(Settings):
	arg: Any = None
	b: Any = None
	l: Any = None
	r: Any = None
	t: Any = None


class Title(Settings):
	arg: Any = None
	font: Font = None
	pad: Pad = None
	text: Any = None
	x: Any = None
	xanchor: Any = None
	xref: Any = None
	y: Any = None
	yanchor: Any = None
	yref: Any = None


class ColorBar(Settings):
	arg: Any = None
	bgcolor: Union[str, np.ndarray] = None
	bordercolor: Union[str, np.ndarray] = None
	borderwidth: Any = None
	dtick: Any = None
	exponentformat: Any = None
	len: Any = None
	lenmode: Any = None
	minexponent: Any = None
	nticks: Any = None
	orientation: Any = None
	outlinecolor: Union[str, np.ndarray] = None
	outlinewidth: Any = None
	separatethousands: Any = None
	showexponent: Any = None
	showticklabels: Any = None
	showtickprefix: Any = None
	showticksuffix: Any = None
	thickness: Any = None
	thicknessmode: Any = None
	tick0: Any = None
	tickangle: Any = None
	tickcolor: Union[str, np.ndarray] = None
	tickfont: Tickfont = None
	tickformat: Any = None
	tickformatstops: Any = None
	tickformatstopdefaults: Any = None
	ticklabeloverflow: Any = None
	ticklabelposition: Any = None
	ticklabelstep: Any = None
	ticklen: Any = None
	tickmode: Any = None
	tickprefix: Any = None
	ticks: Any = None
	ticksuffix: Any = None
	ticktext: Any = None
	ticktextsrc: Any = None
	tickvals: Any = None
	tickvalssrc: Any = None
	tickwidth: Any = None
	title: Title = None
	titlefont: Any = None
	titleside: Any = None
	x: Any = None
	xanchor: Any = None
	xpad: Any = None
	y: Any = None
	yanchor: Any = None
	ypad: Any = None


class Colorscale(Settings):
	arg: Any = None
	cmax: Any = None
	cmin: Any = None
	colorscale: Any = None
	label: Any = None
	name: str = None
	templateitemname: str = None


class Coloraxis(Settings):
	arg: Any = None
	autocolorscale: Any = None
	cauto: Any = None
	cmax: Any = None
	cmid: Any = None
	cmin: Any = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	reversescale: Any = None
	showscale: Any = None


class Circle(Settings):
	arg: Any = None
	radius: Any = None


class Line(Settings):
	arg: Any = None
	autocolorscale: Any = None
	cauto: Any = None
	cmax: Any = None
	cmid: Any = None
	cmin: Any = None
	color: Union[str, np.ndarray] = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	colorsrc: Any = None
	hovertemplate: Any = None
	reversescale: Any = None
	shape: Any = None
	showscale: Any = None


class Fill(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	colorsrc: Any = None


class Symbol(Settings):
	arg: Any = None
	icon: Any = None
	iconsize: Any = None
	placement: Any = None
	text: Any = None
	textfont: Any = None
	textposition: Any = None


class Layer(Settings):
	arg: Any = None
	below: Any = None
	circle: Circle = None
	color: Union[str, np.ndarray] = None
	coordinates: Any = None
	fill: Fill = Fill()
	line: Line = Line()
	maxzoom: Any = None
	minzoom: Any = None
	name: str = None
	opacity: float = None
	source: Any = None
	sourceattribution: Any = None
	sourcelayer: Any = None
	sourcetype: Any = None
	symbol: Symbol = Symbol()
	templateitemname: str = None
	type: Any = None
	visible: Any = None


class Shape(Settings):
	arg: Any = None
	editable: Any = None
	fillcolor: Union[str, np.ndarray] = None
	fillrule: Any = None
	layer: Layer = Layer()
	line: Line = Line()
	name: str = None
	opacity: float = None
	path: Any = None
	templateitemname: str = None
	type: Any = None
	visible: Any = None
	x0: Any = None
	x1: Any = None
	xanchor: Any = None
	xref: Any = None
	xsizemode: Any = None
	y0: Any = None
	y1: Any = None
	yanchor: Any = None
	yref: Any = None
	ysizemode: Any = None


class Gradient(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	colorsrc: Any = None
	type: Any = None
	typesrc: Any = None


class Marker(Settings):
	arg: Any = None
	angle: Any = None
	angleref: Any = None
	anglesrc: Any = None
	autocolorscale: Any = None
	cauto: Any = None
	cmax: Any = None
	cmid: Any = None
	cmin: Any = None
	color: Union[str, np.ndarray] = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	colorsrc: Any = None
	gradient: Gradient = Gradient()
	line: Line = Line()
	maxdisplayed: Any = None
	opacity: float = None
	opacitysrc: Any = None
	reversescale: Any = None
	showscale: Any = None
	size: Any = None
	sizemin: Any = None
	sizemode: Any = None
	sizeref: Any = None
	sizesrc: Any = None
	standoff: Any = None
	standoffsrc: Any = None
	symbol: Symbol = Symbol()
	symbolsrc: Any = None


class Outsidetextfont(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	colorsrc: Any = None
	family: Any = None
	familysrc: Any = None
	size: Any = None
	sizesrc: Any = None


class Textfont(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	colorsrc: Any = None
	family: Any = None
	familysrc: Any = None
	size: Any = None
	sizesrc: Any = None


class Selected(Settings):
	arg: Any = None
	marker: Marker = Marker()
	textfont: Textfont = Textfont()


class Stream(Settings):
	arg: Any = None
	maxpoints: Any = None
	token: Any = None


class Unselected(Settings):
	arg: Any = None
	marker: Marker = Marker()
	textfont: Textfont = Textfont()


class Minor(Settings):
	arg: Any = None
	dtick: Any = None
	gridcolor: Union[str, np.ndarray] = None
	griddash: Any = None
	gridwidth: Any = None
	nticks: Any = None
	showgrid: Any = None
	tick0: Any = None
	tickcolor: Union[str, np.ndarray] = None
	ticklen: Any = None
	tickmode: Any = None
	ticks: Any = None
	tickvals: Any = None
	tickvalssrc: Any = None
	tickwidth: Any = None


class Domain(Settings):
	arg: Any = None
	column: Any = None
	row: Any = None
	x: Any = None
	y: Any = None


class Rangeselector(Settings):
	arg: Any = None
	activecolor: Union[str, np.ndarray] = None
	bgcolor: Union[str, np.ndarray] = None
	bordercolor: Union[str, np.ndarray] = None
	borderwidth: Any = None
	buttons: Any = None
	buttondefaults: Any = None
	font: Font = None
	visible: Any = None
	x: Any = None
	xanchor: Any = None
	y: Any = None
	yanchor: Any = None


class Rangeslider(Settings):
	arg: Any = None
	autorange: Any = None
	bgcolor: Union[str, np.ndarray] = None
	bordercolor: Union[str, np.ndarray] = None
	borderwidth: Any = None
	range: Any = None
	thickness: Any = None
	visible: Any = None
	yaxis: Any = None


class XAxis(Settings):
	arg: Any = None
	anchor: Any = None
	automargin: Any = None
	autorange: Any = None
	autotypenumbers: Any = None
	calendar: Any = None
	categoryarray: Any = None
	categoryarraysrc: Any = None
	categoryorder: Any = None
	color: Union[str, np.ndarray] = None
	constrain: Any = None
	constraintoward: Any = None
	dividercolor: Union[str, np.ndarray] = None
	dividerwidth: Any = None
	domain: Domain = None
	dtick: Any = None
	exponentformat: Any = None
	fixedrange: Any = None
	gridcolor: Union[str, np.ndarray] = None
	griddash: Any = None
	gridwidth: Any = None
	hoverformat: Any = None
	layer: Layer = Layer()
	linecolor: Union[str, np.ndarray] = None
	linewidth: Any = None
	matches: Any = None
	minexponent: Any = None
	minor: Minor = None
	mirror: Any = None
	nticks: Any = None
	overlaying: Any = None
	position: Any = None
	range: Any = None
	rangebreaks: Any = None
	rangebreakdefaults: Any = None
	rangemode: Any = None
	rangeselector: Rangeselector = None
	rangeslider: Rangeslider = None
	scaleanchor: Any = None
	scaleratio: Any = None
	separatethousands: Any = None
	showdividers: Any = None
	showexponent: Any = None
	showgrid: Any = None
	showline: Any = None
	showspikes: Any = None
	showticklabels: Any = None
	showtickprefix: Any = None
	showticksuffix: Any = None
	side: Any = None
	spikecolor: Union[str, np.ndarray] = None
	spikedash: Any = None
	spikemode: Any = None
	spikesnap: Any = None
	spikethickness: Any = None
	tick0: Any = None
	tickangle: Any = None
	tickcolor: Union[str, np.ndarray] = None
	tickfont: Tickfont = None
	tickformat: Any = None
	tickformatstops: Any = None
	tickformatstopdefaults: Any = None
	ticklabelmode: Any = None
	ticklabeloverflow: Any = None
	ticklabelposition: Any = None
	ticklabelstep: Any = None
	ticklen: Any = None
	tickmode: Any = None
	tickprefix: Any = None
	ticks: Any = None
	tickson: Any = None
	ticksuffix: Any = None
	ticktext: Any = None
	ticktextsrc: Any = None
	tickvals: Any = None
	tickvalssrc: Any = None
	tickwidth: Any = None
	title: Title = None
	titlefont: Any = None
	type: Any = None
	uirevision: Any = None
	visible: Any = None
	zeroline: Any = None
	zerolinecolor: Union[str, np.ndarray] = None
	zerolinewidth: Any = None


class YAxis(Settings):
	arg: Any = None
	anchor: Any = None
	automargin: Any = None
	autorange: Any = None
	autoshift: Any = None
	autotypenumbers: Any = None
	calendar: Any = None
	categoryarray: Any = None
	categoryarraysrc: Any = None
	categoryorder: Any = None
	color: Union[str, np.ndarray] = None
	constrain: Any = None
	constraintoward: Any = None
	dividercolor: Union[str, np.ndarray] = None
	dividerwidth: Any = None
	domain: Domain = None
	dtick: Any = None
	exponentformat: Any = None
	fixedrange: Any = None
	gridcolor: Union[str, np.ndarray] = None
	griddash: Any = None
	gridwidth: Any = None
	hoverformat: Any = None
	layer: Layer = Layer()
	linecolor: Union[str, np.ndarray] = None
	linewidth: Any = None
	matches: Any = None
	minexponent: Any = None
	minor: Minor = None
	mirror: Any = None
	nticks: Any = None
	overlaying: Any = None
	position: Any = None
	range: Any = None
	rangebreaks: Any = None
	rangebreakdefaults: Any = None
	rangemode: Any = None
	scaleanchor: Any = None
	scaleratio: Any = None
	separatethousands: Any = None
	shift: Any = None
	showdividers: Any = None
	showexponent: Any = None
	showgrid: Any = None
	showline: Any = None
	showspikes: Any = None
	showticklabels: Any = None
	showtickprefix: Any = None
	showticksuffix: Any = None
	side: Any = None
	spikecolor: Union[str, np.ndarray] = None
	spikedash: Any = None
	spikemode: Any = None
	spikesnap: Any = None
	spikethickness: Any = None
	tick0: Any = None
	tickangle: Any = None
	tickcolor: Union[str, np.ndarray] = None
	tickfont: Tickfont = None
	tickformat: Any = None
	tickformatstops: Any = None
	tickformatstopdefaults: Any = None
	ticklabelmode: Any = None
	ticklabeloverflow: Any = None
	ticklabelposition: Any = None
	ticklabelstep: Any = None
	ticklen: Any = None
	tickmode: Any = None
	tickprefix: Any = None
	ticks: Any = None
	tickson: Any = None
	ticksuffix: Any = None
	ticktext: Any = None
	ticktextsrc: Any = None
	tickvals: Any = None
	tickvalssrc: Any = None
	tickwidth: Any = None
	title: Title = None
	titlefont: Any = None
	type: Any = None
	uirevision: Any = None
	visible: Any = None
	zeroline: Any = None
	zerolinecolor: Union[str, np.ndarray] = None
	zerolinewidth: Any = None


class Bar(Settings):
	arg: Any = None
	alignmentgroup: Any = None
	base: Any = None
	basesrc: Any = None
	cliponaxis: Any = None
	constraintext: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	dx: Any = None
	dy: Any = None
	error_x: Any = None
	error_y: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	insidetextanchor: Any = None
	insidetextfont: Insidetextfont = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	offset: Any = None
	offsetgroup: Any = None
	offsetsrc: Any = None
	opacity: float = None
	orientation: Any = None
	outsidetextfont: Outsidetextfont = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	text: Any = None
	textangle: Any = None
	textfont: Textfont = Textfont()
	textposition: Any = None
	textpositionsrc: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None
	width: Any = None
	widthsrc: Any = None
	x: Any = None
	x0: Any = None
	xaxis: XAxis = XAxis()
	xcalendar: Any = None
	xhoverformat: Any = None
	xperiod: Any = None
	xperiod0: Any = None
	xperiodalignment: Any = None
	xsrc: Any = None
	y: Any = None
	y0: Any = None
	yaxis: YAxis = YAxis()
	ycalendar: Any = None
	yhoverformat: Any = None
	yperiod: Any = None
	yperiod0: Any = None
	yperiodalignment: Any = None
	ysrc: Any = None


class Barpolar(Settings):
	arg: Any = None
	base: Any = None
	basesrc: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	dr: Any = None
	dtheta: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	offset: Any = None
	offsetsrc: Any = None
	opacity: float = None
	r: Any = None
	r0: Any = None
	rsrc: Any = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	subplot: Any = None
	text: Any = None
	textsrc: Any = None
	theta: Any = None
	theta0: Any = None
	thetasrc: Any = None
	thetaunit: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None
	width: Any = None
	widthsrc: Any = None


class Box(Settings):
	arg: Any = None
	alignmentgroup: Any = None
	boxmean: Any = None
	boxpoints: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	dx: Any = None
	dy: Any = None
	fillcolor: Union[str, np.ndarray] = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hoveron: Any = None
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	jitter: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	lowerfence: Any = None
	lowerfencesrc: Any = None
	marker: Marker = Marker()
	mean: Any = None
	meansrc: Any = None
	median: Any = None
	mediansrc: Any = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	notched: Any = None
	notchspan: Any = None
	notchspansrc: Any = None
	notchwidth: Any = None
	offsetgroup: Any = None
	opacity: float = None
	orientation: Any = None
	pointpos: Any = None
	q1: Any = None
	q1src: Any = None
	q3: Any = None
	q3src: Any = None
	quartilemethod: Any = None
	sd: Any = None
	sdsrc: Any = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	text: Any = None
	textsrc: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	upperfence: Any = None
	upperfencesrc: Any = None
	visible: Any = None
	whiskerwidth: Any = None
	width: Any = None
	x: Any = None
	x0: Any = None
	xaxis: XAxis = XAxis()
	xcalendar: Any = None
	xhoverformat: Any = None
	xperiod: Any = None
	xperiod0: Any = None
	xperiodalignment: Any = None
	xsrc: Any = None
	y: Any = None
	y0: Any = None
	yaxis: YAxis = YAxis()
	ycalendar: Any = None
	yhoverformat: Any = None
	yperiod: Any = None
	yperiod0: Any = None
	yperiodalignment: Any = None
	ysrc: Any = None


class Decreasing(Settings):
	arg: Any = None
	fillcolor: Union[str, np.ndarray] = None
	line: Line = Line()


class Increasing(Settings):
	arg: Any = None
	fillcolor: Union[str, np.ndarray] = None
	line: Line = Line()


class Candlestick(Settings):
	arg: Any = None
	close: Any = None
	closesrc: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	decreasing: Decreasing = None
	high: Any = None
	highsrc: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	increasing: Increasing = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	low: Any = None
	lowsrc: Any = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	open: Any = None
	opensrc: Any = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	text: Any = None
	textsrc: Any = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	whiskerwidth: Any = None
	x: Any = None
	xaxis: XAxis = XAxis()
	xcalendar: Any = None
	xhoverformat: Any = None
	xperiod: Any = None
	xperiod0: Any = None
	xperiodalignment: Any = None
	xsrc: Any = None
	yaxis: YAxis = YAxis()
	yhoverformat: Any = None


class Aaxis(Settings):
	arg: Any = None
	arraydtick: Any = None
	arraytick0: Any = None
	autorange: Any = None
	autotypenumbers: Any = None
	categoryarray: Any = None
	categoryarraysrc: Any = None
	categoryorder: Any = None
	cheatertype: Any = None
	color: Union[str, np.ndarray] = None
	dtick: Any = None
	endline: Any = None
	endlinecolor: Union[str, np.ndarray] = None
	endlinewidth: Any = None
	exponentformat: Any = None
	fixedrange: Any = None
	gridcolor: Union[str, np.ndarray] = None
	griddash: Any = None
	gridwidth: Any = None
	labelpadding: Any = None
	labelprefix: Any = None
	labelsuffix: Any = None
	linecolor: Union[str, np.ndarray] = None
	linewidth: Any = None
	minexponent: Any = None
	minorgridcolor: Union[str, np.ndarray] = None
	minorgridcount: Any = None
	minorgriddash: Any = None
	minorgridwidth: Any = None
	nticks: Any = None
	range: Any = None
	rangemode: Any = None
	separatethousands: Any = None
	showexponent: Any = None
	showgrid: Any = None
	showline: Any = None
	showticklabels: Any = None
	showtickprefix: Any = None
	showticksuffix: Any = None
	smoothing: Any = None
	startline: Any = None
	startlinecolor: Union[str, np.ndarray] = None
	startlinewidth: Any = None
	tick0: Any = None
	tickangle: Any = None
	tickfont: Tickfont = None
	tickformat: Any = None
	tickformatstops: Any = None
	tickformatstopdefaults: Any = None
	tickmode: Any = None
	tickprefix: Any = None
	ticksuffix: Any = None
	ticktext: Any = None
	ticktextsrc: Any = None
	tickvals: Any = None
	tickvalssrc: Any = None
	title: Title = None
	titlefont: Any = None
	titleoffset: Any = None
	type: Any = None


class Baxis(Settings):
	arg: Any = None
	arraydtick: Any = None
	arraytick0: Any = None
	autorange: Any = None
	autotypenumbers: Any = None
	categoryarray: Any = None
	categoryarraysrc: Any = None
	categoryorder: Any = None
	cheatertype: Any = None
	color: Union[str, np.ndarray] = None
	dtick: Any = None
	endline: Any = None
	endlinecolor: Union[str, np.ndarray] = None
	endlinewidth: Any = None
	exponentformat: Any = None
	fixedrange: Any = None
	gridcolor: Union[str, np.ndarray] = None
	griddash: Any = None
	gridwidth: Any = None
	labelpadding: Any = None
	labelprefix: Any = None
	labelsuffix: Any = None
	linecolor: Union[str, np.ndarray] = None
	linewidth: Any = None
	minexponent: Any = None
	minorgridcolor: Union[str, np.ndarray] = None
	minorgridcount: Any = None
	minorgriddash: Any = None
	minorgridwidth: Any = None
	nticks: Any = None
	range: Any = None
	rangemode: Any = None
	separatethousands: Any = None
	showexponent: Any = None
	showgrid: Any = None
	showline: Any = None
	showticklabels: Any = None
	showtickprefix: Any = None
	showticksuffix: Any = None
	smoothing: Any = None
	startline: Any = None
	startlinecolor: Union[str, np.ndarray] = None
	startlinewidth: Any = None
	tick0: Any = None
	tickangle: Any = None
	tickfont: Tickfont = None
	tickformat: Any = None
	tickformatstops: Any = None
	tickformatstopdefaults: Any = None
	tickmode: Any = None
	tickprefix: Any = None
	ticksuffix: Any = None
	ticktext: Any = None
	ticktextsrc: Any = None
	tickvals: Any = None
	tickvalssrc: Any = None
	title: Title = None
	titlefont: Any = None
	titleoffset: Any = None
	type: Any = None


class Carpet(Settings):
	arg: Any = None
	a: Any = None
	a0: Any = None
	aaxis: Aaxis = None
	asrc: Any = None
	b: Any = None
	b0: Any = None
	baxis: Baxis = None
	bsrc: Any = None
	carpet: Any = None
	cheaterslope: Any = None
	color: Union[str, np.ndarray] = None
	customdata: Any = None
	customdatasrc: Any = None
	da: Any = None
	db: Any = None
	font: Font = None
	ids: Any = None
	idssrc: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	stream: Stream = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	x: Any = None
	xaxis: XAxis = XAxis()
	xsrc: Any = None
	y: Any = None
	yaxis: YAxis = YAxis()
	ysrc: Any = None


class Z(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	end: Any = None
	highlight: Any = None
	highlightcolor: Union[str, np.ndarray] = None
	highlightwidth: Any = None
	project: Project = None
	show: Any = None
	size: Any = None
	start: Any = None
	usecolormap: Any = None
	width: Any = None


class Center(Settings):
	arg: Any = None
	x: Any = None
	y: Any = None
	z: Any = None


class Lataxis(Settings):
	arg: Any = None
	dtick: Any = None
	gridcolor: Union[str, np.ndarray] = None
	griddash: Any = None
	gridwidth: Any = None
	range: Any = None
	showgrid: Any = None
	tick0: Any = None


class Lonaxis(Settings):
	arg: Any = None
	dtick: Any = None
	gridcolor: Union[str, np.ndarray] = None
	griddash: Any = None
	gridwidth: Any = None
	range: Any = None
	showgrid: Any = None
	tick0: Any = None


class Rotation(Settings):
	arg: Any = None
	lat: Any = None
	lon: Any = None
	roll: Any = None


class Projection(Settings):
	arg: Any = None
	distance: Any = None
	parallels: Any = None
	rotation: Rotation = None
	scale: Any = None
	tilt: Any = None
	type: Any = None


class Geo(Settings):
	arg: Any = None
	bgcolor: Union[str, np.ndarray] = None
	center: Center = None
	coastlinecolor: Union[str, np.ndarray] = None
	coastlinewidth: Any = None
	countrycolor: Union[str, np.ndarray] = None
	countrywidth: Any = None
	domain: Domain = None
	fitbounds: Any = None
	framecolor: Union[str, np.ndarray] = None
	framewidth: Any = None
	lakecolor: Union[str, np.ndarray] = None
	landcolor: Union[str, np.ndarray] = None
	lataxis: Lataxis = None
	lonaxis: Lonaxis = None
	oceancolor: Union[str, np.ndarray] = None
	projection: Projection = None
	resolution: Any = None
	rivercolor: Union[str, np.ndarray] = None
	riverwidth: Any = None
	scope: Any = None
	showcoastlines: Any = None
	showcountries: Any = None
	showframe: Any = None
	showlakes: Any = None
	showland: Any = None
	showocean: Any = None
	showrivers: Any = None
	showsubunits: Any = None
	subunitcolor: Union[str, np.ndarray] = None
	subunitwidth: Any = None
	uirevision: Any = None
	visible: Any = None


class Choropleth(Settings):
	arg: Any = None
	autocolorscale: Any = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	customdata: Any = None
	customdatasrc: Any = None
	featureidkey: Any = None
	geo: Geo = None
	geojson: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	locationmode: Any = None
	locations: Any = None
	locationssrc: Any = None
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	reversescale: Any = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	showscale: Any = None
	stream: Stream = None
	text: Any = None
	textsrc: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None
	z: Any = None
	zauto: Any = None
	zmax: Any = None
	zmid: Any = None
	zmin: Any = None
	zsrc: Any = None


class Choroplethmapbox(Settings):
	arg: Any = None
	autocolorscale: Any = None
	below: Any = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	customdata: Any = None
	customdatasrc: Any = None
	featureidkey: Any = None
	geojson: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	locations: Any = None
	locationssrc: Any = None
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	reversescale: Any = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	showscale: Any = None
	stream: Stream = None
	subplot: Any = None
	text: Any = None
	textsrc: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None
	z: Any = None
	zauto: Any = None
	zmax: Any = None
	zmid: Any = None
	zmin: Any = None
	zsrc: Any = None


class Lighting(Settings):
	arg: Any = None
	ambient: Any = None
	diffuse: Any = None
	facenormalsepsilon: Any = None
	fresnel: Any = None
	roughness: Any = None
	specular: Any = None
	vertexnormalsepsilon: Any = None


class Lightposition(Settings):
	arg: Any = None
	x: Any = None
	y: Any = None
	z: Any = None


class Aspectratio(Settings):
	arg: Any = None
	x: Any = None
	y: Any = None
	z: Any = None


class Eye(Settings):
	arg: Any = None
	x: Any = None
	y: Any = None
	z: Any = None


class Up(Settings):
	arg: Any = None
	x: Any = None
	y: Any = None
	z: Any = None


class Camera(Settings):
	arg: Any = None
	center: Center = None
	eye: Eye = None
	projection: Projection = None
	up: Up = None


class ZAxis(Settings):
	arg: Any = None
	autorange: Any = None
	autotypenumbers: Any = None
	backgroundcolor: Union[str, np.ndarray] = None
	calendar: Any = None
	categoryarray: Any = None
	categoryarraysrc: Any = None
	categoryorder: Any = None
	color: Union[str, np.ndarray] = None
	dtick: Any = None
	exponentformat: Any = None
	gridcolor: Union[str, np.ndarray] = None
	gridwidth: Any = None
	hoverformat: Any = None
	linecolor: Union[str, np.ndarray] = None
	linewidth: Any = None
	minexponent: Any = None
	mirror: Any = None
	nticks: Any = None
	range: Any = None
	rangemode: Any = None
	separatethousands: Any = None
	showaxeslabels: Any = None
	showbackground: Any = None
	showexponent: Any = None
	showgrid: Any = None
	showline: Any = None
	showspikes: Any = None
	showticklabels: Any = None
	showtickprefix: Any = None
	showticksuffix: Any = None
	spikecolor: Union[str, np.ndarray] = None
	spikesides: Any = None
	spikethickness: Any = None
	tick0: Any = None
	tickangle: Any = None
	tickcolor: Union[str, np.ndarray] = None
	tickfont: Tickfont = None
	tickformat: Any = None
	tickformatstops: Any = None
	tickformatstopdefaults: Any = None
	ticklen: Any = None
	tickmode: Any = None
	tickprefix: Any = None
	ticks: Any = None
	ticksuffix: Any = None
	ticktext: Any = None
	ticktextsrc: Any = None
	tickvals: Any = None
	tickvalssrc: Any = None
	tickwidth: Any = None
	title: Title = None
	titlefont: Any = None
	type: Any = None
	visible: Any = None
	zeroline: Any = None
	zerolinecolor: Union[str, np.ndarray] = None
	zerolinewidth: Any = None


class Scene(Settings):
	arg: Any = None
	annotations: Any = None
	annotationdefaults: Any = None
	aspectmode: Any = None
	aspectratio: Aspectratio = Aspectratio()
	bgcolor: Union[str, np.ndarray] = None
	camera: Camera = Camera()
	domain: Domain = None
	dragmode: Any = None
	hovermode: Any = None
	uirevision: Any = None
	xaxis: XAxis = XAxis()
	yaxis: YAxis = YAxis()
	zaxis: ZAxis = ZAxis()


class Cone(Settings):
	arg: Any = None
	anchor: Any = None
	autocolorscale: Any = None
	cauto: Any = None
	cmax: Any = None
	cmid: Any = None
	cmin: Any = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	customdata: Any = None
	customdatasrc: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	lighting: Lighting = None
	lightposition: Lightposition = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	reversescale: Any = None
	scene: Scene = None
	showlegend: Any = None
	showscale: Any = None
	sizemode: Any = None
	sizeref: Any = None
	stream: Stream = None
	text: Any = None
	textsrc: Any = None
	u: Any = None
	uhoverformat: Any = None
	uid: Any = None
	uirevision: Any = None
	usrc: Any = None
	v: Any = None
	vhoverformat: Any = None
	visible: Any = None
	vsrc: Any = None
	w: Any = None
	whoverformat: Any = None
	wsrc: Any = None
	x: Any = None
	xhoverformat: Any = None
	xsrc: Any = None
	y: Any = None
	yhoverformat: Any = None
	ysrc: Any = None
	z: Any = None
	zhoverformat: Any = None
	zsrc: Any = None


class Labelfont(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	family: Any = None
	size: Any = None


class Contours(Settings):
	arg: Any = None
	coloring: Any = None
	end: Any = None
	labelfont: Labelfont = None
	labelformat: Any = None
	operation: Any = None
	showlabels: Any = None
	showlines: Any = None
	size: Any = None
	start: Any = None
	type: Any = None
	value: Any = None


class Contour(Settings):
	arg: Any = None
	autocolorscale: Any = None
	autocontour: Any = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	connectgaps: Any = None
	contours: Contours = None
	customdata: Any = None
	customdatasrc: Any = None
	dx: Any = None
	dy: Any = None
	fillcolor: Union[str, np.ndarray] = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hoverongaps: Any = None
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	ncontours: Any = None
	opacity: float = None
	reversescale: Any = None
	showlegend: Any = None
	showscale: Any = None
	stream: Stream = None
	text: Any = None
	textfont: Textfont = Textfont()
	textsrc: Any = None
	texttemplate: Any = None
	transpose: Any = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	x: Any = None
	x0: Any = None
	xaxis: XAxis = XAxis()
	xcalendar: Any = None
	xhoverformat: Any = None
	xperiod: Any = None
	xperiod0: Any = None
	xperiodalignment: Any = None
	xsrc: Any = None
	xtype: Any = None
	y: Any = None
	y0: Any = None
	yaxis: YAxis = YAxis()
	ycalendar: Any = None
	yhoverformat: Any = None
	yperiod: Any = None
	yperiod0: Any = None
	yperiodalignment: Any = None
	ysrc: Any = None
	ytype: Any = None
	z: Any = None
	zauto: Any = None
	zhoverformat: Any = None
	zmax: Any = None
	zmid: Any = None
	zmin: Any = None
	zsrc: Any = None


class Contourcarpet(Settings):
	arg: Any = None
	a: Any = None
	a0: Any = None
	asrc: Any = None
	atype: Any = None
	autocolorscale: Any = None
	autocontour: Any = None
	b: Any = None
	b0: Any = None
	bsrc: Any = None
	btype: Any = None
	carpet: Carpet = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	contours: Contours = None
	customdata: Any = None
	customdatasrc: Any = None
	da: Any = None
	db: Any = None
	fillcolor: Union[str, np.ndarray] = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	ncontours: Any = None
	opacity: float = None
	reversescale: Any = None
	showlegend: Any = None
	showscale: Any = None
	stream: Stream = None
	text: Any = None
	textsrc: Any = None
	transpose: Any = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	xaxis: XAxis = XAxis()
	yaxis: YAxis = YAxis()
	z: Any = None
	zauto: Any = None
	zmax: Any = None
	zmid: Any = None
	zmin: Any = None
	zsrc: Any = None


class Densitymapbox(Settings):
	arg: Any = None
	autocolorscale: Any = None
	below: Any = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	customdata: Any = None
	customdatasrc: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	lat: Any = None
	latsrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	lon: Any = None
	lonsrc: Any = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	radius: Any = None
	radiussrc: Any = None
	reversescale: Any = None
	showlegend: Any = None
	showscale: Any = None
	stream: Stream = None
	subplot: Any = None
	text: Any = None
	textsrc: Any = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	z: Any = None
	zauto: Any = None
	zmax: Any = None
	zmid: Any = None
	zmin: Any = None
	zsrc: Any = None


class Activeselection(Settings):
	arg: Any = None
	fillcolor: Union[str, np.ndarray] = None
	opacity: float = None


class Activeshape(Settings):
	arg: Any = None
	fillcolor: Union[str, np.ndarray] = None
	opacity: float = None


class Grid(Settings):
	arg: Any = None
	columns: Any = None
	domain: Domain = None
	pattern: Any = None
	roworder: Any = None
	rows: Any = None
	subplots: Any = None
	xaxes: Any = None
	xgap: Any = None
	xside: Any = None
	yaxes: Any = None
	ygap: Any = None
	yside: Any = None


class Grouptitlefont(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	family: Any = None
	size: Any = None


class Legend(Settings):
	arg: Any = None
	bgcolor: Union[str, np.ndarray] = None
	bordercolor: Union[str, np.ndarray] = None
	borderwidth: Any = None
	entrywidth: Any = None
	entrywidthmode: Any = None
	font: Font = None
	groupclick: Any = None
	grouptitlefont: Grouptitlefont = None
	itemclick: Any = None
	itemdoubleclick: Any = None
	itemsizing: Any = None
	itemwidth: Any = None
	orientation: Any = None
	title: Title = None
	tracegroupgap: Any = None
	traceorder: Any = None
	uirevision: Any = None
	valign: Any = None
	x: Any = None
	xanchor: Any = None
	y: Any = None
	yanchor: Any = None


class Bounds(Settings):
	arg: Any = None
	east: Any = None
	north: Any = None
	south: Any = None
	west: Any = None


class Mapbox(Settings):
	arg: Any = None
	accesstoken: Any = None
	bearing: Any = None
	bounds: Bounds = None
	center: Center = None
	domain: Domain = None
	layers: Any = None
	layerdefaults: Any = None
	pitch: Any = None
	style: Any = None
	uirevision: Any = None
	zoom: Any = None


class Margin(Settings):
	arg: Any = None
	autoexpand: Any = None
	b: Any = None
	l: Any = None
	pad: Pad = None
	r: Any = None
	t: Any = None


class Modebar(Settings):
	arg: Any = None
	activecolor: Union[str, np.ndarray] = None
	add: Any = None
	addsrc: Any = None
	bgcolor: Union[str, np.ndarray] = None
	color: Union[str, np.ndarray] = None
	orientation: Any = None
	remove: Any = None
	removesrc: Any = None
	uirevision: Any = None


class Newselection(Settings):
	arg: Any = None
	line: Line = Line()
	mode: Any = None


class Newshape(Settings):
	arg: Any = None
	drawdirection: Any = None
	fillcolor: Union[str, np.ndarray] = None
	fillrule: Any = None
	layer: Layer = Layer()
	line: Line = Line()
	opacity: float = None


class AngularAxis(Settings):
	arg: Any = None
	autotypenumbers: Any = None
	categoryarray: Any = None
	categoryarraysrc: Any = None
	categoryorder: Any = None
	color: Union[str, np.ndarray] = None
	direction: Any = None
	dtick: Any = None
	exponentformat: Any = None
	gridcolor: Union[str, np.ndarray] = None
	griddash: Any = None
	gridwidth: Any = None
	hoverformat: Any = None
	layer: Layer = Layer()
	linecolor: Union[str, np.ndarray] = None
	linewidth: Any = None
	minexponent: Any = None
	nticks: Any = None
	period: Any = None
	rotation: Rotation = None
	separatethousands: Any = None
	showexponent: Any = None
	showgrid: Any = None
	showline: Any = None
	showticklabels: Any = None
	showtickprefix: Any = None
	showticksuffix: Any = None
	thetaunit: Any = None
	tick0: Any = None
	tickangle: Any = None
	tickcolor: Union[str, np.ndarray] = None
	tickfont: Tickfont = None
	tickformat: Any = None
	tickformatstops: Any = None
	tickformatstopdefaults: Any = None
	ticklabelstep: Any = None
	ticklen: Any = None
	tickmode: Any = None
	tickprefix: Any = None
	ticks: Any = None
	ticksuffix: Any = None
	ticktext: Any = None
	ticktextsrc: Any = None
	tickvals: Any = None
	tickvalssrc: Any = None
	tickwidth: Any = None
	type: Any = None
	uirevision: Any = None
	visible: Any = None


class RadialAxis(Settings):
	arg: Any = None
	angle: Any = None
	autorange: Any = None
	autotypenumbers: Any = None
	calendar: Any = None
	categoryarray: Any = None
	categoryarraysrc: Any = None
	categoryorder: Any = None
	color: Union[str, np.ndarray] = None
	dtick: Any = None
	exponentformat: Any = None
	gridcolor: Union[str, np.ndarray] = None
	griddash: Any = None
	gridwidth: Any = None
	hoverformat: Any = None
	layer: Layer = Layer()
	linecolor: Union[str, np.ndarray] = None
	linewidth: Any = None
	minexponent: Any = None
	nticks: Any = None
	range: Any = None
	rangemode: Any = None
	separatethousands: Any = None
	showexponent: Any = None
	showgrid: Any = None
	showline: Any = None
	showticklabels: Any = None
	showtickprefix: Any = None
	showticksuffix: Any = None
	side: Any = None
	tick0: Any = None
	tickangle: Any = None
	tickcolor: Union[str, np.ndarray] = None
	tickfont: Tickfont = None
	tickformat: Any = None
	tickformatstops: Any = None
	tickformatstopdefaults: Any = None
	ticklabelstep: Any = None
	ticklen: Any = None
	tickmode: Any = None
	tickprefix: Any = None
	ticks: Any = None
	ticksuffix: Any = None
	ticktext: Any = None
	ticktextsrc: Any = None
	tickvals: Any = None
	tickvalssrc: Any = None
	tickwidth: Any = None
	title: Title = None
	titlefont: Any = None
	type: Any = None
	uirevision: Any = None
	visible: Any = None


class Polar(Settings):
	arg: Any = None
	angularaxis: AngularAxis = None
	bargap: Any = None
	barmode: Any = None
	bgcolor: Union[str, np.ndarray] = None
	domain: Domain = None
	gridshape: Any = None
	hole: Any = None
	radialaxis: RadialAxis = None
	sector: Any = None
	uirevision: Any = None


class Imaginaryaxis(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	gridcolor: Union[str, np.ndarray] = None
	griddash: Any = None
	gridwidth: Any = None
	hoverformat: Any = None
	layer: Layer = Layer()
	linecolor: Union[str, np.ndarray] = None
	linewidth: Any = None
	showgrid: Any = None
	showline: Any = None
	showticklabels: Any = None
	showtickprefix: Any = None
	showticksuffix: Any = None
	tickcolor: Union[str, np.ndarray] = None
	tickfont: Tickfont = None
	tickformat: Any = None
	ticklen: Any = None
	tickprefix: Any = None
	ticks: Any = None
	ticksuffix: Any = None
	tickvals: Any = None
	tickvalssrc: Any = None
	tickwidth: Any = None
	visible: Any = None


class Realaxis(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	gridcolor: Union[str, np.ndarray] = None
	griddash: Any = None
	gridwidth: Any = None
	hoverformat: Any = None
	layer: Layer = Layer()
	linecolor: Union[str, np.ndarray] = None
	linewidth: Any = None
	showgrid: Any = None
	showline: Any = None
	showticklabels: Any = None
	showtickprefix: Any = None
	showticksuffix: Any = None
	side: Any = None
	tickangle: Any = None
	tickcolor: Union[str, np.ndarray] = None
	tickfont: Tickfont = None
	tickformat: Any = None
	ticklen: Any = None
	tickprefix: Any = None
	ticks: Any = None
	ticksuffix: Any = None
	tickvals: Any = None
	tickvalssrc: Any = None
	tickwidth: Any = None
	visible: Any = None


class Smith(Settings):
	arg: Any = None
	bgcolor: Union[str, np.ndarray] = None
	domain: Domain = None
	imaginaryaxis: Imaginaryaxis = None
	realaxis: Realaxis = None


class Data(Settings):
	arg: Any = None
	barpolar: Barpolar = None
	bar: Bar = None
	box: Box = None
	candlestick: Candlestick = None
	carpet: Carpet = None
	choroplethmapbox: Choroplethmapbox = None
	choropleth: Choropleth = None
	cone: Cone = None
	contourcarpet: Contourcarpet = None
	contour: Contour = None
	densitymapbox: Densitymapbox = None
	funnelarea: Any = None
	funnel: Any = None
	heatmapgl: Any = None
	heatmap: Any = None
	histogram2dcontour: Any = None
	histogram2d: Any = None
	histogram: Any = None
	icicle: Any = None
	image: Any = None
	indicator: Any = None
	isosurface: Any = None
	mesh3d: Any = None
	ohlc: Any = None
	parcats: Any = None
	parcoords: Any = None
	pie: Any = None
	pointcloud: Any = None
	sankey: Any = None
	scatter3d: Any = None
	scattercarpet: Any = None
	scattergeo: Any = None
	scattergl: Any = None
	scattermapbox: Any = None
	scatterpolargl: Any = None
	scatterpolar: Any = None
	scatter: Any = None
	scattersmith: Any = None
	scatterternary: Any = None
	splom: Any = None
	streamtube: Any = None
	sunburst: Any = None
	surface: Any = None
	table: Any = None
	treemap: Any = None
	violin: Any = None
	volume: Any = None
	waterfall: Any = None


class Caxis(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	dtick: Any = None
	exponentformat: Any = None
	gridcolor: Union[str, np.ndarray] = None
	griddash: Any = None
	gridwidth: Any = None
	hoverformat: Any = None
	layer: Layer = Layer()
	linecolor: Union[str, np.ndarray] = None
	linewidth: Any = None
	min: Any = None
	minexponent: Any = None
	nticks: Any = None
	separatethousands: Any = None
	showexponent: Any = None
	showgrid: Any = None
	showline: Any = None
	showticklabels: Any = None
	showtickprefix: Any = None
	showticksuffix: Any = None
	tick0: Any = None
	tickangle: Any = None
	tickcolor: Union[str, np.ndarray] = None
	tickfont: Tickfont = None
	tickformat: Any = None
	tickformatstops: Any = None
	tickformatstopdefaults: Any = None
	ticklabelstep: Any = None
	ticklen: Any = None
	tickmode: Any = None
	tickprefix: Any = None
	ticks: Any = None
	ticksuffix: Any = None
	ticktext: Any = None
	ticktextsrc: Any = None
	tickvals: Any = None
	tickvalssrc: Any = None
	tickwidth: Any = None
	title: Title = None
	titlefont: Any = None
	uirevision: Any = None


class Ternary(Settings):
	arg: Any = None
	aaxis: Aaxis = None
	baxis: Baxis = None
	bgcolor: Union[str, np.ndarray] = None
	caxis: Caxis = None
	domain: Domain = None
	sum: Any = None
	uirevision: Any = None


class Template(Settings):
	arg: Any = None
	data: Data = None
	layout: Any = None


class Transition(Settings):
	arg: Any = None
	duration: Any = None
	easing: Any = None
	ordering: Any = None


class Uniformtext(Settings):
	arg: Any = None
	minsize: Any = None
	mode: Any = None


class Layout(Settings):
	arg: Any = None
	activeselection: Activeselection = None
	activeshape: Activeshape = None
	annotations: Any = None
	annotationdefaults: Any = None
	autosize: Any = None
	autotypenumbers: Any = None
	bargap: Any = None
	bargroupgap: Any = None
	barmode: Any = None
	barnorm: Any = None
	boxgap: Any = None
	boxgroupgap: Any = None
	boxmode: Any = None
	calendar: Any = None
	clickmode: Any = None
	coloraxis: Coloraxis = None
	colorscale: Colorscale = Colorscale()
	colorway: Any = None
	computed: Any = None
	datarevision: Any = None
	dragmode: Any = None
	editrevision: Any = None
	extendfunnelareacolors: Any = None
	extendiciclecolors: Any = None
	extendpiecolors: Any = None
	extendsunburstcolors: Any = None
	extendtreemapcolors: Any = None
	font: Font = None
	funnelareacolorway: Any = None
	funnelgap: Any = None
	funnelgroupgap: Any = None
	funnelmode: Any = None
	geo: Geo = None
	grid: Grid = None
	height: Any = None
	hiddenlabels: Any = None
	hiddenlabelssrc: Any = None
	hidesources: Any = None
	hoverdistance: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovermode: Any = None
	iciclecolorway: Any = None
	images: Any = None
	imagedefaults: Any = None
	legend: Legend = None
	mapbox: Mapbox = None
	margin: Margin = Margin()
	meta: Any = None
	metasrc: Any = None
	minreducedheight: Any = None
	minreducedwidth: Any = None
	modebar: Modebar = None
	newselection: Newselection = None
	newshape: Newshape = None
	paper_bgcolor: Union[str, np.ndarray] = None
	piecolorway: Any = None
	plot_bgcolor: Union[str, np.ndarray] = None
	polar: Polar = None
	scattergap: Any = None
	scattermode: Any = None
	scene: Scene = None
	selectdirection: Any = None
	selectionrevision: Any = None
	selections: Any = None
	selectiondefaults: Any = None
	separators: Any = None
	shapes: Any = None
	shapedefaults: Any = None
	showlegend: Any = None
	sliders: Any = None
	sliderdefaults: Any = None
	smith: Smith = None
	spikedistance: Any = None
	sunburstcolorway: Any = None
	template: Template = None
	ternary: Ternary = None
	title: Title = None
	titlefont: Any = None
	transition: Transition = Transition()
	treemapcolorway: Any = None
	uirevision: Any = None
	uniformtext: Uniformtext = None
	updatemenus: Any = None
	updatemenudefaults: Any = None
	violingap: Any = None
	violingroupgap: Any = None
	violinmode: Any = None
	waterfallgap: Any = None
	waterfallgroupgap: Any = None
	waterfallmode: Any = None
	width: Any = None
	xaxis: XAxis = XAxis()
	yaxis: YAxis = YAxis()


class Figure(Settings):
	data: Data = False
	layout: Layout = None
	frames: Any = None
	skip_invalid: Any = None


class FigureWidget(Settings):
	data: Data = False
	layout: Layout = None
	frames: Any = None
	skip_invalid: Any = None


class Frame(Settings):
	arg: Any = None
	baseframe: Any = None
	data: Data = None
	group: Any = None
	layout: Layout = None
	name: str = None
	traces: Any = None


class Connector(Settings):
	arg: Any = None
	fillcolor: Union[str, np.ndarray] = None
	line: Line = Line()
	visible: Any = None


class Funnel(Settings):
	arg: Any = None
	alignmentgroup: Any = None
	cliponaxis: Any = None
	connector: Connector = None
	constraintext: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	dx: Any = None
	dy: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	insidetextanchor: Any = None
	insidetextfont: Insidetextfont = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	offset: Any = None
	offsetgroup: Any = None
	opacity: float = None
	orientation: Any = None
	outsidetextfont: Outsidetextfont = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	text: Any = None
	textangle: Any = None
	textfont: Textfont = Textfont()
	textinfo: Any = None
	textposition: Any = None
	textpositionsrc: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	width: Any = None
	x: Any = None
	x0: Any = None
	xaxis: XAxis = XAxis()
	xhoverformat: Any = None
	xperiod: Any = None
	xperiod0: Any = None
	xperiodalignment: Any = None
	xsrc: Any = None
	y: Any = None
	y0: Any = None
	yaxis: YAxis = YAxis()
	yhoverformat: Any = None
	yperiod: Any = None
	yperiod0: Any = None
	yperiodalignment: Any = None
	ysrc: Any = None


class Funnelarea(Settings):
	arg: Any = None
	aspectratio: Aspectratio = Aspectratio()
	baseratio: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	dlabel: Any = None
	domain: Domain = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	insidetextfont: Insidetextfont = None
	label0: Any = None
	labels: Any = None
	labelssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	scalegroup: Any = None
	showlegend: Any = None
	stream: Stream = None
	text: Any = None
	textfont: Textfont = Textfont()
	textinfo: Any = None
	textposition: Any = None
	textpositionsrc: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	title: Title = None
	uid: Any = None
	uirevision: Any = None
	values: Any = None
	valuessrc: Any = None
	visible: Any = None


class Heatmap(Settings):
	arg: Any = None
	autocolorscale: Any = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	connectgaps: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	dx: Any = None
	dy: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hoverongaps: Any = None
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	reversescale: Any = None
	showlegend: Any = None
	showscale: Any = None
	stream: Stream = None
	text: Any = None
	textfont: Textfont = Textfont()
	textsrc: Any = None
	texttemplate: Any = None
	transpose: Any = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	x: Any = None
	x0: Any = None
	xaxis: XAxis = XAxis()
	xcalendar: Any = None
	xgap: Any = None
	xhoverformat: Any = None
	xperiod: Any = None
	xperiod0: Any = None
	xperiodalignment: Any = None
	xsrc: Any = None
	xtype: Any = None
	y: Any = None
	y0: Any = None
	yaxis: YAxis = YAxis()
	ycalendar: Any = None
	ygap: Any = None
	yhoverformat: Any = None
	yperiod: Any = None
	yperiod0: Any = None
	yperiodalignment: Any = None
	ysrc: Any = None
	ytype: Any = None
	z: Any = None
	zauto: Any = None
	zhoverformat: Any = None
	zmax: Any = None
	zmid: Any = None
	zmin: Any = None
	zsmooth: Any = None
	zsrc: Any = None


class Heatmapgl(Settings):
	arg: Any = None
	autocolorscale: Any = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	customdata: Any = None
	customdatasrc: Any = None
	dx: Any = None
	dy: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	ids: Any = None
	idssrc: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	reversescale: Any = None
	showscale: Any = None
	stream: Stream = None
	text: Any = None
	textsrc: Any = None
	transpose: Any = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	x: Any = None
	x0: Any = None
	xaxis: XAxis = XAxis()
	xsrc: Any = None
	xtype: Any = None
	y: Any = None
	y0: Any = None
	yaxis: YAxis = YAxis()
	ysrc: Any = None
	ytype: Any = None
	z: Any = None
	zauto: Any = None
	zmax: Any = None
	zmid: Any = None
	zmin: Any = None
	zsmooth: Any = None
	zsrc: Any = None


class Cumulative(Settings):
	arg: Any = None
	currentbin: Any = None
	direction: Any = None
	enabled: Any = None


class XBins(Settings):
	arg: Any = None
	end: Any = None
	size: Any = None
	start: Any = None


class YBins(Settings):
	arg: Any = None
	end: Any = None
	size: Any = None
	start: Any = None


class Histogram(Settings):
	arg: Any = None
	alignmentgroup: Any = None
	autobinx: Any = None
	autobiny: Any = None
	bingroup: Any = None
	cliponaxis: Any = None
	constraintext: Any = None
	cumulative: Cumulative = None
	customdata: Any = None
	customdatasrc: Any = None
	error_x: Any = None
	error_y: Any = None
	histfunc: Any = None
	histnorm: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	insidetextanchor: Any = None
	insidetextfont: Insidetextfont = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	nbinsx: Any = None
	nbinsy: Any = None
	offsetgroup: Any = None
	opacity: float = None
	orientation: Any = None
	outsidetextfont: Outsidetextfont = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	text: Any = None
	textangle: Any = None
	textfont: Textfont = Textfont()
	textposition: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None
	x: Any = None
	xaxis: XAxis = XAxis()
	xbins: XBins = None
	xcalendar: Any = None
	xhoverformat: Any = None
	xsrc: Any = None
	y: Any = None
	yaxis: YAxis = YAxis()
	ybins: YBins = None
	ycalendar: Any = None
	yhoverformat: Any = None
	ysrc: Any = None


class Histogram2d(Settings):
	arg: Any = None
	autobinx: Any = None
	autobiny: Any = None
	autocolorscale: Any = None
	bingroup: Any = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	customdata: Any = None
	customdatasrc: Any = None
	histfunc: Any = None
	histnorm: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	nbinsx: Any = None
	nbinsy: Any = None
	opacity: float = None
	reversescale: Any = None
	showlegend: Any = None
	showscale: Any = None
	stream: Stream = None
	textfont: Textfont = Textfont()
	texttemplate: Any = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	x: Any = None
	xaxis: XAxis = XAxis()
	xbingroup: Any = None
	xbins: XBins = None
	xcalendar: Any = None
	xgap: Any = None
	xhoverformat: Any = None
	xsrc: Any = None
	y: Any = None
	yaxis: YAxis = YAxis()
	ybingroup: Any = None
	ybins: YBins = None
	ycalendar: Any = None
	ygap: Any = None
	yhoverformat: Any = None
	ysrc: Any = None
	z: Any = None
	zauto: Any = None
	zhoverformat: Any = None
	zmax: Any = None
	zmid: Any = None
	zmin: Any = None
	zsmooth: Any = None
	zsrc: Any = None


class Histogram2dContour(Settings):
	arg: Any = None
	autobinx: Any = None
	autobiny: Any = None
	autocolorscale: Any = None
	autocontour: Any = None
	bingroup: Any = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	contours: Contours = None
	customdata: Any = None
	customdatasrc: Any = None
	histfunc: Any = None
	histnorm: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	nbinsx: Any = None
	nbinsy: Any = None
	ncontours: Any = None
	opacity: float = None
	reversescale: Any = None
	showlegend: Any = None
	showscale: Any = None
	stream: Stream = None
	textfont: Textfont = Textfont()
	texttemplate: Any = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	x: Any = None
	xaxis: XAxis = XAxis()
	xbingroup: Any = None
	xbins: XBins = None
	xcalendar: Any = None
	xhoverformat: Any = None
	xsrc: Any = None
	y: Any = None
	yaxis: YAxis = YAxis()
	ybingroup: Any = None
	ybins: YBins = None
	ycalendar: Any = None
	yhoverformat: Any = None
	ysrc: Any = None
	z: Any = None
	zauto: Any = None
	zhoverformat: Any = None
	zmax: Any = None
	zmid: Any = None
	zmin: Any = None
	zsrc: Any = None


class Leaf(Settings):
	arg: Any = None
	opacity: float = None


class Pathbar(Settings):
	arg: Any = None
	edgeshape: Any = None
	side: Any = None
	textfont: Textfont = Textfont()
	thickness: Any = None
	visible: Any = None


class Root(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None


class Tiling(Settings):
	arg: Any = None
	flip: Any = None
	packing: Any = None
	pad: Pad = None
	squarifyratio: Any = None


class Icicle(Settings):
	arg: Any = None
	branchvalues: Any = None
	count: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	domain: Domain = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	insidetextfont: Insidetextfont = None
	labels: Any = None
	labelssrc: Any = None
	leaf: Leaf = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	level: Any = None
	marker: Marker = Marker()
	maxdepth: Any = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	outsidetextfont: Outsidetextfont = None
	parents: Any = None
	parentssrc: Any = None
	pathbar: Pathbar = None
	root: Root = None
	sort: Any = None
	stream: Stream = None
	text: Any = None
	textfont: Textfont = Textfont()
	textinfo: Any = None
	textposition: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	tiling: Tiling = None
	uid: Any = None
	uirevision: Any = None
	values: Any = None
	valuessrc: Any = None
	visible: Any = None


class Image(Settings):
	arg: Any = None
	colormodel: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	dx: Any = None
	dy: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	source: Any = None
	stream: Stream = None
	text: Any = None
	textsrc: Any = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	x0: Any = None
	xaxis: XAxis = XAxis()
	y0: Any = None
	yaxis: YAxis = YAxis()
	z: Any = None
	zmax: Any = None
	zmin: Any = None
	zsmooth: Any = None
	zsrc: Any = None


class Delta(Settings):
	arg: Any = None
	decreasing: Decreasing = None
	font: Font = None
	increasing: Increasing = None
	position: Any = None
	prefix: Any = None
	reference: Any = None
	relative: Any = None
	suffix: Any = None
	valueformat: Any = None


class Axis(Settings):
	arg: Any = None
	dtick: Any = None
	exponentformat: Any = None
	minexponent: Any = None
	nticks: Any = None
	range: Any = None
	separatethousands: Any = None
	showexponent: Any = None
	showticklabels: Any = None
	showtickprefix: Any = None
	showticksuffix: Any = None
	tick0: Any = None
	tickangle: Any = None
	tickcolor: Union[str, np.ndarray] = None
	tickfont: Tickfont = None
	tickformat: Any = None
	tickformatstops: Any = None
	tickformatstopdefaults: Any = None
	ticklabelstep: Any = None
	ticklen: Any = None
	tickmode: Any = None
	tickprefix: Any = None
	ticks: Any = None
	ticksuffix: Any = None
	ticktext: Any = None
	ticktextsrc: Any = None
	tickvals: Any = None
	tickvalssrc: Any = None
	tickwidth: Any = None
	visible: Any = None


class Threshold(Settings):
	arg: Any = None
	line: Line = Line()
	thickness: Any = None
	value: Any = None


class Gauge(Settings):
	arg: Any = None
	axis: Axis = None
	bar: Bar = None
	bgcolor: Union[str, np.ndarray] = None
	bordercolor: Union[str, np.ndarray] = None
	borderwidth: Any = None
	shape: Shape = None
	steps: Any = None
	stepdefaults: Any = None
	threshold: Threshold = None


class Number(Settings):
	arg: Any = None
	font: Font = None
	prefix: Any = None
	suffix: Any = None
	valueformat: Any = None


class Indicator(Settings):
	arg: Any = None
	align: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	delta: Delta = None
	domain: Domain = None
	gauge: Gauge = None
	ids: Any = None
	idssrc: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	meta: Any = None
	metasrc: Any = None
	mode: Any = None
	name: str = None
	number: Number = None
	stream: Stream = None
	title: Title = None
	uid: Any = None
	uirevision: Any = None
	value: Any = None
	visible: Any = None


class Surface(Settings):
	arg: Any = None
	autocolorscale: Any = None
	cauto: Any = None
	cmax: Any = None
	cmid: Any = None
	cmin: Any = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	connectgaps: Any = None
	contours: Contours = None
	customdata: Any = None
	customdatasrc: Any = None
	hidesurface: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	lighting: Lighting = None
	lightposition: Lightposition = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	opacityscale: Any = None
	reversescale: Any = None
	scene: Scene = None
	showlegend: Any = None
	showscale: Any = None
	stream: Stream = None
	surfacecolor: Union[str, np.ndarray] = None
	surfacecolorsrc: Any = None
	text: Any = None
	textsrc: Any = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	x: Any = None
	xcalendar: Any = None
	xhoverformat: Any = None
	xsrc: Any = None
	y: Any = None
	ycalendar: Any = None
	yhoverformat: Any = None
	ysrc: Any = None
	z: Any = None
	zcalendar: Any = None
	zhoverformat: Any = None
	zsrc: Any = None


class Caps(Settings):
	arg: Any = None
	x: Any = None
	y: Any = None
	z: Any = None


class Slices(Settings):
	arg: Any = None
	x: Any = None
	y: Any = None
	z: Any = None


class Spaceframe(Settings):
	arg: Any = None
	fill: Fill = Fill()
	show: Any = None


class Isosurface(Settings):
	arg: Any = None
	autocolorscale: Any = None
	caps: Caps = None
	cauto: Any = None
	cmax: Any = None
	cmid: Any = None
	cmin: Any = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	contour: Contour = None
	customdata: Any = None
	customdatasrc: Any = None
	flatshading: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	isomax: Any = None
	isomin: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	lighting: Lighting = None
	lightposition: Lightposition = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	reversescale: Any = None
	scene: Scene = None
	showlegend: Any = None
	showscale: Any = None
	slices: Slices = None
	spaceframe: Spaceframe = None
	stream: Stream = None
	surface: Surface = None
	text: Any = None
	textsrc: Any = None
	uid: Any = None
	uirevision: Any = None
	value: Any = None
	valuehoverformat: Any = None
	valuesrc: Any = None
	visible: Any = None
	x: Any = None
	xhoverformat: Any = None
	xsrc: Any = None
	y: Any = None
	yhoverformat: Any = None
	ysrc: Any = None
	z: Any = None
	zhoverformat: Any = None
	zsrc: Any = None


class Mesh3d(Settings):
	arg: Any = None
	alphahull: Any = None
	autocolorscale: Any = None
	cauto: Any = None
	cmax: Any = None
	cmid: Any = None
	cmin: Any = None
	color: Union[str, np.ndarray] = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	contour: Contour = None
	customdata: Any = None
	customdatasrc: Any = None
	delaunayaxis: Any = None
	facecolor: Union[str, np.ndarray] = None
	facecolorsrc: Any = None
	flatshading: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	i: Any = None
	ids: Any = None
	idssrc: Any = None
	intensity: Any = None
	intensitymode: Any = None
	intensitysrc: Any = None
	isrc: Any = None
	j: Any = None
	jsrc: Any = None
	k: Any = None
	ksrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	lighting: Lighting = None
	lightposition: Lightposition = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	reversescale: Any = None
	scene: Scene = None
	showlegend: Any = None
	showscale: Any = None
	stream: Stream = None
	text: Any = None
	textsrc: Any = None
	uid: Any = None
	uirevision: Any = None
	vertexcolor: Union[str, np.ndarray] = None
	vertexcolorsrc: Any = None
	visible: Any = None
	x: Any = None
	xcalendar: Any = None
	xhoverformat: Any = None
	xsrc: Any = None
	y: Any = None
	ycalendar: Any = None
	yhoverformat: Any = None
	ysrc: Any = None
	z: Any = None
	zcalendar: Any = None
	zhoverformat: Any = None
	zsrc: Any = None


class Ohlc(Settings):
	arg: Any = None
	close: Any = None
	closesrc: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	decreasing: Decreasing = None
	high: Any = None
	highsrc: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	increasing: Increasing = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	low: Any = None
	lowsrc: Any = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	open: Any = None
	opensrc: Any = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	text: Any = None
	textsrc: Any = None
	tickwidth: Any = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	x: Any = None
	xaxis: XAxis = XAxis()
	xcalendar: Any = None
	xhoverformat: Any = None
	xperiod: Any = None
	xperiod0: Any = None
	xperiodalignment: Any = None
	xsrc: Any = None
	yaxis: YAxis = YAxis()
	yhoverformat: Any = None


class Parcats(Settings):
	arg: Any = None
	arrangement: Any = None
	bundlecolors: Any = None
	counts: Any = None
	countssrc: Any = None
	dimensions: Any = None
	dimensiondefaults: Any = None
	domain: Domain = None
	hoverinfo: Any = None
	hoveron: Any = None
	hovertemplate: Any = None
	labelfont: Labelfont = None
	legendgrouptitle: Legendgrouptitle = None
	legendwidth: Any = None
	line: Line = Line()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	sortpaths: Any = None
	stream: Stream = None
	tickfont: Tickfont = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None


class Rangefont(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	family: Any = None
	size: Any = None


class Parcoords(Settings):
	arg: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	dimensions: Any = None
	dimensiondefaults: Any = None
	domain: Domain = None
	ids: Any = None
	idssrc: Any = None
	labelangle: Any = None
	labelfont: Labelfont = None
	labelside: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	rangefont: Rangefont = None
	stream: Stream = None
	tickfont: Tickfont = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None


class Pie(Settings):
	arg: Any = None
	automargin: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	direction: Any = None
	dlabel: Any = None
	domain: Domain = None
	hole: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	insidetextfont: Insidetextfont = None
	insidetextorientation: Any = None
	label0: Any = None
	labels: Any = None
	labelssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	outsidetextfont: Outsidetextfont = None
	pull: Any = None
	pullsrc: Any = None
	rotation: Rotation = None
	scalegroup: Any = None
	showlegend: Any = None
	sort: Any = None
	stream: Stream = None
	text: Any = None
	textfont: Textfont = Textfont()
	textinfo: Any = None
	textposition: Any = None
	textpositionsrc: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	title: Title = None
	titlefont: Any = None
	titleposition: Any = None
	uid: Any = None
	uirevision: Any = None
	values: Any = None
	valuessrc: Any = None
	visible: Any = None


class Pointcloud(Settings):
	arg: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	ids: Any = None
	idssrc: Any = None
	indices: Any = None
	indicessrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	showlegend: Any = None
	stream: Stream = None
	text: Any = None
	textsrc: Any = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	x: Any = None
	xaxis: XAxis = XAxis()
	xbounds: Any = None
	xboundssrc: Any = None
	xsrc: Any = None
	xy: Any = None
	xysrc: Any = None
	y: Any = None
	yaxis: YAxis = YAxis()
	ybounds: Any = None
	yboundssrc: Any = None
	ysrc: Any = None


class Link(Settings):
	arg: Any = None
	arrowlen: Any = None
	color: Union[str, np.ndarray] = None
	colorscales: Any = None
	colorscaledefaults: Any = None
	colorsrc: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	hoverinfo: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	label: Any = None
	labelsrc: Any = None
	line: Line = Line()
	source: Any = None
	sourcesrc: Any = None
	target: Any = None
	targetsrc: Any = None
	value: Any = None
	valuesrc: Any = None


class Node(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	colorsrc: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	groups: Any = None
	hoverinfo: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	label: Any = None
	labelsrc: Any = None
	line: Line = Line()
	pad: Pad = None
	thickness: Any = None
	x: Any = None
	xsrc: Any = None
	y: Any = None
	ysrc: Any = None


class Sankey(Settings):
	arg: Any = None
	arrangement: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	domain: Domain = None
	hoverinfo: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	ids: Any = None
	idssrc: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	link: Link = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	node: Node = None
	orientation: Any = None
	selectedpoints: Any = None
	stream: Stream = None
	textfont: Textfont = Textfont()
	uid: Any = None
	uirevision: Any = None
	valueformat: Any = None
	valuesuffix: Any = None
	visible: Any = None


class Fillpattern(Settings):
	arg: Any = None
	bgcolor: Union[str, np.ndarray] = None
	bgcolorsrc: Any = None
	fgcolor: Union[str, np.ndarray] = None
	fgcolorsrc: Any = None
	fgopacity: float = None
	fillmode: Any = None
	shape: Shape = None
	shapesrc: Any = None
	size: Any = None
	sizesrc: Any = None
	solidity: Any = None
	soliditysrc: Any = None


class Scatter(Settings):
	arg: Any = None
	alignmentgroup: Any = None
	cliponaxis: Any = None
	connectgaps: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	dx: Any = None
	dy: Any = None
	error_x: Any = None
	error_y: Any = None
	fill: Fill = Fill()
	fillcolor: Union[str, np.ndarray] = None
	fillpattern: Fillpattern = None
	groupnorm: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hoveron: Any = None
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	mode: Any = None
	name: str = None
	offsetgroup: Any = None
	opacity: float = None
	orientation: Any = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	stackgaps: Any = None
	stackgroup: Any = None
	stream: Stream = None
	text: Any = None
	textfont: Textfont = Textfont()
	textposition: Any = None
	textpositionsrc: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None
	x: Any = None
	x0: Any = None
	xaxis: XAxis = XAxis()
	xcalendar: Any = None
	xhoverformat: Any = None
	xperiod: Any = None
	xperiod0: Any = None
	xperiodalignment: Any = None
	xsrc: Any = None
	y: Any = None
	y0: Any = None
	yaxis: YAxis = YAxis()
	ycalendar: Any = None
	yhoverformat: Any = None
	yperiod: Any = None
	yperiod0: Any = None
	yperiodalignment: Any = None
	ysrc: Any = None


class Scatter3d(Settings):
	arg: Any = None
	connectgaps: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	error_x: Any = None
	error_y: Any = None
	error_z: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	mode: Any = None
	name: str = None
	opacity: float = None
	projection: Projection = None
	scene: Scene = None
	showlegend: Any = None
	stream: Stream = None
	surfaceaxis: Any = None
	surfacecolor: Union[str, np.ndarray] = None
	text: Any = None
	textfont: Textfont = Textfont()
	textposition: Any = None
	textpositionsrc: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	x: Any = None
	xcalendar: Any = None
	xhoverformat: Any = None
	xsrc: Any = None
	y: Any = None
	ycalendar: Any = None
	yhoverformat: Any = None
	ysrc: Any = None
	z: Any = None
	zcalendar: Any = None
	zhoverformat: Any = None
	zsrc: Any = None


class Scattercarpet(Settings):
	arg: Any = None
	a: Any = None
	asrc: Any = None
	b: Any = None
	bsrc: Any = None
	carpet: Carpet = None
	connectgaps: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	fill: Fill = Fill()
	fillcolor: Union[str, np.ndarray] = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hoveron: Any = None
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	mode: Any = None
	name: str = None
	opacity: float = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	text: Any = None
	textfont: Textfont = Textfont()
	textposition: Any = None
	textpositionsrc: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None
	xaxis: XAxis = XAxis()
	yaxis: YAxis = YAxis()


class Scattergeo(Settings):
	arg: Any = None
	connectgaps: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	featureidkey: Any = None
	fill: Fill = Fill()
	fillcolor: Union[str, np.ndarray] = None
	geo: Geo = None
	geojson: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	lat: Any = None
	latsrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	locationmode: Any = None
	locations: Any = None
	locationssrc: Any = None
	lon: Any = None
	lonsrc: Any = None
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	mode: Any = None
	name: str = None
	opacity: float = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	text: Any = None
	textfont: Textfont = Textfont()
	textposition: Any = None
	textpositionsrc: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None


class Scattergl(Settings):
	arg: Any = None
	connectgaps: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	dx: Any = None
	dy: Any = None
	error_x: Any = None
	error_y: Any = None
	fill: Fill = Fill()
	fillcolor: Union[str, np.ndarray] = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	mode: Any = None
	name: str = None
	opacity: float = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	text: Any = None
	textfont: Textfont = Textfont()
	textposition: Any = None
	textpositionsrc: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None
	x: Any = None
	x0: Any = None
	xaxis: XAxis = XAxis()
	xcalendar: Any = None
	xhoverformat: Any = None
	xperiod: Any = None
	xperiod0: Any = None
	xperiodalignment: Any = None
	xsrc: Any = None
	y: Any = None
	y0: Any = None
	yaxis: YAxis = YAxis()
	ycalendar: Any = None
	yhoverformat: Any = None
	yperiod: Any = None
	yperiod0: Any = None
	yperiodalignment: Any = None
	ysrc: Any = None


class Cluster(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	colorsrc: Any = None
	enabled: Any = None
	maxzoom: Any = None
	opacity: float = None
	opacitysrc: Any = None
	size: Any = None
	sizesrc: Any = None
	step: Any = None
	stepsrc: Any = None


class Scattermapbox(Settings):
	arg: Any = None
	below: Any = None
	cluster: Cluster = None
	connectgaps: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	fill: Fill = Fill()
	fillcolor: Union[str, np.ndarray] = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	lat: Any = None
	latsrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	lon: Any = None
	lonsrc: Any = None
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	mode: Any = None
	name: str = None
	opacity: float = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	subplot: Any = None
	text: Any = None
	textfont: Textfont = Textfont()
	textposition: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None


class Scatterpolar(Settings):
	arg: Any = None
	cliponaxis: Any = None
	connectgaps: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	dr: Any = None
	dtheta: Any = None
	fill: Fill = Fill()
	fillcolor: Union[str, np.ndarray] = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hoveron: Any = None
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	mode: Any = None
	name: str = None
	opacity: float = None
	r: Any = None
	r0: Any = None
	rsrc: Any = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	subplot: Any = None
	text: Any = None
	textfont: Textfont = Textfont()
	textposition: Any = None
	textpositionsrc: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	theta: Any = None
	theta0: Any = None
	thetasrc: Any = None
	thetaunit: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None


class Scatterpolargl(Settings):
	arg: Any = None
	connectgaps: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	dr: Any = None
	dtheta: Any = None
	fill: Fill = Fill()
	fillcolor: Union[str, np.ndarray] = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	mode: Any = None
	name: str = None
	opacity: float = None
	r: Any = None
	r0: Any = None
	rsrc: Any = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	subplot: Any = None
	text: Any = None
	textfont: Textfont = Textfont()
	textposition: Any = None
	textpositionsrc: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	theta: Any = None
	theta0: Any = None
	thetasrc: Any = None
	thetaunit: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None


class Scattersmith(Settings):
	arg: Any = None
	cliponaxis: Any = None
	connectgaps: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	fill: Fill = Fill()
	fillcolor: Union[str, np.ndarray] = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hoveron: Any = None
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	imag: Any = None
	imagsrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	mode: Any = None
	name: str = None
	opacity: float = None
	real: Any = None
	realsrc: Any = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	subplot: Any = None
	text: Any = None
	textfont: Textfont = Textfont()
	textposition: Any = None
	textpositionsrc: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None


class Scatterternary(Settings):
	arg: Any = None
	a: Any = None
	asrc: Any = None
	b: Any = None
	bsrc: Any = None
	c: Any = None
	cliponaxis: Any = None
	connectgaps: Any = None
	csrc: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	fill: Fill = Fill()
	fillcolor: Union[str, np.ndarray] = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hoveron: Any = None
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	mode: Any = None
	name: str = None
	opacity: float = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	subplot: Any = None
	sum: Any = None
	text: Any = None
	textfont: Textfont = Textfont()
	textposition: Any = None
	textpositionsrc: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None


class Diagonal(Settings):
	arg: Any = None
	visible: Any = None


class Splom(Settings):
	arg: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	diagonal: Diagonal = None
	dimensions: Any = None
	dimensiondefaults: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	marker: Marker = Marker()
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	showlowerhalf: Any = None
	showupperhalf: Any = None
	stream: Stream = None
	text: Any = None
	textsrc: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None
	xaxes: Any = None
	xhoverformat: Any = None
	yaxes: Any = None
	yhoverformat: Any = None


class Starts(Settings):
	arg: Any = None
	x: Any = None
	xsrc: Any = None
	y: Any = None
	ysrc: Any = None
	z: Any = None
	zsrc: Any = None


class Streamtube(Settings):
	arg: Any = None
	autocolorscale: Any = None
	cauto: Any = None
	cmax: Any = None
	cmid: Any = None
	cmin: Any = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	customdata: Any = None
	customdatasrc: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	ids: Any = None
	idssrc: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	lighting: Lighting = None
	lightposition: Lightposition = None
	maxdisplayed: Any = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	reversescale: Any = None
	scene: Scene = None
	showlegend: Any = None
	showscale: Any = None
	sizeref: Any = None
	starts: Starts = None
	stream: Stream = None
	text: Any = None
	u: Any = None
	uhoverformat: Any = None
	uid: Any = None
	uirevision: Any = None
	usrc: Any = None
	v: Any = None
	vhoverformat: Any = None
	visible: Any = None
	vsrc: Any = None
	w: Any = None
	whoverformat: Any = None
	wsrc: Any = None
	x: Any = None
	xhoverformat: Any = None
	xsrc: Any = None
	y: Any = None
	yhoverformat: Any = None
	ysrc: Any = None
	z: Any = None
	zhoverformat: Any = None
	zsrc: Any = None


class Sunburst(Settings):
	arg: Any = None
	branchvalues: Any = None
	count: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	domain: Domain = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	insidetextfont: Insidetextfont = None
	insidetextorientation: Any = None
	labels: Any = None
	labelssrc: Any = None
	leaf: Leaf = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	level: Any = None
	marker: Marker = Marker()
	maxdepth: Any = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	outsidetextfont: Outsidetextfont = None
	parents: Any = None
	parentssrc: Any = None
	root: Root = None
	rotation: Rotation = None
	sort: Any = None
	stream: Stream = None
	text: Any = None
	textfont: Textfont = Textfont()
	textinfo: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	uid: Any = None
	uirevision: Any = None
	values: Any = None
	valuessrc: Any = None
	visible: Any = None


class Cells(Settings):
	arg: Any = None
	align: Any = None
	alignsrc: Any = None
	fill: Fill = Fill()
	font: Font = None
	format: Any = None
	formatsrc: Any = None
	height: Any = None
	line: Line = Line()
	prefix: Any = None
	prefixsrc: Any = None
	suffix: Any = None
	suffixsrc: Any = None
	values: Any = None
	valuessrc: Any = None


class Header(Settings):
	arg: Any = None
	align: Any = None
	alignsrc: Any = None
	fill: Fill = Fill()
	font: Font = None
	format: Any = None
	formatsrc: Any = None
	height: Any = None
	line: Line = Line()
	prefix: Any = None
	prefixsrc: Any = None
	suffix: Any = None
	suffixsrc: Any = None
	values: Any = None
	valuessrc: Any = None


class Table(Settings):
	arg: Any = None
	cells: Cells = None
	columnorder: Any = None
	columnordersrc: Any = None
	columnwidth: Any = None
	columnwidthsrc: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	domain: Domain = None
	header: Header = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	ids: Any = None
	idssrc: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	stream: Stream = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None


class Treemap(Settings):
	arg: Any = None
	branchvalues: Any = None
	count: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	domain: Domain = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	insidetextfont: Insidetextfont = None
	labels: Any = None
	labelssrc: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	level: Any = None
	marker: Marker = Marker()
	maxdepth: Any = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	outsidetextfont: Outsidetextfont = None
	parents: Any = None
	parentssrc: Any = None
	pathbar: Pathbar = None
	root: Root = None
	sort: Any = None
	stream: Stream = None
	text: Any = None
	textfont: Textfont = Textfont()
	textinfo: Any = None
	textposition: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	tiling: Tiling = None
	uid: Any = None
	uirevision: Any = None
	values: Any = None
	valuessrc: Any = None
	visible: Any = None


class Meanline(Settings):
	arg: Any = None
	color: Union[str, np.ndarray] = None
	visible: Any = None
	width: Any = None


class Violin(Settings):
	arg: Any = None
	alignmentgroup: Any = None
	bandwidth: Any = None
	box: Box = None
	customdata: Any = None
	customdatasrc: Any = None
	fillcolor: Union[str, np.ndarray] = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hoveron: Any = None
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	jitter: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	line: Line = Line()
	marker: Marker = Marker()
	meanline: Meanline = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	offsetgroup: Any = None
	opacity: float = None
	orientation: Any = None
	pointpos: Any = None
	points: Any = None
	quartilemethod: Any = None
	scalegroup: Any = None
	scalemode: Any = None
	selected: Selected = None
	selectedpoints: Any = None
	showlegend: Any = None
	side: Any = None
	span: Any = None
	spanmode: Any = None
	stream: Stream = None
	text: Any = None
	textsrc: Any = None
	uid: Any = None
	uirevision: Any = None
	unselected: Unselected = None
	visible: Any = None
	width: Any = None
	x: Any = None
	x0: Any = None
	xaxis: XAxis = XAxis()
	xhoverformat: Any = None
	xsrc: Any = None
	y: Any = None
	y0: Any = None
	yaxis: YAxis = YAxis()
	yhoverformat: Any = None
	ysrc: Any = None


class Volume(Settings):
	arg: Any = None
	autocolorscale: Any = None
	caps: Caps = None
	cauto: Any = None
	cmax: Any = None
	cmid: Any = None
	cmin: Any = None
	coloraxis: Coloraxis = None
	colorbar: ColorBar = ColorBar()
	colorscale: Colorscale = Colorscale()
	contour: Contour = None
	customdata: Any = None
	customdatasrc: Any = None
	flatshading: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	isomax: Any = None
	isomin: Any = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	lighting: Lighting = None
	lightposition: Lightposition = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	opacity: float = None
	opacityscale: Any = None
	reversescale: Any = None
	scene: Scene = None
	showlegend: Any = None
	showscale: Any = None
	slices: Slices = None
	spaceframe: Spaceframe = None
	stream: Stream = None
	surface: Surface = None
	text: Any = None
	textsrc: Any = None
	uid: Any = None
	uirevision: Any = None
	value: Any = None
	valuehoverformat: Any = None
	valuesrc: Any = None
	visible: Any = None
	x: Any = None
	xhoverformat: Any = None
	xsrc: Any = None
	y: Any = None
	yhoverformat: Any = None
	ysrc: Any = None
	z: Any = None
	zhoverformat: Any = None
	zsrc: Any = None


class Totals(Settings):
	arg: Any = None
	marker: Marker = Marker()


class Waterfall(Settings):
	arg: Any = None
	alignmentgroup: Any = None
	base: Any = None
	cliponaxis: Any = None
	connector: Connector = None
	constraintext: Any = None
	customdata: Any = None
	customdatasrc: Any = None
	decreasing: Decreasing = None
	dx: Any = None
	dy: Any = None
	hoverinfo: Any = None
	hoverinfosrc: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertemplate: Any = None
	hovertemplatesrc: Any = None
	hovertext: Any = None
	hovertextsrc: Any = None
	ids: Any = None
	idssrc: Any = None
	increasing: Increasing = None
	insidetextanchor: Any = None
	insidetextfont: Insidetextfont = None
	legendgroup: Any = None
	legendgrouptitle: Legendgrouptitle = None
	legendrank: Any = None
	legendwidth: Any = None
	measure: Any = None
	measuresrc: Any = None
	meta: Any = None
	metasrc: Any = None
	name: str = None
	offset: Any = None
	offsetgroup: Any = None
	offsetsrc: Any = None
	opacity: float = None
	orientation: Any = None
	outsidetextfont: Outsidetextfont = None
	selectedpoints: Any = None
	showlegend: Any = None
	stream: Stream = None
	text: Any = None
	textangle: Any = None
	textfont: Textfont = Textfont()
	textinfo: Any = None
	textposition: Any = None
	textpositionsrc: Any = None
	textsrc: Any = None
	texttemplate: Any = None
	texttemplatesrc: Any = None
	totals: Totals = None
	uid: Any = None
	uirevision: Any = None
	visible: Any = None
	width: Any = None
	widthsrc: Any = None
	x: Any = None
	x0: Any = None
	xaxis: XAxis = XAxis()
	xhoverformat: Any = None
	xperiod: Any = None
	xperiod0: Any = None
	xperiodalignment: Any = None
	xsrc: Any = None
	y: Any = None
	y0: Any = None
	yaxis: YAxis = YAxis()
	yhoverformat: Any = None
	yperiod: Any = None
	yperiod0: Any = None
	yperiodalignment: Any = None
	ysrc: Any = None


class ErrorX(Settings):
	arg: Any = None
	array: Any = None
	arrayminus: Any = None
	arrayminussrc: Any = None
	arraysrc: Any = None
	color: Union[str, np.ndarray] = None
	copy_ystyle: Any = None
	symmetric: Any = None
	thickness: Any = None
	traceref: Any = None
	tracerefminus: Any = None
	type: Any = None
	value: Any = None
	valueminus: Any = None
	visible: Any = None
	width: Any = None


class ErrorY(Settings):
	arg: Any = None
	array: Any = None
	arrayminus: Any = None
	arrayminussrc: Any = None
	arraysrc: Any = None
	color: Union[str, np.ndarray] = None
	copy_zstyle: Any = None
	symmetric: Any = None
	thickness: Any = None
	traceref: Any = None
	tracerefminus: Any = None
	type: Any = None
	value: Any = None
	valueminus: Any = None
	visible: Any = None
	width: Any = None


class Pattern(Settings):
	arg: Any = None
	bgcolor: Union[str, np.ndarray] = None
	bgcolorsrc: Any = None
	fgcolor: Union[str, np.ndarray] = None
	fgcolorsrc: Any = None
	fgopacity: float = None
	fillmode: Any = None
	shape: Shape = None
	shapesrc: Any = None
	size: Any = None
	sizesrc: Any = None
	solidity: Any = None
	soliditysrc: Any = None


class Tickformatstop(Settings):
	arg: Any = None
	dtickrange: Any = None
	enabled: Any = None
	name: str = None
	templateitemname: str = None
	value: Any = None


class Step(Settings):
	arg: Any = None
	args: Any = None
	execute: Any = None
	label: Any = None
	method: Any = None
	name: str = None
	templateitemname: str = None
	value: Any = None
	visible: Any = None


class Annotation(Settings):
	arg: Any = None
	align: Any = None
	arrowcolor: Union[str, np.ndarray] = None
	arrowhead: Any = None
	arrowside: Any = None
	arrowsize: Any = None
	arrowwidth: Any = None
	ax: Any = None
	axref: Any = None
	ay: Any = None
	ayref: Any = None
	bgcolor: Union[str, np.ndarray] = None
	bordercolor: Union[str, np.ndarray] = None
	borderpad: Any = None
	borderwidth: Any = None
	captureevents: Any = None
	clicktoshow: Any = None
	font: Font = None
	height: Any = None
	hoverlabel: Hoverlabel = Hoverlabel()
	hovertext: Any = None
	name: str = None
	opacity: float = None
	showarrow: Any = None
	standoff: Any = None
	startarrowhead: Any = None
	startarrowsize: Any = None
	startstandoff: Any = None
	templateitemname: str = None
	text: Any = None
	textangle: Any = None
	valign: Any = None
	visible: Any = None
	width: Any = None
	x: Any = None
	xanchor: Any = None
	xclick: Any = None
	xref: Any = None
	xshift: Any = None
	y: Any = None
	yanchor: Any = None
	yclick: Any = None
	yref: Any = None
	yshift: Any = None


class Selection(Settings):
	arg: Any = None
	line: Line = Line()
	name: str = None
	opacity: float = None
	path: Any = None
	templateitemname: str = None
	type: Any = None
	x0: Any = None
	x1: Any = None
	xref: Any = None
	y0: Any = None
	y1: Any = None
	yref: Any = None


class Currentvalue(Settings):
	arg: Any = None
	font: Font = None
	offset: Any = None
	prefix: Any = None
	suffix: Any = None
	visible: Any = None
	xanchor: Any = None


class Slider(Settings):
	arg: Any = None
	active: Any = None
	activebgcolor: Union[str, np.ndarray] = None
	bgcolor: Union[str, np.ndarray] = None
	bordercolor: Union[str, np.ndarray] = None
	borderwidth: Any = None
	currentvalue: Currentvalue = None
	font: Font = None
	len: Any = None
	lenmode: Any = None
	minorticklen: Any = None
	name: str = None
	pad: Pad = None
	steps: Any = None
	stepdefaults: Any = None
	templateitemname: str = None
	tickcolor: Union[str, np.ndarray] = None
	ticklen: Any = None
	tickwidth: Any = None
	transition: Transition = Transition()
	visible: Any = None
	x: Any = None
	xanchor: Any = None
	y: Any = None
	yanchor: Any = None


class Updatemenu(Settings):
	arg: Any = None
	active: Any = None
	bgcolor: Union[str, np.ndarray] = None
	bordercolor: Union[str, np.ndarray] = None
	borderwidth: Any = None
	buttons: Any = None
	buttondefaults: Any = None
	direction: Any = None
	font: Font = None
	name: str = None
	pad: Pad = None
	showactive: Any = None
	templateitemname: str = None
	type: Any = None
	visible: Any = None
	x: Any = None
	xanchor: Any = None
	y: Any = None
	yanchor: Any = None


class Button(Settings):
	arg: Any = None
	args: Any = None
	args2: Any = None
	execute: Any = None
	label: Any = None
	method: Any = None
	name: str = None
	templateitemname: str = None
	visible: Any = None


class Rangebreak(Settings):
	arg: Any = None
	bounds: Bounds = None
	dvalue: Any = None
	enabled: Any = None
	name: str = None
	pattern: Pattern = None
	templateitemname: str = None
	values: Any = None


class Dimension(Settings):
	arg: Any = None
	constraintrange: Any = None
	label: Any = None
	multiselect: Any = None
	name: str = None
	range: Any = None
	templateitemname: str = None
	tickformat: Any = None
	ticktext: Any = None
	ticktextsrc: Any = None
	tickvals: Any = None
	tickvalssrc: Any = None
	values: Any = None
	valuessrc: Any = None
	visible: Any = None


class Border(Settings):
	arg: Any = None
	arearatio: Any = None
	color: Union[str, np.ndarray] = None


class ErrorZ(Settings):
	arg: Any = None
	array: Any = None
	arrayminus: Any = None
	arrayminussrc: Any = None
	arraysrc: Any = None
	color: Union[str, np.ndarray] = None
	symmetric: Any = None
	thickness: Any = None
	traceref: Any = None
	tracerefminus: Any = None
	type: Any = None
	value: Any = None
	valueminus: Any = None
	visible: Any = None
	width: Any = None