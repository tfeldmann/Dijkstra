# -*- coding: utf-8 -*-
"""
Dijkstra

A demo program to show the capabilites of dijkstra's algorithm.
"""

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtUiTools import *

class FieldView(QWidget):
    def __init__(self, parent):
        super(FieldView, self).__init__()
        self.field = []
        self.setFieldSize(10, 50)

    def setFieldSize(self, xSize, ySize):
        self.field = [[0]*ySize for _ in range(xSize)]

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(255, 255, 255))
        qp.setBrush(QColor(255, 255, 184))
        for y, row in enumerate(self.field):
            for x, field in enumerate(row):
                qp.fillRect(x*(1+10), y*(1+10), 10, 10, QColor(100, 100, 100))
        qp.end()


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
