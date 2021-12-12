import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtCore import Qt
import random
from ui_class import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.should_paint_circle = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.should_paint_circle:
            painter = QPainter(self)
            diameter = random.randint(1, 800)
            start = 400 - int((diameter / 2))
            color = QColor(random.randint(0, 255),
                           random.randint(0, 255),
                           random.randint(0, 255)
                           )
            painter.setPen(QPen(color, 2, Qt.SolidLine))

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
