from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
import sys
from widget_configs import *

app = QApplication(sys.argv)
main_window = QMainWindow()
window = MainXploreWidget()
main_window.setCentralWidget(window)
window.styles._color_palette.base().setColor('#121212')
main_window.setPalette(window.styles._color_palette)
main_window.setAutoFillBackground(True)
main_window.show()
app.exec()


