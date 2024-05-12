import ctypes
import functools
import numpy as np
from inspect import ismethod
import clr 
import System
from System import Array, Int32, Single
from System.Runtime.InteropServices import GCHandle, GCHandleType
import types
from pydantic.v1 import BaseModel
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union
from array import array

_MAP_NP_NET = {
	np.dtype(np.float32): System.Single,
	np.dtype(np.float64): System.Double,
	np.dtype(np.int8)   : System.SByte,
	np.dtype(np.int16)  : System.Int16,
	np.dtype(np.int32)  : System.Int32,
	np.dtype(np.int64)  : System.Int64,
	np.dtype(np.uint8)  : System.Byte,
	np.dtype(np.uint16) : System.UInt16,
	np.dtype(np.uint32) : System.UInt32,
	np.dtype(np.uint64) : System.UInt64,
	np.dtype(np.bool)   : System.Boolean,
}
_MAP_NET_NP = {
	'Single' : np.dtype(np.float32),
	'Double' : np.dtype(np.float64),
	'SByte'  : np.dtype(np.int8),
	'Int16'  : np.dtype(np.int16), 
	'Int32'  : np.dtype(np.int32),
	'Int64'  : np.dtype(np.int64),
	'Byte'   : np.dtype(np.uint8),
	'UInt16' : np.dtype(np.uint16),
	'UInt32' : np.dtype(np.uint32),
	'UInt64' : np.dtype(np.uint64),
	'Boolean': np.dtype(np.bool),
}

class UNet(BaseModel): # Represents an object that has undergone conversion to or from .NET object
	class Config:
		arbitrary_types_allowed = True
	obj: Any = None
	result: Any = None
	handle: GCHandle = None
	source_pointer: int = None
	destination_pointer: int = None

class UNetCall(BaseModel): # Represents a call to a .NET method, the results of that call, and the arguments passed to that call in the form of UNet objects
	class Config:
		arbitrary_types_allowed = True
		extra = 'allow'
		exclude = {'result'}
	result: Any = None


class asJaggedNetArray:
		"""
		A decorator that converts a numpy array to a jagged .NET array, 
		and any .NET array returned by the function to a numpy array.
		"""
		def __init__(self, func):
			self.func = func
			self.is_instance = False
			self.return_UNet = False
		
		def __call__(self, *args,**kwargs):
			instance = None
			if self.is_instance:
				instance = args[0]
				args = args[1:]
			print(args)
			new_args = []
			
			for arg in args:
				if (not isinstance(arg, np.ndarray) and type(arg) != np.ndarray) and not type(arg) == array:
					new_args.append(arg)
					continue
				# Ensure that the array is 1D
				if type(arg) == np.ndarray: 
					if len(arg.shape) == 1:
						iterable = arg.tolist()
					elif arg.shape[0] == 1 or arg.shape[1] == 1:
						iterable = arg.squeeze().tolist()
					elif arg.shape[0] > arg.shape[1]:
						iterable = arg.T[0].tolist()
					else:
						iterable = arg[0].tolist() # Note: Later I'd like to add support for multidimensional arrays, but right now my brain says no.
				elif type(arg) == array:
					iterable = list(arg)
				# Convert to Jagged .NET Array
				netArray = Array[Array[Single]]([
					Array[Single](iterable)
					])
				#destHandle = GCHandle.Alloc(netArray, GCHandleType.Pinned) # Not realy sure if this is neccessary, but adding it for safety
				#destPtr = destHandle.AddrOfPinnedObject().ToInt64() # Same as above
				arg = netArray
				new_args.append(arg) # Add back to args list

			if instance: new_args.insert(0, instance) # Add the instance (self) back to the args list
			print(new_args)
			result = self.func(*(new_args), **kwargs) # Call the function
			if isinstance(result, System.Array): result=np.ctypeslib.as_array(result)
			return result
		
		def __get__(self, instance, objtype=None):
			if instance is None:
				return self  # Accessed from class, return unchanged
			self.is_instance = True
			return types.MethodType(self, instance)  # Accessed from instance, bind to instance

