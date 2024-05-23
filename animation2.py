import sys

from PySide6.QtCore import QRectF, Qt, QPropertyAnimation, QPoint, QTimer, QEasingCurve
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
        self.renderer = QSvgRenderer("images/svg/volna_mo.svg")

        pixmap = self.render_svg(1600, 900)
        self.label.setPixmap(pixmap)
        # self.label.setStyleSheet("border: 2px solid white; border-radius: 10px;")
        self.anim = QPropertyAnimation(self.label, b"pos")
        self.anim.setStartValue(QPoint(0, self.height() + self.height()))
        self.anim.setEndValue(QPoint(0, 0 - int(self.height() * 1.43)))
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.setDuration(3000)
        self.anim.start()

        self.setCentralWidget(self.label)
        self.resize(1600, 900)
        QTimer.singleShot(8000, self.start_hide_animation)  # Start hide animation after 8 seconds

    def start_hide_animation(self):
        self.anim.setStartValue(QPoint(0, 0 - int(self.height() * 1.43)))
        self.anim.setEndValue(QPoint(0, self.height() + self.height()))
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.setDuration(3000)
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
