
from parselmouth.praat import call
from .handlers import Handlers
import types
import inspect


class PraatProcessor:
    def __init__(self, func):
        self.func = func
        self.defaults = inspect.getfullargspec(func).defaults
        self._handlers = None
        self._target = None

    def __call__(self, *args, **kwargs):
        instance = args[0] if self.is_instance else None
        if instance: args = args[1:]
        if not args: args = list(inspect.getfullargspec(self.func).defaults)
        self._target = instance._target if instance else None
        if not instance or not hasattr(self, '_target'): raise AttributeError(f'PraatProcessor has no attribute "_target".')
        arguments = [] # Since praat only takes positional arguements, compile kwargs into args
        if args: arguments.extend(args)
        if kwargs: arguments.extend(kwargs.values())
        praat_function: str = self.func(instance, *arguments) # Get the id of the praat function to call
        call_result = call(self._target, praat_function, *arguments) # Call the praat function
        for handler in self.handlers.dict().values(): # Iterate through the handlers
            if handler.__check__(call_result): # If the handler is applicable
                call_result = handler(call_result) # Apply the handler
        return call_result # Otherwise, return the result unchanged
    
    @property
    def handlers(self):
        if self._handlers is None: self._handlers = Handlers
        return self._handlers
        

    def __get__(self, instance, objtype=None):
        if instance is None:
            return self  # Accessed from class, return unchanged
        self.is_instance = True
        return types.MethodType(self, instance)  # Accessed from instance, bind to instance