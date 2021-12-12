import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.should_paint_circle = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.should_paint_circle:
            painter = QPainter(self)
            diameter = random.randint(1, 800)
            start = 400 - int((diameter / 2))
            painter.setPen(QPen(Qt.yellow, 2, Qt.SolidLine))

            painter.drawEllipse(start, start, diameter, diameter)
            self.should_paint_circle = False

    def run(self):
        self.should_paint_circle = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
