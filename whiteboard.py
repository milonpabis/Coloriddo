from widgets import *
import random as rd


# -------------------------------------------------------- PAINTZONE WIDGET
class PaintZone(QLabel):

    def __init__(self):
        super().__init__()

        self.TOOLBAR_H = 13

        self.prev_paintZones = []
        self.paintZone = QPixmap(QSize(800, 600))
        self.paintZone.fill()
        self.setPixmap(self.paintZone)

        self.prev_x = None
        self.prev_y = None

        self.p_color = QColor("000000")
        self.p_width = 1
        self.type = None
        self.set_brush()

    def mouseMoveEvent(self, e):
        local_point = e.position()
        if not self.prev_x:
            self.prev_x = local_point.x()
            self.prev_y = local_point.y()
            return

        play_gr = self.pixmap()
        painter = QPainter(play_gr)
        pen = painter.pen()
        pen.setWidth(self.p_width)
        pen.setColor(self.p_color)
        if self.type == 'e':
            pen.setColor(QColor('#ffffff'))
        if self.type == 's':
            pen.setWidth(1)
        painter.setPen(pen)


        if self.type in ['b', 'e']:
            painter.drawLine(QPoint(local_point.x(), local_point.y() + self.TOOLBAR_H),
                             QPoint(self.prev_x, self.prev_y + self.TOOLBAR_H))
        elif self.type == 's':
            painter.drawPoint(QPoint(local_point.x() + rd.randint(-self.p_width * 4, self.p_width * 4),
                                     local_point.y() + rd.randint(-self.p_width * 4,
                                                                  self.p_width * 4) + self.TOOLBAR_H))
            painter.drawPoint(QPoint(local_point.x() + rd.randint(-self.p_width * 4, self.p_width * 4),
                                     local_point.y() + rd.randint(-self.p_width * 4,
                                                                  self.p_width * 4) + self.TOOLBAR_H))
        elif self.type == 'r':
            painter.drawLine(QPoint(local_point.x(), local_point.y() + self.TOOLBAR_H),
                             QPoint(rd.randint(local_point.x() - 30, local_point.x() + 30),
                                    rd.randint(local_point.y() - 30, local_point.y() + 30)))

        elif self.type == 'm':
            painter.drawLine(QPoint(local_point.x(), local_point.y() + self.TOOLBAR_H),
                             QPoint(self.prev_x, self.prev_y + self.TOOLBAR_H))
            painter.drawLine(QPoint(local_point.x(), 564 - local_point.y() + self.TOOLBAR_H),
                             QPoint(self.prev_x, 564 - self.prev_y + self.TOOLBAR_H))
            painter.drawLine(QPoint(692 - local_point.x(), local_point.y() + self.TOOLBAR_H),
                             QPoint(692 - self.prev_x, self.prev_y + self.TOOLBAR_H))
            painter.drawLine(QPoint(692 - local_point.x(), 564 - local_point.y() + self.TOOLBAR_H),
                             QPoint(692 - self.prev_x, 564 - self.prev_y + self.TOOLBAR_H))


        elif self.type == 't':
            pass


        painter.end()
        self.setPixmap(play_gr)


        self.prev_x = local_point.x()
        self.prev_y = local_point.y()

    def flood_fill(self, point):
        x, y = point.x(), point.y()
        if x >= 0 and x <= 692 and y >= 0 and y <= 564:
            color = QColor(self.pixmap().toImage().pixel(x, y))
            print(color)



    def mouseReleaseEvent(self, e):
        self.prev_x = None
        self.prev_y = None

    def mousePressEvent(self, e):
        if len(self.prev_paintZones) < 50:
            a = self.pixmap().copy()
            self.prev_paintZones.append(a)

        if self.type == 'f':
            self.flood_fill(e.position())

        # pz = self.pixmap()
        # painter = QPainter(pz)
        # pen = painter.pen()
        # pen.setWidth(self.p_width)
        # pen.setColor(self.p_color)
        # painter.setPen(pen)
        # painter.drawPoint(QPoint(e.position().x(), e.position().y() + self.TOOLBAR_H))
        # painter.end()
        # self.setPixmap(pz)

    def undo(self):
        if len(self.prev_paintZones):
            undo = self.prev_paintZones[-1]
            self.prev_paintZones.remove(undo)
            self.setPixmap(undo)


    def change_color(self, color):
        if type(color) == str:
            self.p_color = QColor(color)
        elif isinstance(color, QColor):
            self.p_color = color

    def change_width(self, width):
        self.p_width = width

    def set_brush(self):
        self.type = 'b'

    def set_eraser(self):
        self.type = 'e'

    def set_spray(self):
        self.type = 's'

    def set_random(self):
        self.type = 'r'

    def set_mirror(self):
        self.type = 'm'

    def set_text(self):
        self.type = 't'

    def set_fill(self):
        self.type = 'f'
