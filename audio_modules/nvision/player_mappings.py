from __future__ import annotations
from pydantic.v1 import BaseModel
from .plotly_mappings import Settings
from .mapping_base import HtmlBase
from typing import Any
from collections import UserList
from dash import dcc
import dash_player 


class DashPlayer(Settings):
	id: Any = None
	className: Any = None
	url: Any = None
	playing: Any = None
	loop: Any = None
	controls: Any = None
	volume: Any = None
	muted: Any = None
	playbackRate: Any = None
	width: Any = None
	height: Any = None
	style: Any = None
	playsinline: Any = None
	currentTime: Any = None
	secondsLoaded: Any = None
	duration: Any = None
	intervalCurrentTime: Any = None
	intervalSecondsLoaded: Any = None
	intervalDuration: Any = None
	seekTo: Any = None

class PlayerComponent(HtmlBase):

	def __init__(self, parent=None):
		super().__init__()
		self.parent = parent

	@property
	def dashplayer(self):
		self._layout_type = dash_player.DashPlayer
		if type(self.settings) != DashPlayer: self.settings: DashPlayer = DashPlayer()
		return self.settings