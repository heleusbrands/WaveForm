from __future__ import annotations
import pandas as pd
from pydantic.v1 import BaseModel, Field, create_model, validator
from pydantic.v1.dataclasses import dataclass
from itertools import chain
from copy import deepcopy
from enum import Enum
from collections import UserString
from typing import Any, Callable, NewType, Type, Union
import ctypes as ct
from rich import print
from rich.console import Group
from rich.padding import Padding
from rich.panel import Panel
from rich.progress import Progress, track
from rich.style import Style
from rich.syntax import Syntax
from rich.text import Text
from rich.tree import Tree




class GData(BaseModel):
    """
    GData is a pydantic based model that allows for easy .dot notation tree creation.
    """
    class Config:
        orm_mode = True
        extra = 'allow'
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
    name: str
    children: GData = None
GData.update_forward_refs()

class OData(BaseModel):
    """
    OData is similar to GData, in that it has a name and children attributes, 
    but by default it excludes those two attributes from the dict representation,
    which allows for pure .dot notation dictionary creation.
    """
    class Config:
        orm_mode = True
        extra = 'allow'
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        exclude = {'name', 'children'}
    name: str
    children: OData = Field(default=None, exclude=True)
OData.update_forward_refs()

@dataclass
class SData:
    """
    SData is a dataclass and was designed to be used for quick settings creation.
    It was designed to be simple and flexible, allowing for it's attributes to be set
    by either dot notation or operator. 

    Example:
    >>> settings = SData()
    >>> settings.milkchocolate = Set(OptData(), settings)
    >>> settings.darkchocolate = Set(OptData(), settings)
    >>> settings + 'other_options' # by default, using the '+' operator with a string will create a new SData attribute
    >>> settings.other_options.sprinkles = Set(OptData(), settings.other_options)
    """
    def __add__(self, value: Union[GData, OData, SData, str]):
        if isinstance(self, [GData, OData, SData]):
            setattr(self, value.name, value)
        elif isinstance(self, str):
            self.__setattr__(value, SData())

class OptData(BaseModel):
    """
    OptData is a pydantic based model that holds relevant data for a given option, including whether or not it has been selected.
    It was designed primarily to be used with the Set() class.
    """
    class Config:
        orm_mode = True
        extra = 'allow'
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
    selected: bool = False
    data: Any = None

class Set:
    """
    The Set class was created to allow for dot notation option setting. When it's true or false property is called,
    it will first set all other options in it's setting group to false, then set itself to true. This allows for 
    single selection options, essentially the code equivalent of radio buttons.

    It was also designed to be treated like a bool, returning true or false depending on whether it's option has been set.

    In addition, calling the instance returns it's option's data attribute.

    Example:
    >>> settings = SData()
    >>> settings.milkchocolate = Set(OptData(), settings)
    >>> settings.darkchocolate = Set(OptData(), settings)
    """
    def __init__(self, optdata: OptData, sdata: SData):
        self._option = optdata
        self._optionset = sdata

    def __call__(self):
        return self._option.data

    @property
    def true(self):
        for opt in self._optionset.__dict__.values():
            if type(opt) != bool:
                opt.false
        self._option.selected = True

    @property
    def false(self):
        self._option.selected = False

    def __bool__(self) -> bool:
        return self._option.selected

    def __repr__(self) -> str:
        return self._option.__repr__()
    
class G3Data(BaseModel):
    
    class Config:
        orm_mode = True
        extra = 'allow'
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
    
    x: pd.Series
    y: pd.Series
    z: pd.Series
    name: str = Field(default=None, exclude=True)
    color: str = Field(default=None, exclude=True)

class G2Data(BaseModel):
        
        class Config:
            orm_mode = True
            extra = 'allow'
            arbitrary_types_allowed = True
            allow_population_by_field_name = True
        
        x: pd.Series
        y: pd.Series
        name: str = Field(default=None, exclude=True)
        color: str = Field(default=None, exclude=True)


class GxData:
    def __init__(self):
        self._data = []

    def Data(self, name, value):
        self.__setattr__(name, value)
        self._data.append(value)
        return self

    def __add__(self, value):
        if type(value) is not str:
            self._data.append(value)
            return self
        else:
            self.__setattr__(value, GxData())
            return self.__getattribute__(value)