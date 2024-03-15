from functools import reduce
from .wrapper import CRubberBand as crb 
from codex import SData, OData, Set, OptData



class Settings:
    
	defaults = crb.RubberBandStretcher.DefaultOptions

	_Engine = SData()
	_Engine.realtime: Set = Set(OptData(data=crb.RubberBandStretcher.Options.ProcessRealTime), _Engine)
	_Engine.offline: Set = Set(OptData(data=crb.RubberBandStretcher.Options.ProcessOffline), _Engine)

	_StretchMode = SData()
	_StretchMode.v3_precise: Set = Set(OptData(data=crb.RubberBandStretcher.Options.StretchPrecise), _StretchMode)
	_StretchMode.v2_elastic: Set = Set(OptData(data=crb.RubberBandStretcher.Options.StretchElastic), _StretchMode)

	_TransientMode = SData()
	_TransientMode.smooth: Set = Set(OptData(data=crb.RubberBandStretcher.Options.TransientsSmooth), _TransientMode)
	_TransientMode.mixed: Set = Set(OptData(data=crb.RubberBandStretcher.Options.TransientsMixed), _TransientMode)
	_TransientMode.crisp: Set = Set(OptData(data=crb.RubberBandStretcher.Options.TransientsCrisp), _TransientMode)

	_DetectorMode = SData()
	_DetectorMode.soft: Set = Set(OptData(data=crb.RubberBandStretcher.Options.DetectorSoft), _DetectorMode)
	_DetectorMode.percussive: Set = Set(OptData(data=crb.RubberBandStretcher.Options.DetectorPercussive), _DetectorMode)
	_DetectorMode.compound: Set = Set(OptData(data=crb.RubberBandStretcher.Options.DetectorCompound), _DetectorMode)

	_PhaseMode = SData()
	_PhaseMode.independent: Set = Set(OptData(data=crb.RubberBandStretcher.Options.PhaseIndependent), _PhaseMode)
	_PhaseMode.laminar: Set = Set(OptData(data=crb.RubberBandStretcher.Options.PhaseLaminar), _PhaseMode)

	_ThreadingMode = SData()
	_ThreadingMode.always: Set = Set(OptData(data=crb.RubberBandStretcher.Options.ThreadingAlways), _ThreadingMode)
	_ThreadingMode.never: Set = Set(OptData(data=crb.RubberBandStretcher.Options.ThreadingNever), _ThreadingMode)
	_ThreadingMode.auto: Set = Set(OptData(data=crb.RubberBandStretcher.Options.ThreadingAuto), _ThreadingMode)

	_WindowMode = SData()
	_WindowMode.long: Set = Set(OptData(data=crb.RubberBandStretcher.Options.WindowLong), _WindowMode)
	_WindowMode.short: Set = Set(OptData(data=crb.RubberBandStretcher.Options.WindowShort), _WindowMode)
	_WindowMode.standard: Set = Set(OptData(data=crb.RubberBandStretcher.Options.WindowStandard), _WindowMode)

	_SmoothingMode = SData()
	_SmoothingMode.on: Set = Set(OptData(data=crb.RubberBandStretcher.Options.SmoothingOn), _SmoothingMode)
	_SmoothingMode.off: Set = Set(OptData(data=crb.RubberBandStretcher.Options.SmoothingOff), _SmoothingMode)

	_FormantMode = SData()
	_FormantMode.preserved: Set = Set(OptData(data=crb.RubberBandStretcher.Options.FormantPreserved), _FormantMode)
	_FormantMode.shifted: Set = Set(OptData(data=crb.RubberBandStretcher.Options.FormantShifted), _FormantMode)

	_PitchMode = SData()
	_PitchMode.highconsistency: Set = Set(OptData(data=crb.RubberBandStretcher.Options.PitchHighConsistency), _PitchMode)
	_PitchMode.highquality: Set = Set(OptData(data=crb.RubberBandStretcher.Options.PitchHighQuality), _PitchMode)
	_PitchMode.highspeed: Set = Set(OptData(data=crb.RubberBandStretcher.Options.PitchHighSpeed), _PitchMode)

	_ChannelsMode = SData()
	_ChannelsMode.together: Set = Set(OptData(data=crb.RubberBandStretcher.Options.ChannelsTogether), _ChannelsMode)
	_ChannelsMode.apart: Set = Set(OptData(data=crb.RubberBandStretcher.Options.ChannelsApart), _ChannelsMode)

	def __init__(self):
		self.Processing = self._Engine
		self.EngineVersion = self._StretchMode
		self.Transient = self._TransientMode
		self.Detector = self._DetectorMode
		self.Phase = self._PhaseMode
		self.Threading = self._ThreadingMode
		self.Window = self._WindowMode
		self.Smoothing = self._SmoothingMode
		self.Formant = self._FormantMode
		self.Pitch = self._PitchMode
		self.Channels = self._ChannelsMode

	def __compile__(self):
		defined_settings = self._filter_attributes()
		defined_settings = reduce(lambda x, y: x+y, defined_settings)
		print(defined_settings)
		if len(defined_settings) == 0:
			return self.defaults
		elif len(defined_settings) == 1:
			return defined_settings[0]
		else:
			return reduce(lambda x, y: x.value__ | y.value__, defined_settings)
	
	def _filter_attributes(self, obj = None):
		if obj is None:
			obj = self
			public = filter(lambda x: not x.startswith('_'), obj.__dict__.keys())
			public = [getattr(obj, x) for x in public]
			return [self._filter_attributes(obj=o) for o in filter(lambda x: isinstance(x, SData), public)]
		else:
			public = filter(lambda x: not x.startswith('_'), obj.__dict__.keys())
			public = [getattr(obj, x) for x in public]
			options = filter(lambda x: isinstance(x, Set), public)
			option_data = [x._option for x in options]
			set_settings = [x.data for x in option_data if x.selected is True]
			return set_settings

