from __future__ import annotations
from pydantic.v1 import BaseModel
from .plotly_mappings import Settings
from .mapping_base import HtmlBase

from typing import Any
from collections import UserList
from dash import dcc, html
from random import randint

class Title(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class A(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	download: Any = None
	href: Any = None
	hrefLang: Any = None
	media: Any = None
	referrerPolicy: Any = None
	rel: Any = None
	shape: Any = None
	target: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Abbr(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Acronym(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Address(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Area(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	alt: Any = None
	coords: Any = None
	download: Any = None
	href: Any = None
	hrefLang: Any = None
	media: Any = None
	referrerPolicy: Any = None
	rel: Any = None
	shape: Any = None
	target: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Article(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Aside(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Audio(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	autoPlay: Any = None
	controls: Any = None
	crossOrigin: Any = None
	loop: Any = None
	muted: Any = None
	preload: Any = None
	src: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class B(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Base(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	href: Any = None
	target: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Basefont(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Bdi(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Bdo(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Big(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Blink(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Cite(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Blockquote(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	cite: Cite = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Br(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Form(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accept: Any = None
	acceptCharset: Any = None
	action: Any = None
	autoComplete: Any = None
	encType: Any = None
	method: Any = None
	name: Any = None
	noValidate: Any = None
	target: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Button(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	autoFocus: Any = None
	disabled: Any = None
	form: Form = None
	formAction: Any = None
	formEncType: Any = None
	formMethod: Any = None
	formNoValidate: Any = None
	formTarget: Any = None
	name: Any = None
	type: Any = None
	value: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Canvas(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	height: Any = None
	width: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Caption(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Center(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Code(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Span(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Col(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	span: Span = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Colgroup(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	span: Span = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Content(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Data(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	value: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Datalist(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Dd(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Del(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	cite: Cite = None
	dateTime: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Details(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	open: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Dfn(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Dialog(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	open: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Div(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Dl(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Dt(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Em(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Embed(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	height: Any = None
	src: Any = None
	type: Any = None
	width: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Fieldset(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	disabled: Any = None
	form: Form = None
	name: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Figcaption(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Figure(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Font(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Footer(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Frame(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Frameset(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class H1(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class H2(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class H3(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class H4(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class H5(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class H6(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Header(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Hgroup(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Hr(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class I(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Iframe(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	allow: Any = None
	height: Any = None
	name: Any = None
	referrerPolicy: Any = None
	sandbox: Any = None
	src: Any = None
	srcDoc: Any = None
	width: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Img(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	alt: Any = None
	crossOrigin: Any = None
	height: Any = None
	referrerPolicy: Any = None
	sizes: Any = None
	src: Any = None
	srcSet: Any = None
	useMap: Any = None
	width: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Ins(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	cite: Cite = None
	dateTime: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Kbd(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Keygen(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	autoFocus: Any = None
	challenge: Any = None
	disabled: Any = None
	form: Form = None
	keyType: Any = None
	name: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Label(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	htmlFor: Any = None
	form: Form = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Legend(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Li(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	value: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Link(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	crossOrigin: Any = None
	href: Any = None
	hrefLang: Any = None
	integrity: Any = None
	media: Any = None
	referrerPolicy: Any = None
	rel: Any = None
	sizes: Any = None
	type: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Main(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class MapEl(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	name: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Mark(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Marquee(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	loop: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Meta(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	charSet: Any = None
	content: Content = None
	httpEquiv: Any = None
	name: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Meter(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	form: Form = None
	high: Any = None
	low: Any = None
	max: Any = None
	min: Any = None
	optimum: Any = None
	value: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Nav(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Nobr(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Noscript(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class ObjectEl(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	data: Data = None
	form: Form = None
	height: Any = None
	name: Any = None
	type: Any = None
	useMap: Any = None
	width: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Ol(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	reversed: Any = None
	start: Any = None
	type: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Optgroup(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	disabled: Any = None
	label: Label = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Option(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	disabled: Any = None
	label: Label = None
	selected: Any = None
	value: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Output(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	htmlFor: Any = None
	form: Form = None
	name: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class P(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Param(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	name: Any = None
	value: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Picture(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Plaintext(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Pre(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Progress(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	form: Form = None
	max: Any = None
	value: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Q(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	cite: Cite = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Rb(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Rp(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Rt(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Rtc(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Ruby(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class S(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Samp(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Script(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	charSet: Any = None
	crossOrigin: Any = None
	defer: Any = None
	integrity: Any = None
	referrerPolicy: Any = None
	src: Any = None
	type: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Section(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Select(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	autoComplete: Any = None
	autoFocus: Any = None
	disabled: Any = None
	form: Form = None
	multiple: Any = None
	name: Any = None
	required: Any = None
	size: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Shadow(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Slot(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Small(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Source(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	media: Any = None
	sizes: Any = None
	src: Any = None
	srcSet: Any = None
	type: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Spacer(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Strike(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Strong(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Sub(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Summary(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Sup(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Table(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Tbody(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Td(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	colSpan: Any = None
	headers: Any = None
	rowSpan: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Template(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Textarea(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	autoComplete: Any = None
	autoFocus: Any = None
	cols: Any = None
	disabled: Any = None
	form: Form = None
	inputMode: Any = None
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
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Tfoot(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Th(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	colSpan: Any = None
	headers: Any = None
	rowSpan: Any = None
	scope: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Thead(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Time(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	dateTime: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Tr(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Track(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	default: Any = None
	kind: Any = None
	label: Label = None
	src: Any = None
	srcLang: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class U(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Ul(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Var(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Video(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	autoPlay: Any = None
	controls: Any = None
	crossOrigin: Any = None
	height: Any = None
	loop: Any = None
	muted: Any = None
	poster: Any = None
	preload: Any = None
	src: Any = None
	width: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Wbr(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None

class Xmp(Settings):
	children: Any = None
	id: Any = None
	n_clicks: Any = None
	n_clicks_timestamp: Any = None
	disable_n_clicks: Any = None
	key: Any = None
	accessKey: Any = None
	className: Any = None
	contentEditable: Any = None
	contextMenu: Any = None
	dir: Any = None
	draggable: Any = None
	hidden: Any = None
	lang: Any = None
	role: Any = None
	spellCheck: Any = None
	style: Any = None
	tabIndex: Any = None
	title: Title = None
	loading_state: Any = None


class Container(HtmlBase):

	def __init__(self, parent=None):
		super().__init__()
		self.parent = parent

	@property
	def title(self):
		self._layout_type = html.Title
		if type(self.settings) != Title: self.settings: Title = Title()
		return self.settings

	@property
	def a(self):
		self._layout_type = html.A
		if type(self.settings) != A: self.settings: A = A()
		return self.settings

	@property
	def abbr(self):
		self._layout_type = html.Abbr
		if type(self.settings) != Abbr: self.settings: Abbr = Abbr()
		return self.settings

	@property
	def acronym(self):
		self._layout_type = html.Acronym
		if type(self.settings) != Acronym: self.settings: Acronym = Acronym()
		return self.settings

	@property
	def address(self):
		self._layout_type = html.Address
		if type(self.settings) != Address: self.settings: Address = Address()
		return self.settings

	@property
	def area(self):
		self._layout_type = html.Area
		if type(self.settings) != Area: self.settings: Area = Area()
		return self.settings

	@property
	def article(self):
		self._layout_type = html.Article
		if type(self.settings) != Article: self.settings: Article = Article()
		return self.settings

	@property
	def aside(self):
		self._layout_type = html.Aside
		if type(self.settings) != Aside: self.settings: Aside = Aside()
		return self.settings

	@property
	def audio(self):
		self._layout_type = html.Audio
		if type(self.settings) != Audio: self.settings: Audio = Audio()
		return self.settings

	@property
	def b(self):
		self._layout_type = html.B
		if type(self.settings) != B: self.settings: B = B()
		return self.settings

	@property
	def base(self):
		self._layout_type = html.Base
		if type(self.settings) != Base: self.settings: Base = Base()
		return self.settings

	@property
	def basefont(self):
		self._layout_type = html.Basefont
		if type(self.settings) != Basefont: self.settings: Basefont = Basefont()
		return self.settings

	@property
	def bdi(self):
		self._layout_type = html.Bdi
		if type(self.settings) != Bdi: self.settings: Bdi = Bdi()
		return self.settings

	@property
	def bdo(self):
		self._layout_type = html.Bdo
		if type(self.settings) != Bdo: self.settings: Bdo = Bdo()
		return self.settings

	@property
	def big(self):
		self._layout_type = html.Big
		if type(self.settings) != Big: self.settings: Big = Big()
		return self.settings

	@property
	def blink(self):
		self._layout_type = html.Blink
		if type(self.settings) != Blink: self.settings: Blink = Blink()
		return self.settings

	@property
	def cite(self):
		self._layout_type = html.Cite
		if type(self.settings) != Cite: self.settings: Cite = Cite()
		return self.settings

	@property
	def blockquote(self):
		self._layout_type = html.Blockquote
		if type(self.settings) != Blockquote: self.settings: Blockquote = Blockquote()
		return self.settings

	@property
	def br(self):
		self._layout_type = html.Br
		if type(self.settings) != Br: self.settings: Br = Br()
		return self.settings

	@property
	def form(self):
		self._layout_type = html.Form
		if type(self.settings) != Form: self.settings: Form = Form()
		return self.settings

	@property
	def button(self):
		self._layout_type = html.Button
		if type(self.settings) != Button: self.settings: Button = Button()
		return self.settings

	@property
	def canvas(self):
		self._layout_type = html.Canvas
		if type(self.settings) != Canvas: self.settings: Canvas = Canvas()
		return self.settings

	@property
	def caption(self):
		self._layout_type = html.Caption
		if type(self.settings) != Caption: self.settings: Caption = Caption()
		return self.settings

	@property
	def center(self):
		self._layout_type = html.Center
		if type(self.settings) != Center: self.settings: Center = Center()
		return self.settings

	@property
	def code(self):
		self._layout_type = html.Code
		if type(self.settings) != Code: self.settings: Code = Code()
		return self.settings

	@property
	def span(self):
		self._layout_type = html.Span
		if type(self.settings) != Span: self.settings: Span = Span()
		return self.settings

	@property
	def col(self):
		self._layout_type = html.Col
		if type(self.settings) != Col: self.settings: Col = Col()
		return self.settings

	@property
	def colgroup(self):
		self._layout_type = html.Colgroup
		if type(self.settings) != Colgroup: self.settings: Colgroup = Colgroup()
		return self.settings

	@property
	def content(self):
		self._layout_type = html.Content
		if type(self.settings) != Content: self.settings: Content = Content()
		return self.settings

	@property
	def data(self):
		self._layout_type = html.Data
		if type(self.settings) != Data: self.settings: Data = Data()
		return self.settings

	@property
	def datalist(self):
		self._layout_type = html.Datalist
		if type(self.settings) != Datalist: self.settings: Datalist = Datalist()
		return self.settings

	@property
	def dd(self):
		self._layout_type = html.Dd
		if type(self.settings) != Dd: self.settings: Dd = Dd()
		return self.settings

	@property
	def delete(self):
		self._layout_type = html.Del
		if type(self.settings) != Del: self.settings: Del = Del()
		return self.settings

	@property
	def details(self):
		self._layout_type = html.Details
		if type(self.settings) != Details: self.settings: Details = Details()
		return self.settings

	@property
	def dfn(self):
		self._layout_type = html.Dfn
		if type(self.settings) != Dfn: self.settings: Dfn = Dfn()
		return self.settings

	@property
	def dialog(self):
		self._layout_type = html.Dialog
		if type(self.settings) != Dialog: self.settings: Dialog = Dialog()
		return self.settings

	@property
	def div(self):
		self._layout_type = html.Div
		if type(self.settings) != Div: self.settings: Div = Div()
		return self.settings

	@property
	def dl(self):
		self._layout_type = html.Dl
		if type(self.settings) != Dl: self.settings: Dl = Dl()
		return self.settings

	@property
	def dt(self):
		self._layout_type = html.Dt
		if type(self.settings) != Dt: self.settings: Dt = Dt()
		return self.settings

	@property
	def em(self):
		self._layout_type = html.Em
		if type(self.settings) != Em: self.settings: Em = Em()
		return self.settings

	@property
	def embed(self):
		self._layout_type = html.Embed
		if type(self.settings) != Embed: self.settings: Embed = Embed()
		return self.settings

	@property
	def fieldset(self):
		self._layout_type = html.Fieldset
		if type(self.settings) != Fieldset: self.settings: Fieldset = Fieldset()
		return self.settings

	@property
	def figcaption(self):
		self._layout_type = html.Figcaption
		if type(self.settings) != Figcaption: self.settings: Figcaption = Figcaption()
		return self.settings

	@property
	def figure(self):
		self._layout_type = html.Figure
		if type(self.settings) != Figure: self.settings: Figure = Figure()
		return self.settings

	@property
	def font(self):
		self._layout_type = html.Font
		if type(self.settings) != Font: self.settings: Font = Font()
		return self.settings

	@property
	def footer(self):
		self._layout_type = html.Footer
		if type(self.settings) != Footer: self.settings: Footer = Footer()
		return self.settings

	@property
	def frame(self):
		self._layout_type = html.Frame
		if type(self.settings) != Frame: self.settings: Frame = Frame()
		return self.settings

	@property
	def frameset(self):
		self._layout_type = html.Frameset
		if type(self.settings) != Frameset: self.settings: Frameset = Frameset()
		return self.settings

	@property
	def h1(self):
		self._layout_type = html.H1
		if type(self.settings) != H1: self.settings: H1 = H1()
		return self.settings

	@property
	def h2(self):
		self._layout_type = html.H2
		if type(self.settings) != H2: self.settings: H2 = H2()
		return self.settings

	@property
	def h3(self):
		self._layout_type = html.H3
		if type(self.settings) != H3: self.settings: H3 = H3()
		return self.settings

	@property
	def h4(self):
		self._layout_type = html.H4
		if type(self.settings) != H4: self.settings: H4 = H4()
		return self.settings

	@property
	def h5(self):
		self._layout_type = html.H5
		if type(self.settings) != H5: self.settings: H5 = H5()
		return self.settings

	@property
	def h6(self):
		self._layout_type = html.H6
		if type(self.settings) != H6: self.settings: H6 = H6()
		return self.settings

	@property
	def header(self):
		self._layout_type = html.Header
		if type(self.settings) != Header: self.settings: Header = Header()
		return self.settings

	@property
	def hgroup(self):
		self._layout_type = html.Hgroup
		if type(self.settings) != Hgroup: self.settings: Hgroup = Hgroup()
		return self.settings

	@property
	def hr(self):
		self._layout_type = html.Hr
		if type(self.settings) != Hr: self.settings: Hr = Hr()
		return self.settings

	@property
	def i(self):
		self._layout_type = html.I
		if type(self.settings) != I: self.settings: I = I()
		return self.settings

	@property
	def iframe(self):
		self._layout_type = html.Iframe
		if type(self.settings) != Iframe: self.settings: Iframe = Iframe()
		return self.settings

	@property
	def img(self):
		self._layout_type = html.Img
		if type(self.settings) != Img: self.settings: Img = Img()
		return self.settings

	@property
	def ins(self):
		self._layout_type = html.Ins
		if type(self.settings) != Ins: self.settings: Ins = Ins()
		return self.settings

	@property
	def kbd(self):
		self._layout_type = html.Kbd
		if type(self.settings) != Kbd: self.settings: Kbd = Kbd()
		return self.settings

	@property
	def keygen(self):
		self._layout_type = html.Keygen
		if type(self.settings) != Keygen: self.settings: Keygen = Keygen()
		return self.settings

	@property
	def label(self):
		self._layout_type = html.Label
		if type(self.settings) != Label: self.settings: Label = Label()
		return self.settings

	@property
	def legend(self):
		self._layout_type = html.Legend
		if type(self.settings) != Legend: self.settings: Legend = Legend()
		return self.settings

	@property
	def li(self):
		self._layout_type = html.Li
		if type(self.settings) != Li: self.settings: Li = Li()
		return self.settings

	@property
	def link(self):
		self._layout_type = html.Link
		if type(self.settings) != Link: self.settings: Link = Link()
		return self.settings

	@property
	def main(self):
		self._layout_type = html.Main
		if type(self.settings) != Main: self.settings: Main = Main()
		return self.settings

	@property
	def mapel(self):
		self._layout_type = html.MapEl
		if type(self.settings) != MapEl: self.settings: MapEl = MapEl()
		return self.settings

	@property
	def mark(self):
		self._layout_type = html.Mark
		if type(self.settings) != Mark: self.settings: Mark = Mark()
		return self.settings

	@property
	def marquee(self):
		self._layout_type = html.Marquee
		if type(self.settings) != Marquee: self.settings: Marquee = Marquee()
		return self.settings

	@property
	def meta(self):
		self._layout_type = html.Meta
		if type(self.settings) != Meta: self.settings: Meta = Meta()
		return self.settings

	@property
	def meter(self):
		self._layout_type = html.Meter
		if type(self.settings) != Meter: self.settings: Meter = Meter()
		return self.settings

	@property
	def nav(self):
		self._layout_type = html.Nav
		if type(self.settings) != Nav: self.settings: Nav = Nav()
		return self.settings

	@property
	def nobr(self):
		self._layout_type = html.Nobr
		if type(self.settings) != Nobr: self.settings: Nobr = Nobr()
		return self.settings

	@property
	def noscript(self):
		self._layout_type = html.Noscript
		if type(self.settings) != Noscript: self.settings: Noscript = Noscript()
		return self.settings

	@property
	def objectel(self):
		self._layout_type = html.ObjectEl
		if type(self.settings) != ObjectEl: self.settings: ObjectEl = ObjectEl()
		return self.settings

	@property
	def ol(self):
		self._layout_type = html.Ol
		if type(self.settings) != Ol: self.settings: Ol = Ol()
		return self.settings

	@property
	def optgroup(self):
		self._layout_type = html.Optgroup
		if type(self.settings) != Optgroup: self.settings: Optgroup = Optgroup()
		return self.settings

	@property
	def option(self):
		self._layout_type = html.Option
		if type(self.settings) != Option: self.settings: Option = Option()
		return self.settings

	@property
	def output(self):
		self._layout_type = html.Output
		if type(self.settings) != Output: self.settings: Output = Output()
		return self.settings

	@property
	def p(self):
		self._layout_type = html.P
		if type(self.settings) != P: self.settings: P = P()
		return self.settings

	@property
	def param(self):
		self._layout_type = html.Param
		if type(self.settings) != Param: self.settings: Param = Param()
		return self.settings

	@property
	def picture(self):
		self._layout_type = html.Picture
		if type(self.settings) != Picture: self.settings: Picture = Picture()
		return self.settings

	@property
	def plaintext(self):
		self._layout_type = html.Plaintext
		if type(self.settings) != Plaintext: self.settings: Plaintext = Plaintext()
		return self.settings

	@property
	def pre(self):
		self._layout_type = html.Pre
		if type(self.settings) != Pre: self.settings: Pre = Pre()
		return self.settings

	@property
	def progress(self):
		self._layout_type = html.Progress
		if type(self.settings) != Progress: self.settings: Progress = Progress()
		return self.settings

	@property
	def q(self):
		self._layout_type = html.Q
		if type(self.settings) != Q: self.settings: Q = Q()
		return self.settings

	@property
	def rb(self):
		self._layout_type = html.Rb
		if type(self.settings) != Rb: self.settings: Rb = Rb()
		return self.settings

	@property
	def rp(self):
		self._layout_type = html.Rp
		if type(self.settings) != Rp: self.settings: Rp = Rp()
		return self.settings

	@property
	def rt(self):
		self._layout_type = html.Rt
		if type(self.settings) != Rt: self.settings: Rt = Rt()
		return self.settings

	@property
	def rtc(self):
		self._layout_type = html.Rtc
		if type(self.settings) != Rtc: self.settings: Rtc = Rtc()
		return self.settings

	@property
	def ruby(self):
		self._layout_type = html.Ruby
		if type(self.settings) != Ruby: self.settings: Ruby = Ruby()
		return self.settings

	@property
	def s(self):
		self._layout_type = html.S
		if type(self.settings) != S: self.settings: S = S()
		return self.settings

	@property
	def samp(self):
		self._layout_type = html.Samp
		if type(self.settings) != Samp: self.settings: Samp = Samp()
		return self.settings

	@property
	def script(self):
		self._layout_type = html.Script
		if type(self.settings) != Script: self.settings: Script = Script()
		return self.settings

	@property
	def section(self):
		self._layout_type = html.Section
		if type(self.settings) != Section: self.settings: Section = Section()
		return self.settings

	@property
	def select(self):
		self._layout_type = html.Select
		if type(self.settings) != Select: self.settings: Select = Select()
		return self.settings

	@property
	def shadow(self):
		self._layout_type = html.Shadow
		if type(self.settings) != Shadow: self.settings: Shadow = Shadow()
		return self.settings

	@property
	def slot(self):
		self._layout_type = html.Slot
		if type(self.settings) != Slot: self.settings: Slot = Slot()
		return self.settings

	@property
	def small(self):
		self._layout_type = html.Small
		if type(self.settings) != Small: self.settings: Small = Small()
		return self.settings

	@property
	def source(self):
		self._layout_type = html.Source
		if type(self.settings) != Source: self.settings: Source = Source()
		return self.settings

	@property
	def spacer(self):
		self._layout_type = html.Spacer
		if type(self.settings) != Spacer: self.settings: Spacer = Spacer()
		return self.settings

	@property
	def strike(self):
		self._layout_type = html.Strike
		if type(self.settings) != Strike: self.settings: Strike = Strike()
		return self.settings

	@property
	def strong(self):
		self._layout_type = html.Strong
		if type(self.settings) != Strong: self.settings: Strong = Strong()
		return self.settings

	@property
	def sub(self):
		self._layout_type = html.Sub
		if type(self.settings) != Sub: self.settings: Sub = Sub()
		return self.settings

	@property
	def summary(self):
		self._layout_type = html.Summary
		if type(self.settings) != Summary: self.settings: Summary = Summary()
		return self.settings

	@property
	def sup(self):
		self._layout_type = html.Sup
		if type(self.settings) != Sup: self.settings: Sup = Sup()
		return self.settings

	@property
	def table(self):
		self._layout_type = html.Table
		if type(self.settings) != Table: self.settings: Table = Table()
		return self.settings

	@property
	def tbody(self):
		self._layout_type = html.Tbody
		if type(self.settings) != Tbody: self.settings: Tbody = Tbody()
		return self.settings

	@property
	def td(self):
		self._layout_type = html.Td
		if type(self.settings) != Td: self.settings: Td = Td()
		return self.settings

	@property
	def template(self):
		self._layout_type = html.Template
		if type(self.settings) != Template: self.settings: Template = Template()
		return self.settings

	@property
	def textarea(self):
		self._layout_type = html.Textarea
		if type(self.settings) != Textarea: self.settings: Textarea = Textarea()
		return self.settings

	@property
	def tfoot(self):
		self._layout_type = html.Tfoot
		if type(self.settings) != Tfoot: self.settings: Tfoot = Tfoot()
		return self.settings

	@property
	def th(self):
		self._layout_type = html.Th
		if type(self.settings) != Th: self.settings: Th = Th()
		return self.settings

	@property
	def thead(self):
		self._layout_type = html.Thead
		if type(self.settings) != Thead: self.settings: Thead = Thead()
		return self.settings

	@property
	def time(self):
		self._layout_type = html.Time
		if type(self.settings) != Time: self.settings: Time = Time()
		return self.settings

	@property
	def tr(self):
		self._layout_type = html.Tr
		if type(self.settings) != Tr: self.settings: Tr = Tr()
		return self.settings

	@property
	def track(self):
		self._layout_type = html.Track
		if type(self.settings) != Track: self.settings: Track = Track()
		return self.settings

	@property
	def u(self):
		self._layout_type = html.U
		if type(self.settings) != U: self.settings: U = U()
		return self.settings

	@property
	def ul(self):
		self._layout_type = html.Ul
		if type(self.settings) != Ul: self.settings: Ul = Ul()
		return self.settings

	@property
	def var(self):
		self._layout_type = html.Var
		if type(self.settings) != Var: self.settings: Var = Var()
		return self.settings

	@property
	def video(self):
		self._layout_type = html.Video
		if type(self.settings) != Video: self.settings: Video = Video()
		return self.settings

	@property
	def wbr(self):
		self._layout_type = html.Wbr
		if type(self.settings) != Wbr: self.settings: Wbr = Wbr()
		return self.settings

	@property
	def xmp(self):
		self._layout_type = html.Xmp
		if type(self.settings) != Xmp: self.settings: Xmp = Xmp()
		return self.settings