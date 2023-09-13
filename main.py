#todo:
#1. fix position affection by widgets !!!!! x
#2. add colors pallete x
#3. add some brushes x
#4. add some tools x
#5. expand toolbar x
#6. expand menu x
#7. saving file
#8. adding image
#9. fill *

#todo future:
#1. clear x
#2. ctrl z x
#3. color picker x
#4. copy of color // using pil/pyautogui lib
#5. pasting images
#6. text
#7. random brush x
#8. mirror brush // 4 pieces x

# SPRAY ADAPTATION
# RANDOM CHANGE
# NEW SLIDER FOR WIDTH/SIZE

import sys
import random as rd
from pathlib import Path
from widgets import *
from whiteboard import PaintZone

COLORS1 = [
    "#10751c", "#159924", "#17b529", "#35ed4a", "#87ee92", "#821c7b", "#b31ea9", "#e222d5", "#f075e8", "#f8b5f3",
    "#9c5c11", "#b46c18", "#e18923", "#e9a453", "#f4c38a", "#000000", "#444444", "#5b5b5b", "#999999", "#ffffff"
]

COLORS2 = [

    "#592296", "#6f25c1", "#8b3de1", "#ad71ef", "#c292f6", "#1d6b9f", "#1b87d0", "#2f9ee9", "#55b2f1", "#8cccf8",
    "#861d2b", "#c02136", "#e7364e", "#f17e8d", "#fbbcc4", "#3325bb", "#5344e4", "#8074f1", "#a9a0f8", "#cac5fc"
]


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
# -------------------------------------------------------- SETTINGS
        self.setWindowTitle("Coloriddo")
        self.setFixedSize(QSize(800, 600))
        self.setWindowIcon(QIcon('icons/icon.png'))

        self.toolbar = QToolBar("Toolbar")
        self.toolbar.setMovable(False)
        self.addToolBar(self.toolbar)
        self.save_path = None

# -------------------------------------------------------- TOOLBAR WIDGETS
        self.button_group = QButtonGroup()

        self.brush = BrushButton()                          # BRUSH
        self.spray = SprayButton()                          # SPRAY
        self.eraser = EraserButton()                        # ERASER
        self.random = RandomBrushButton()                   # RANDOM
        self.mirror = MirrorBrushButton()                   # MIRROR
        self.text = TextCreator()                           # TEXT
        self.fill = FloodFill()

        self.button_group.addButton(self.brush)
        self.button_group.addButton(self.spray)
        self.button_group.addButton(self.eraser)
        self.button_group.addButton(self.random)
        self.button_group.addButton(self.mirror)
        self.button_group.addButton(self.text)
        self.button_group.addButton(self.fill)

        self.brush.setChecked(True)
        self.button_group.buttonPressed.connect(self.change_tool)

        self.width_slider = WidthSlider()                        # WIDTH SLIDER
        self.width_slider.sliderMoved.connect(self.change_width)

        self.color_picker = ColorPicker()                        # COLOR PICKER

        self.undo = Undo()                                       # UNDO

        self.save = Save()                                       # SAVE

        self.new_page = NewPage()                                # NEW PAGE
        self.new_page.triggered.connect(self.fill_white)

        self.toolbar.addAction(self.new_page)                    # TOOLBAR LAYOUT
        self.toolbar.addAction(self.save)
        self.toolbar.addAction(self.undo)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.width_slider)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.brush)
        self.toolbar.addWidget(self.spray)
        self.toolbar.addWidget(self.fill)
        self.toolbar.addWidget(self.eraser)
        self.toolbar.addWidget(self.random)
        self.toolbar.addWidget(self.mirror)
        #self.toolbar.addWidget(self.text)
        self.toolbar.addWidget(self.color_picker)

# -------------------------------------------------------- MAIN LAYOUT SETTINGS
        layout_lab = QLabel()
        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(1)

# -------------------------------------------------------- PAINTZONE
        self.paintZone = PaintZone()
        self.layout.addWidget(self.paintZone, 0, 2)
        self.color_picker.dialog.currentColorChanged.connect(lambda x: self.paintZone.change_color(x))
        self.undo.triggered.connect(self.paintZone.undo)
        self.save.triggered.connect(self.save_image)
        self.add_color_buttons()

        layout_lab.setLayout(self.layout)
        self.setCentralWidget(layout_lab)

    def fill_white(self):
        self.paintZone.setPixmap(self.paintZone.paintZone)

    def save_image(self):
        if not self.save_path:
            dialog = QFileDialog()
            filename, _ = dialog.getSaveFileName(
                self,
                'Save File As',
                '',
                '*.png'
            )
            self.save_path = filename
        self.paintZone.pixmap().save(self.save_path)


    def change_tool(self, button):
        if button == self.spray:
            self.paintZone.set_spray()
        elif button == self.eraser:
            self.paintZone.set_eraser()
        elif button == self.brush:
            self.paintZone.set_brush()
        elif button == self.random:
            self.paintZone.set_random()
        elif button == self.mirror:
            self.paintZone.set_mirror()
        elif button == self.text:
            self.paintZone.set_text()
        elif button == self.fill:
            self.paintZone.set_fill()

    def change_width(self, width):
        self.paintZone.change_width(width)

# -------------------------------------------------------- ADDING BUTTONS
    def add_color_buttons(self):
        #pallete_lab = QLabel()
        pallete_lout = QVBoxLayout()
        pallete_lout.setSpacing(0)
        pallete_lout.setContentsMargins(20, 20, 0, 20)

        pallete_lout1 = QVBoxLayout()
        pallete_lout1.setSpacing(0)
        pallete_lout1.setContentsMargins(0, 20, 20, 20)

        for color1, color2 in zip(COLORS1, COLORS2):
            paint = ColorButton(color1)
            paint.pressed.connect(lambda x=color1: self.paintZone.change_color(x))
            paint1 = ColorButton(color2)
            paint1.pressed.connect(lambda x=color2: self.paintZone.change_color(x))
            pallete_lout.addWidget(paint)
            pallete_lout1.addWidget(paint1)
        #pallete_lab.setLayout(pallete_lout)
        self.layout.addLayout(pallete_lout, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addLayout(pallete_lout1, 0, 1, alignment=Qt.AlignmentFlag.AlignRight)


app = QApplication(sys.argv)

window = Window()
window.show()

app.exec()
