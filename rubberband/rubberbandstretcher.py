from functools import wraps
import os
from tempfile import NamedTemporaryFile
from typing import Iterable, Union
from .wrapper import CRubberBand as crb 
from .options import Settings
from codex import SData
from converters import NetArrayConverter, asJaggedNetArray
import clr
from System import Array, Single
from queue import Queue
from threading import Thread
import numpy as np

 

class RubberBandStretcher:
	settings = Settings()
	defaults = Settings.defaults

	def __init__(
			self, 
			sampleRate: int, 
			channels: int, 
			options=None, 
			initialTimeRatio=1.0, 
			initialPitchScale=1.0
		):
		if options is None: options = self.defaults
		else: options = options.__compile__()
		self._maps = SData()
		self._maps.PitchMap = PitchMap()
		self._maps.TimeMap = TimeMap()
		self._maps.FrequencyMap = FrequencyMap()
		self._buffer: np.ndarray = np.array([])
		self._queue: Queue = Queue()
		self._outqueue: Queue = Queue()
		self.Q = self._queue # Reference to the internal queue object used to pass data to be processed in realtime mode.
		self.Qout = self._outqueue # Reference to the internal queue object used to pass processed data in realtime mode.
		self._RubberBandStretcher = crb.RubberBandStretcher(
			sampleRate, 
			channels, 
			options, 
			initialTimeRatio, 
			initialPitchScale
		)
 
	def available(self, *args, **kwargs):
		return self._RubberBandStretcher.Available(*args, **kwargs)
 
	def calculate_stretch(self, *args, **kwargs):
		return self._RubberBandStretcher.CalculateStretch(*args, **kwargs)
 
	def dispose(self, *args, **kwargs):
		return self._RubberBandStretcher.Dispose(*args, **kwargs)
 
	def equals(self, *args, **kwargs):
		return self._RubberBandStretcher.Equals(*args, **kwargs)
 
	def finalize(self, *args, **kwargs):
		return self._RubberBandStretcher.Finalize(*args, **kwargs)
 
	def get_channel_count(self, *args, **kwargs):
		return self._RubberBandStretcher.GetChannelCount(*args, **kwargs)
 
	def get_exact_time_points(self, *args, **kwargs):
		return self._RubberBandStretcher.GetExactTimePoints(*args, **kwargs)
 
	def get_frequency_cutoff(self, n):
		return self._RubberBandStretcher.GetFrequencyCutoff(n)
 
	def get_hash_code(self, *args, **kwargs):
		return self._RubberBandStretcher.GetHashCode(*args, **kwargs)
 
	def get_input_increment(self, *args, **kwargs):
		return self._RubberBandStretcher.GetInputIncrement(*args, **kwargs)
 
	def get_latency(self, *args, **kwargs):
		return self._RubberBandStretcher.GetLatency(*args, **kwargs)
 
	def get_output_increments(self, *args, **kwargs):
		return self._RubberBandStretcher.GetOutputIncrements(*args, **kwargs)
 
	def get_phase_reset_curve(self, *args, **kwargs):
		return self._RubberBandStretcher.GetPhaseResetCurve(*args, **kwargs)
 
	def get_pitch_scale(self, *args, **kwargs):
		return self._RubberBandStretcher.GetPitchScale(*args, **kwargs)
 
	def get_samples_required(self, *args, **kwargs):
		return self._RubberBandStretcher.GetSamplesRequired(*args, **kwargs)
 
	def get_time_ratio(self, *args, **kwargs):
		return self._RubberBandStretcher.GetTimeRatio(*args, **kwargs)
 
	def get_type(self, *args, **kwargs):
		return self._RubberBandStretcher.GetType(*args, **kwargs)
 
	def memberwise_clone(self, *args, **kwargs):
		return self._RubberBandStretcher.MemberwiseClone(*args, **kwargs)
 
	def overloads(self, sampleRate: int, channels: int, options=Settings.defaults, initialTimeRatio=1.0, initialPitchScale=1.0):
		return self._RubberBandStretcher.Overloads(sampleRate, channels, options, initialTimeRatio, initialPitchScale)
	
	@asJaggedNetArray
	def process(self, input, num_sample_frames = None, final = False):
		if num_sample_frames == None: num_sample_frames = len(input[0])
		return self._RubberBandStretcher.Process(input, num_sample_frames, final)
	
	@property
	def maps(self):
		return self._maps

	def reference_equals(self, objA, objB):
		return self._RubberBandStretcher.ReferenceEquals(objA, objB)

	def reset(self, *args, **kwargs):
		return self._RubberBandStretcher.Reset(*args, **kwargs)
	
	def retrieve(self, all_available: bool = True, num_sample_frames: int = None):

		if num_sample_frames is None or all_available:

			num_sample_frames = self._RubberBandStretcher.Available()

		output = Array[Array[Single]]([

			Array.CreateInstance(Single, num_sample_frames)

			])
		
		self._RubberBandStretcher.Retrieve(output, num_sample_frames)

		return np.ctypeslib.as_array(output)
 
	def set_debug_level(self, level):
		return self._RubberBandStretcher.SetDebugLevel(level)
 
	def set_default_debug_level(self, level):
		return self._RubberBandStretcher.SetDefaultDebugLevel(level)
 
	def set_detector_option(self, options):
		options = options._option.data.value__
		return self._RubberBandStretcher.SetDetectorOption(options)
 
	def set_expected_input_duration(self, num_sample_frames:int):
		return self._RubberBandStretcher.SetExpectedInputDuration(num_sample_frames)
 
	def set_formant_option(self, options):
		options = options._option.data.value__
		return self._RubberBandStretcher.SetFormantOption(options)
 
	def set_frequency_cutoff(self, cutoff: int, frequency: float):
		return self._RubberBandStretcher.SetFrequencyCutoff(cutoff, frequency)
 
	def set_key_frame_map(self, map):
		return self._RubberBandStretcher.SetKeyFrameMap(map)
 
	def set_max_process_size(self, samples:int):
		return self._RubberBandStretcher.SetMaxProcessSize(samples)
 
	def set_phase_option(self, options):
		options = options._option.data.value__
		return self._RubberBandStretcher.SetPhaseOption(options)
 
	def set_pitch_option(self, options):
		options = options._option.data.value__
		return self._RubberBandStretcher.SetPitchOption(options)
 
	def set_pitch_scale(self, scale: float):
		return self._RubberBandStretcher.SetPitchScale(scale)
 
	def set_time_ratio(self, ratio:float):
		return self._RubberBandStretcher.SetTimeRatio(ratio)
 
	def set_transients_option(self, options):
		options = options._option.data.value__
		return self._RubberBandStretcher.SetTransientsOption(options)
	
	@asJaggedNetArray
	def study(self, input, num_sample_frames, final = False):
		return self._RubberBandStretcher.Study(input, num_sample_frames, final)
 
	def to_string(self, *args, **kwargs):
		return self._RubberBandStretcher.ToString(*args, **kwargs)


