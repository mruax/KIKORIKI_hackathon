import sys

from PySide6.QtCore import QRectF, Qt, QPropertyAnimation, QPoint, QTimer
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtSvg import QSvgRenderer


class MainWindow(QMainWindow):
    def __init__(self):
        global pixmap
        super().__init__()
        self.title = "Анимация картинки SVG"
        self.setWindowTitle(self.title)

        self.label = QLabel(self)
        self.renderer = QSvgRenderer("images/volna.svg")

        pixmap = self.render_svg(200, 100)
        self.label.setPixmap(pixmap)
        self.label.setStyleSheet("border: 2px solid white; border-radius: 10px;")
        self.anim = QPropertyAnimation(self.label, b"pos")
        self.anim.setStartValue(QPoint(self.width() - pixmap.width(), 0))
        self.anim.setEndValue(QPoint(0, 0))
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.setDuration(2000)
        self.anim.start()
        self.setCentralWidget(self.label)
        self.resize(1000, 1000)

        QTimer.singleShot(8000, self.start_hide_animation)  # Start hide animation after 8 seconds
    def start_hide_animation(self):
        self.anim.setStartValue(QPoint(0, 0))
        self.anim.setEndValue(QPoint(-pixmap.width(), 0))
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
w.show()
sys.exit(app.exec())
