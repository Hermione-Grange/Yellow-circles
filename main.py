import sys

import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QPainter, QColor
from Ui import Ui_Dialog


class MyWidget(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
        
    def draw_circle(self, qp):
        R = random.randint(0, 225)
        G = random.randint(0, 225)
        B = random.randint(0, 225)
        x = random.randint(1, 300)
        y = random.randint(1, 200)
        radius = random.randint(1, 200)
        qp.setBrush(QColor(R, G, B))
        qp.drawEllipse(x, y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())