class SourceMap:
	def __init__(self):
		self._source_map = None
		self._file = NamedTemporaryFile(delete=False)
		self._file_name = self._file.name

	
	def __map_to_source__(self, a, b):

		if isinstance(a, Iterable) and isinstance(b, Iterable):
			if len(a) == len(b): data = np.transpose(np.vstack((a, b)))
		else: data = np.array([[a, b]])

		if self._source_map is None: self._source_map = data
		else: self._source_map = np.vstack((self._source_map, data))

		return self._source_map
	
	def __source_to_file__(self):
		if self._file.closed: self._file = NamedTemporaryFile(delete=False)
		self._file.seek(0)
		for row in self._source_map:
			if len(row) == 2: self._file.write(f"{row[0]} {row[1]}\n".encode())
			else:
				for i in range(len(row)):
					self._file.write(f"{row[i]} ".encode())
				self._file.write("\n".encode())
		self.__close_file__()
		return self._file.name

	def __close_file__(self):
		self._file.close()
	
	def __del_file__(self):
		if not self._file.closed: self.__close_file__()
		os.remove(self._file_name)

	def __bool__(self):
		return bool(self._source_map)

class SourceMapping:
	def __init__(self, func):
		wraps(func)(self)
	
	def __call__(self, wrapped_self, *args, **kwargs):
		
		result, sourcemap = self.__wrapped__(wrapped_self, *args, **kwargs)
		sourcemap.__del_file__()
		return result