class NetArrayConverter:
	"""
	def __init__(self):
		self._is_instance = False
		self.func = None
		self._return_UNet = False
	"""

	@property
	def is_instance(self):
		return self._is_instance
	
	@is_instance.setter
	def is_instance(self, value):
		self._is_instance = value

	@property
	def return_UNet(self):
		return self._return_UNet
	
	@return_UNet.setter
	def return_UNet(self, value):
		self._return_UNet = value

	def __get__(self, instance, objtype=None):
		if instance is None:
			return self  # Accessed from class, return unchanged
		self.is_instance = True
		return types.MethodType(self, instance)  # Accessed from instance, bind to instance
	
	def asNumpyArray(self, func):
		"""
		A decorator that converts any .NET array arguments to numpy.ndarray,
		and any .NET array returned by the function to a numpy array.
		"""
		new_args=[]
		call = UNetCall()
		def wrapper(*args, **kwargs):
			instance = None
			if self.is_instance:
				instance = args[0]
				args = args[1:]

			for arg in args:
				if isinstance(arg, System.Array):
					netArray = arg
				else: 
					new_args.append(arg)
					continue
				Uarg = self._toNumpyArray(netArray)
				setattr(call, f'arg{len(new_args)+1}', Uarg)
				new_args.append(Uarg.obj)
			
			if instance: new_args.insert(0, instance)
			result = func(*(new_args), **kwargs)
			if isinstance(result, System.Array): call.result=np.ctypeslib.as_array(result)
			else: call.result=result
			if self.return_UNet: return call
			return call.result
		return wrapper

	def _toNumpyArray(self, netArray: System.Array):
		"""
		Converts a .NET array to a numpy.ndarray
		"""
		dims = np.empty(netArray.Rank, dtype=int)
		for I in range(netArray.Rank):
			dims[I] = netArray.GetLength(I)
		netType = netArray.GetType().GetElementType().Name

		try:
			npArray = np.empty(dims, order='C', dtype=_MAP_NET_NP[netType])
		except KeyError:
			raise NotImplementedError(f'asNumpyArray does support System type {netType}')

		try: # Memmove 
			sourceHandle = GCHandle.Alloc(netArray, GCHandleType.Pinned)
			sourcePtr = sourceHandle.AddrOfPinnedObject().ToInt64()
			destPtr = npArray.__array_interface__['data'][0]
			ctypes.memmove(destPtr, sourcePtr, npArray.nbytes)
			
		finally:
			if sourceHandle.IsAllocated: 
				sourceHandle.Free()

		return UNet(obj=npArray, result=None, handle=sourceHandle, source_pointer=sourcePtr, destination_pointer=destPtr)
	
	def asNetArray(self, npArray):
		"""
		A decorator that converts any numpy.ndarray arguments or returns to .NET array
		"""
		dims = npArray.shape
		dtype = npArray.dtype

		# For complex arrays, we must make a view of the array as its corresponding 
		# float type as if it's (real, imag)
		if dtype == np.complex64:
			dtype = np.dtype(np.float32)
			dims += (2,)
			npArray = npArray.view(dtype).reshape(dims)
		elif dtype == np.complex128:
			dtype = np.dtype(np.float64)
			dims += (2,)
			npArray = npArray.view(dtype).reshape(dims)

		if not npArray.flags.c_contiguous or not npArray.flags.aligned:
			npArray = np.ascontiguousarray(npArray)
		assert npArray.flags.c_contiguous

		try:
			netArray = Array.CreateInstance(_MAP_NP_NET[dtype], *dims)
		except KeyError:
			raise NotImplementedError(f'asNetArray does not yet support dtype {dtype}')

		try: # Memmove 
			destHandle = GCHandle.Alloc(netArray, GCHandleType.Pinned)
			sourcePtr = npArray.__array_interface__['data'][0]
			destPtr = destHandle.AddrOfPinnedObject().ToInt64()
			ctypes.memmove(destPtr, sourcePtr, npArray.nbytes)
		finally:
			if destHandle.IsAllocated: 
				destHandle.Free()
		return UNet(obj=netArray, result=None, handle=destHandle, source_pointer=sourcePtr, destination_pointer=destPtr)