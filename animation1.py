import sys

from PySide6.QtCore import QRectF, Qt, QPropertyAnimation, QPoint, QTimer, QEasingCurve
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtSvg import QSvgRenderer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Анимация картинки SVG"
        self.setWindowTitle(self.title)



        self.resize(1000, 1000)
    def create(self, filepath, numb,i):
        self.numb=numb
        self.list=['label1','label2','label3']
        self.renderer = QSvgRenderer(filepath)
        self.list[i] = QLabel(self)
        self.pixmap = self.render_svg(200, 100)
        self.list[i].setPixmap(self.pixmap)
        self.list[i].setStyleSheet("border: 2px solid white; border-radius: 10px;")
        self.anim = QPropertyAnimation(self.list[i], b"pos")
        self.anim.setStartValue(QPoint(self.width() - self.pixmap.width(), numb))
        self.anim.setEndValue(QPoint(0, numb))
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.setDuration(2000)
        self.anim.start()
        self.setCentralWidget(self.list[i])


        QTimer.singleShot(8000, self.start_hide_animation)  # Start hide animation after 8 seconds

    def start_hide_animation(self):
        self.anim.setStartValue(QPoint(0, self.numb))
        self.anim.setEndValue(QPoint(-self.pixmap.width(), self.numb))
        self.anim.start()

    def render_svg(self, width, height):
        pixmap = QPixmap(width, height)
        pixmap.fill(Qt.transparent)

        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        self.renderer.render(painter, QRectF(0, 0, width, height))
        painter.end()

        return pixmap

app = QApplication(sys.argv)

w = MainWindow()
w.create('images\\volna.svg',0,0)
w.create('images\\volna_mo.svg',100,1)
w.create('images\\volna_oz.svg',200,2)
w.show()

sys.exit(app.exec())