class PitchMap(SourceMap):
	def __init__(self):
		super(PitchMap, self).__init__()
		self.temp_file = self._file

	@property
	def file_name(self):
		return self._file_name

	def frequency_to_ratio(self, original_frequencies: Union[int, list], new_frequencies: Union[int, list]):
		if original_frequencies and new_frequencies:
			if isinstance(original_frequencies, int) and isinstance(new_frequencies, int):
				original_frequencies = [original_frequencies]
				new_frequencies = [new_frequencies]
			pairs = tuple(zip(original_frequencies, new_frequencies))
			ratios = [new / original for original, new in pairs]
			return ratios
		
	def frequency_to_semitone(self, original_frequencies: Union[int, list], new_frequencies: Union[int, list]):
		if original_frequencies and new_frequencies:
			if isinstance(original_frequencies, int) and isinstance(new_frequencies, int):
				original_frequencies = [original_frequencies]
				new_frequencies = [new_frequencies]
			pairs = tuple(zip(original_frequencies, new_frequencies))
			semitones = [12 * np.log2(new / original) for original, new in pairs]
			return semitones
		
	def semitone_to_ratio(self, semitones: Union[int, list]):
		if semitones:
			if isinstance(semitones, int): semitones = [semitones]
			ratios = [2 ** (semitone / 12) for semitone in semitones]
			return ratios
		
	def semitone_to_frequency(self, original_frequencies: Union[int, list], semitones: Union[int, list]):
		if original_frequencies and semitones:
			if isinstance(original_frequencies, int) and isinstance(semitones, int):
				original_frequencies = [original_frequencies]
				semitones = [semitones]
			pairs = tuple(zip(original_frequencies, semitones))
			frequencies = [original * (2 ** (semitone / 12)) for original, semitone in pairs]
			return frequencies

	def add_to_map(self, sample_position: Union[int, list], ratio: Union[int, list]):
		if sample_position and ratio:
			self.__map_to_source__(sample_position, ratio)

	@property
	def get_map_array(self):
		return self._source_map
	
class TimeMap(SourceMap):
	def __init__(self):
		super(TimeMap, self).__init__()
		self.temp_file = self._file

	@property
	def file_name(self):
		return self._file_name
	
	def frame_to_time(self, rate: int, frames: Union[int, list]):
		if frames:
			if isinstance(frames, int): frames = [frames]
			times = [frame / rate for frame in frames]
			return times
	
	def time_to_frame(self, rate: int, times: Union[int, list]):
		if times:
			if isinstance(times, int): times = [times]
			frames = [time * rate for time in times]
			return frames

	def add_to_map(self, origin_sample: Union[int, list], destination_sample: Union[int, list]):
		if origin_sample and destination_sample:
			self.__map_to_source__(origin_sample, destination_sample)

	@property
	def get_map_array(self):
		return self._source_map
	
class FrequencyMap(SourceMap):
	def __init__(self):
		super(FrequencyMap, self).__init__()
		self.temp_file = self._file

	@property
	def file_name(self):
		return self._file_name
	
	def frequency_to_ratio(self, original_frequencies: Union[int, list], new_frequencies: Union[int, list]):
		if original_frequencies and new_frequencies:
			if isinstance(original_frequencies, int) and isinstance(new_frequencies, int):
				original_frequencies = [original_frequencies]
				new_frequencies = [new_frequencies]
			pairs = tuple(zip(original_frequencies, new_frequencies))
			ratios = [new / original for original, new in pairs]
			return ratios
		
	def ratio_to_frequency(self, original_frequencies: Union[int, list], ratios: Union[int, list]):
		if original_frequencies and ratios:
			if isinstance(original_frequencies, int) and isinstance(ratios, int):
				original_frequencies = [original_frequencies]
				ratios = [ratios]
			new_frequencies = [original * ratio for original, ratio in zip(original_frequencies, ratios)]
			return new_frequencies

	def add_to_map(self, sample_position: Union[int, list], frequency_multiplier: Union[int, list]):
		if sample_position and frequency_multiplier:
			self.__map_to_source__(sample_position, frequency_multiplier)

	@property
	def get_map_array(self):
		return self._source_map


class Processor(Thread):
	def __init__(self, rbs_instance: RubberBandStretcher):
		super().__init__()

		self._rbs = rbs_instance
		self._input_queue = self._rbs.Q
		self._output_queue = self._rbs.Qout
		self._running = False
		self.daemon = True
		self.total_frames_processed = 0
		self.pitchmap = None
		self.timemap = None
		self.frequencymap = None

	def run(self):
		self._running = True

		while self._running:

			if not self._input_queue.empty():

				input = self._input_queue.get()

				output_size = self._rbs.process(input)

				self.total_frames_processed += output_size

				output = self._rbs.retrieve()

				self._output_queue.put(output)