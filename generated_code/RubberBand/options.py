from .wrapper import RubberBand 
from enum import Enum


 

class Options(Enum):

	_Options = RubberBand.RubberBandStretcher.Options
	ChannelsTogether = _Options.ChannelsTogether
	ChannelsApart = _Options.ChannelsApart.value__
	PitchHighConsistency = _Options.PitchHighConsistency.value__
	PitchHighQuality = _Options.PitchHighQuality.value__
	PitchHighSpeed = _Options.PitchHighSpeed.value__
	FormantPreserved = _Options.FormantPreserved.value__
	FormantShifted = _Options.FormantShifted.value__
	SmoothingOn = _Options.SmoothingOn.value__
	SmoothingOff = _Options.SmoothingOff.value__
	WindowLong = _Options.WindowLong.value__
	WindowShort = _Options.WindowShort.value__
	WindowStandard = _Options.WindowStandard.value__
	ThreadingAlways = _Options.ThreadingAlways.value__
	ThreadingNever = _Options.ThreadingNever.value__
	ThreadingAuto = _Options.ThreadingAuto.value__
	PhaseIndependent = _Options.PhaseIndependent.value__
	PhaseLaminar = _Options.PhaseLaminar.value__
	DetectorSoft = _Options.DetectorSoft.value__
	DetectorPercussive = _Options.DetectorPercussive.value__
	DetectorCompound = _Options.DetectorCompound.value__
	TransientsSmooth = _Options.TransientsSmooth.value__
	TransientsMixed = _Options.TransientsMixed.value__
	TransientsCrisp = _Options.TransientsCrisp.value__
	StretchPrecise = _Options.StretchPrecise.value__
	StretchElastic = _Options.StretchElastic.value__
	ProcessRealTime = _Options.ProcessRealTime.value__
	ProcessOffline = _Options.ProcessOffline.value__

	value__ = _Options.value__

