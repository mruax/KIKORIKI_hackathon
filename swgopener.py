import sys

from PySide6.QtCore import QRectF, Qt
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtSvg import QSvgRenderer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Анимация картинки SVG"
        self.setWindowTitle(self.title)

        self.label = QLabel(self)
        self.renderer = QSvgRenderer('volna.svg')

        pixmap = self.render_svg(200, 100)
        self.label.setPixmap(pixmap)
        self.label.setStyleSheet("border: 2px solid white; border-radius: 10px;")
        self.setCentralWidget(self.label)
        self.resize(1000, 1000)

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
