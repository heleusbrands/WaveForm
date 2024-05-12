from pydantic.v1 import BaseModel
import pydantic.v1 as pyd
from PySide6.QtCore import Qt, QObject
from PySide6.QtGui import QPalette, QBrush, QWindow
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget
from typing import Union, TypeVar

I = TypeVar("I")
D = TypeVar("D")
A = TypeVar("A")


class Style(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        allow_mutation = True

    styleproperty: str = None
    stylevalue: Union[str, int, float] = None

class StyleSheet(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        allow_mutation = True

    backgroundcolor: Style = Style(styleproperty="background-color")
    alternatebackgroundcolor: Style = Style(styleproperty="alternate-background-color")
    color: Style = Style(styleproperty="color")
    bordercolor: Style = Style(styleproperty="border-color")
    borderwidth: Style = Style(styleproperty="border-width")
    borderstyle: Style = Style(styleproperty="border-style")
    borderradius: Style = Style(styleproperty="border-radius")
    gridlinecolor: Style = Style(styleproperty="gridline-color")
    selectioncolor: Style = Style(styleproperty="selection-color")
    backgroundimage: Style = Style(styleproperty="background-image")
    borderimage: Style = Style(styleproperty="border-image")
    image: Style = Style(styleproperty="image")

class State(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        allow_mutation = True
    
    color: str = None
    group: QPalette.ColorGroup = None

class Color(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        allow_mutation = True  

    role: QBrush
    color: str = None
    group: QPalette.ColorGroup = None
    Inactive: State = State(group=QPalette.ColorGroup.Inactive)
    Disabled: State = State(group=QPalette.ColorGroup.Disabled)

class Styler:
    def __init__(self, q: QObject):
        self._q = q
        self._color_palette: QPalette = q.palette()
        self._target_state = A
        self._stylesheet = StyleSheet()
        self._basecolor = Color(role=self._color_palette.base())
        self._textcolor = Color(role=self._color_palette.text())
        self._windowcolor = Color(role=self._color_palette.window())
        self._windowtextcolor = Color(role=self._color_palette.windowText())
        self._buttoncolor = Color(role=self._color_palette.button())
        self._buttontextcolor = Color(role=self._color_palette.buttonText())
        self._highlightcolor = Color(role=self._color_palette.highlight())
        self._highlighttextcolor = Color(role=self._color_palette.highlightedText())
        self._alternatebasecolor = Color(role=self._color_palette.alternateBase())

    @property
    def set_inactive_style(self):
        self._target_state = I
        return self
    
    @property
    def set_disabled_style(self):
        self._target_state = D
        return self

    def set_style(self, target: Color, style):
        cr = target.role
        color = style
        if self._target_state == I:
            target.Inactive.color = style
            cg = self._color_palette.ColorGroup.Inactive
            self._color_palette.setColor(cg, cr, color)
        elif self._target_state == D:
            target.Disabled.color = style
            cg = self._color_palette.ColorGroup.Disabled
            self._color_palette.setColor(cg, cr, color)
        else:
            target.color = style
            cr.setColor(color)
        self._target_state = A

    @property
    def stylesheet(self):
        return self._stylesheet
    
    def load_stylesheet(self):
        ss = ""
        for s in self._stylesheet.dict().values():
            if hasattr(s, 'stylevalue'):
                ss += f"{s.styleproperty}: {s.stylevalue};"
        self._q.setStyleSheet(ss)

    @property
    def basecolor(self):
        if self._target_state == A: return self._basecolor.color
        elif self._target_state == I: return self._basecolor.Inactive.color
        elif self._target_state == D: return self._basecolor.Disabled.color
    
    @basecolor.setter
    def basecolor(self, style):
        self.set_style(self._basecolor, style)

    @property
    def textcolor(self):
        if self._target_state == A: return self._textcolor.color
        elif self._target_state == I: return self._textcolor.Inactive.color
        elif self._target_state == D: return self._textcolor.Disabled.color

    @textcolor.setter
    def textcolor(self, style):
        self.set_style(self._textcolor, style)

    @property
    def windowcolor(self):
        if self._target_state == A: return self._windowcolor.color
        elif self._target_state == I: return self._windowcolor.Inactive.color
        elif self._target_state == D: return self._windowcolor.Disabled.color

    @windowcolor.setter
    def windowcolor(self, style):
        self.set_style(self._windowcolor, style)

    @property
    def windowtextcolor(self):
        if self._target_state == A: return self._windowtextcolor.color
        elif self._target_state == I: return self._windowtextcolor.Inactive.color
        elif self._target_state == D: return self._windowtextcolor.Disabled.color

    @windowtextcolor.setter
    def windowtextcolor(self, style):
        self.set_style(self._windowtextcolor, style)

    @property
    def buttoncolor(self):
        if self._target_state == A: return self._buttoncolor.color
        elif self._target_state == I: return self._buttoncolor.Inactive.color
        elif self._target_state == D: return self._buttoncolor.Disabled.color

    @buttoncolor.setter
    def buttoncolor(self, style):
        self.set_style(self._buttoncolor, style)

    @property
    def buttontextcolor(self):
        if self._target_state == A: return self._buttontextcolor.color
        elif self._target_state == I: return self._buttontextcolor.Inactive.color
        elif self._target_state == D: return self._buttontextcolor.Disabled.color

    @buttontextcolor.setter
    def buttontextcolor(self, style):
        self.set_style(self._buttontextcolor, style)

    @property
    def highlightcolor(self):
        if self._target_state == A: return self._highlightcolor.color
        elif self._target_state == I: return self._highlightcolor.Inactive.color
        elif self._target_state == D: return self._highlightcolor.Disabled.color
    
    @highlightcolor.setter
    def highlightcolor(self, style):
        self.set_style(self._highlightcolor, style)

    @property
    def highlighttextcolor(self):
        if self._target_state == A: return self._highlighttextcolor.color
        elif self._target_state == I: return self._highlighttextcolor.Inactive.color
        elif self._target_state == D: return self._highlighttextcolor.Disabled.color

    @highlighttextcolor.setter
    def highlighttextcolor(self, style):
        self.set_style(self._highlighttextcolor, style)

    @property
    def alternatebasecolor(self):
        if self._target_state == A: return self._alternatebasecolor.color
        elif self._target_state == I: return self._alternatebasecolor.Inactive.color
        elif self._target_state == D: return self._alternatebasecolor.Disabled.color

    @alternatebasecolor.setter
    def alternatebasecolor(self, style):
        self.set_style(self._alternatebasecolor, style)

class MainXploreWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.styles = Styler(self)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAutoFillBackground(True)
        self.create_ui()
        

    def create_ui(self):
        self.styles._color_palette.base().setColor('#121212')
        self.setWindowTitle("MainXplore")
        self.setFixedSize(800, 600)
        self.styles.basecolor = "#121212"
        self.styles.textcolor = "#ffffff"
        self.styles.windowcolor = "#121212"
        self.styles.windowtextcolor = "#ffffff"
        self.styles.buttoncolor = "#000000"
        self.styles.buttontextcolor = "#ffffff"
        self.styles.highlightcolor = "#000000"
        self.styles.highlighttextcolor = "#ffffff"
        self.styles.alternatebasecolor = "#121212"
        self.styles.stylesheet.backgroundcolor.stylevalue = "#121212"
        self.styles.load_stylesheet()