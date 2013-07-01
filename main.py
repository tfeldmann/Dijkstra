# -*- coding: utf-8 -*-
"""
Dijkstra

A demo program to show the capabilites of dijkstra's algorithm.
"""

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtUiTools import *

class Field(object):
    pass

class FieldView(QWidget):
    def __init__(self, parent):
        super(FieldView, self).__init__()
        self.setMouseTracking(True)

        self.field = []
        self.selected = None
        self.setFieldSize(20, 30)

    def setFieldSize(self, xSize, ySize):
        self.xSize = xSize
        self.ySize = ySize
        self.field = [[0]*ySize for _ in range(xSize)]

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self._paintField(qp)
        qp.end()

    def _paintField(self, qp):
        normalColor = QColor(0, 0, 0, 0)
        hoverColor = QColor(255, 255, 255, 100)
        rectWidth = self.width() / self.xSize
        rectHeight = self.height() / self.ySize

        for x, row in enumerate(self.field):
            for y, field in enumerate(row):
                color = normalColor
                if self.selected != None and x == self.selected.x() and y == self.selected.y():
                    color = hoverColor
                qp.fillRect(x*rectWidth, y*rectHeight,
                    rectWidth, rectHeight, color)

    def mouseMoveEvent(self, m):
        self.selected = self._itemAtCoordinates(m.pos())
        self.update()

    def _itemAtCoordinates(self, pos):
        return QPoint(pos.x() * self.xSize / self.width(),
            pos.y() * self.ySize / self.height())


class App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        loader = QUiLoader()
        loader.registerCustomWidget(FieldView)
        self.ui = loader.load("main.ui", self)
        self.ui.show()
        QMetaObject.connectSlotsByName(self)

    @Slot()
    def on_save_triggered(self):
        print "save"

    @Slot()
    def on_load_triggered(self):
        print "load"

    @Slot()
    def on_clear_triggered(self):
        print "clear"


if __name__ == "__main__":
    import sys
    application = QApplication(sys.argv)
    app = App()
    application.exec_()
