from PySide6.QtGui import QIcon, QColor, QAction, QPalette, QKeySequence, QPixmap, QPainter, QPen
from PySide6.QtCore import Qt, QSize, QPoint, QRect
from PySide6.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, QToolBar, QMenuBar, QFontComboBox,
                               QGridLayout, QCheckBox, QLabel, QSlider, QVBoxLayout, QHBoxLayout, QButtonGroup,
                               QColorDialog, QTextEdit, QDialog, QFileDialog)


# -------------------------------------------------------- COLOR BUTTON WIDGET
class ColorButton(QPushButton):

    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QSize(32, 32))
        self.setStyleSheet(f"background-color: {color}")


# -------------------------------------------------------- BRUSH BUTTON WIDGET
class BrushButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(32, 32))
        self.setCheckable(True)
        self.setIcon(QIcon("icons/paint-brush.png"))


# -------------------------------------------------------- SPRAY BUTTON WIDGET
class SprayButton(BrushButton):

    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("icons/spray.png"))


# -------------------------------------------------------- ERASER BUTTON WIDGET
class EraserButton(BrushButton):

    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("icons/eraser.png"))


# -------------------------------------------------------- RANDOM BRUSH BUTTON WIDGET
class RandomBrushButton(BrushButton):

    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("icons/randompen.png"))


# -------------------------------------------------------- MIRROR BRUSH BUTTON WIDGET
class MirrorBrushButton(BrushButton):

    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("icons/mirrorpen.png"))


# -------------------------------------------------------- WIDTH SLIDER WIDGET

class WidthSlider(QSlider):

    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(96, 16))
        self.setMinimum(1)
        self.setMaximum(12)
        self.setTickInterval(1)
        self.setOrientation(Qt.Horizontal)
        self.setContentsMargins(0, 8, 0, 8)


# --------------------------------------------------------- COLOR PICKER WIDGET
class ColorPicker(QPushButton):

    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(32, 32))
        self.setIcon(QIcon('icons/color.png'))
        self.pressed.connect(self.button_clicked)
        self.picked_color = None                                       # HERE
        self.dialog = QColorDialog(self)
        self.dialog.colorSelected.connect(self.change_color)

    def button_clicked(self):
        self.dialog.exec()

    def change_color(self, color):
        self.picked_color = color
        self.dialog.close()


# -------------------------------------------------------- NEW PAGE WIDGET
class NewPage(QAction):

    def __init__(self):
        super().__init__()
        self.setIcon(QIcon('icons/doc.png'))
        self.setShortcut(QKeySequence("Ctrl+n"))
        self.setToolTip("New Page: CTRL+N")


# -------------------------------------------------------- TEXT CREATOR WIDGET
class TextCreator(BrushButton):

    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("icons/text.png"))


# -------------------------------------------------------- UNDO WIDGET
class Undo(QAction):

    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("icons/undo.png"))
        self.setShortcut(QKeySequence("Ctrl+z"))
        self.setToolTip("Undo: CTRL+Z")


# -------------------------------------------------------- SAVE WIDGET
class Save(QAction):

    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("icons/save.png"))
        self.setShortcut(QKeySequence("Ctrl+s"))
        self.setToolTip("Save: CTRL+S")


# -------------------------------------------------------- FLOOD FILL WIDGET

class FloodFill(BrushButton):

    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("icons/fill.png"))


# -------------------------------------------------------- FLOOD FILL WIDGET
class Pipette(BrushButton):

    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("icons/pipette.png"))

