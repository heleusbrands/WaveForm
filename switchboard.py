from __future__ import annotations
from threading import Event
from pydantic.v1 import BaseModel
from typing import TypeVar, Union, Any
from rich.style import Style
from rich.text import Text
from rich.console import Console
from rich import print
from rich.repr import Result
from rich.tree import Tree

Switch = TypeVar('Switch', bound='Switch')
Circuit = TypeVar('Circuit', bound='Circuit')
Board = TypeVar('Board', bound='Board')
SwitchBoard = TypeVar('SwitchBoard', bound='SwitchBoard')
console = Console()

class CBModel(BaseModel):
    class Config:
        orm_mode = True
        extra = 'allow'
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        exclude = {'id', 'name'}

    def __add__(self, value = Union[Circuit, Switch]):
        if isinstance(self, Board) and isinstance(value, Circuit):
            self.add_circuit(value)
        elif isinstance(self, Circuit) and isinstance(value, Switch):
            setattr(self, value.name, value)

class Board(CBModel):
    class Config:
        orm_mode = True
        extra = 'allow'
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        exclude = {'id', 'name', 'base_circuit'}
    id: int
    name: str = None
    base_circuit: Circuit = None 

    def __repr__(self):
        children = list(self.dict(exclude=self.Config.exclude).keys())
        children = [f'\n{getattr(self, child).__repr__()}' if getattr(self, child) is not None else 'Empty Slot' for child in children]
        children_str = str('\n').join(children)
        return f'Board \n______\n[{self.id}: {self.name}]\n\n {children_str}'
    
    def __rich_repr__(self) -> Result:
        yield Text(self.__repr__())

    def collect(self):
        return [getattr(self, child).output for child in self.dict(exclude=self.Config.exclude).keys()]

class Circuit(CBModel):
    class Config:
        orm_mode = True
        extra = 'allow'
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        exclude = {'id', 'name', 'board', 'output', 'base_switch'}
        underscore_attrs_are_private = True
    _view: Tree = None
    output: Any = None
    board: SwitchBoard = None
    id: int
    name: str = None
    base_switch: Switch = None 

    def __repr__(self):
        children = list(self.dict(exclude=self.Config.exclude).keys())
        children = [f'\n\t[{child}] | On: {getattr(self, child).is_set()}' if getattr(self, child) is not None else 'Empty Slot' for child in children]
        for child in children:
            if 'True' in child:
                c = Text(child)
                c.highlight_words('True', Style(color='green'))
                children[children.index(child)] = c
            elif 'False' in child:
                c = Text(child)
                c.highlight_words('False', Style(color='red'))
                children[children.index(child)] = c
            else: 
                children[children.index(child)] = Text(child)     
        return f'Circuit: {self.name.capitalize()} \n-------\n[{self.id}: {self.name}]\n\tSwitches: {Text().join(children)}'
    
    def __rich_repr__(self) -> Result:
        self.board.view()
        yield self._view

    def ARM(self):
        self.board.__ensure_base_switch__(self)
        self.base_switch.on
        print(f'{self.name.capitalize()} Armed')

class Switch(Event):
    def __init__(self, circuit: Circuit, name, output = None):
        super().__init__()
        self.name = name
        self.circuit = circuit
        self.output = output
        self.storage = {}
        setattr(self.circuit, self.name, self)
        self.listener = self.altlisten
    
    def __repr__(self):
        return f'Switch \n______\n[{self.name}] | On: {self.is_set()}'
    
    def _view(self):
        text = Text(f'[{self.name}] | On: {self.is_set()}')
        if 'True' in text:
            text.highlight_words(['True'], Style(color='#3ADCA5'))
        elif 'False' in text:
            text.highlight_words(['False'], Style(color='#ED3A71'))
        return self.circuit._view.add(text)
    
    @property
    def listen(self):
        if self.name == 'base_switch': 
            self.set()
            return self.is_set()
        if self.circuit.base_switch is None: return self
        if not self.circuit.base_switch.is_set(): return self
        else: return self.on
    
    @property
    def altlisten(self):
        while True:
            if self.name == 'base_switch': 
                self.set()
                yield self.is_set()
            if self.circuit.base_switch is None: yield self
            if not self.circuit.base_switch.is_set(): yield self
            else: yield self.on

    @property
    def on(self):
        for s in self.circuit.dict(exclude=self.circuit.Config.exclude).values():
            if s.is_set():
                s.clear()
        self.set()
        if self.output:
            self.circuit.output = self.output
        else:
            self.circuit.output = self.name

        return self.is_set()

    @property
    def off(self):
        self.clear()
Circuit.update_forward_refs()

class SwitchBoard:
    def __init__(self, id, name = None):
        self._board = Board(id=id, name=name)
        self.id = id
        self.name = name
        self._set_base()
        self._view = None
    
    def _set_base(self):
        Circuit.update_forward_refs()
        self.new_circuit('base')
        
    def __repr__(self):
        return f'\nBoard \n______\n{self._board.id}: {self.name}\n({str(list(self.circuits.keys()))})'
    
    def __add__(self, circuit: Union[Circuit, str]):
        if isinstance(circuit, str):
            circuit = self.new_circuit(circuit)
        else:
            self.add_circuit(circuit)

    def __sub__(self, circuit: Circuit):
        self.remove_circuit(circuit)

    def __getitem__(self, name):
        return self.get_circuit(name)
    
    def __ensure_base_switch__(self, circuit: Circuit):
        if circuit.base_switch is None:
            circuit.base_switch = Switch(circuit, 'base_switch')
            setattr(self.board, 'base_switch', circuit)
    
    def view(self):
        tree = Tree(f'Board {self.id}: {self.name.capitalize()}')
        ckeys = list(self.circuits.keys())
        circs = [getattr(self._board, ckey) for ckey in ckeys]
        for c in circs:
            if c is None: continue
            if c.base_switch.is_set(): 
                text = Text(f'Circuit: {c.name}')
                text.highlight_words([c.name], Style(color='#3CE1E7', bold=True))
            else: text = Text(f'Circuit: {c.name}')
            c._view = tree.add(text)
            for s in c.dict(exclude=c.Config.exclude).values():
                if s is None: continue
                s._view()
        return tree
    
    def new_circuit(self, name):
        circuit = Circuit(board=self, id=len(self.circuits), name=name)
        circuit.base_switch = Switch(circuit=circuit, name='base_switch')
        self.add_circuit(circuit)
        return circuit
    
    @property
    def Circuit(self):
        return Circuit
    
    @property
    def Switch(self) -> Switch:
        return Switch
    
    @property
    def board(self):
        #self.__ensure_base_switch__()
        return self._board
    
    @property
    def board_dictionary(self):
        return self._board.dict(exclude={'id', 'name'})

    @property
    def circuits(self):
        #self.__ensure_base_switch__()
        return self._board.dict(exclude=self._board.Config.exclude)

    def add_circuit(self, circuit: Circuit):
        setattr(self._board, circuit.name, circuit)
    
    def remove_circuit(self, circuit: Circuit):
        delattr(self._board, circuit.name)
    
    def get_circuit(self, name):
        return getattr(self._board, name)
    
    def get_switch(self, circuit, name):
        return getattr(self.get_circuit(circuit), name)
    
    def whats_on(self):
        on_switches = []
        circuits = list(self.circuits.keys())
        for circuit in circuits:
            c = self.circuits[circuit]
            switches = list(c.keys())
            [on_switches.append(c[s]) for s in switches if c[s].is_set]
        return on_switches
    
    def ARM(self):
        for k in self.circuits.keys():
            self[k].ARM()