import sys

from PySide6.QtCore import QRectF, Qt, QPropertyAnimation, QPoint, QTimer, QEasingCurve
from PySide6.QtGui import QPainter, QPixmap, QFont
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtSvg import QSvgRenderer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Анимация картинки SVG"
        self.setWindowTitle(self.title)
        self.resize(1600, 900)

        self.label = QLabel(self)
        self.renderer = QSvgRenderer("images/svg/volna_mo.svg")

        self.pixmap = self.render_svg(1600, 900)
        self.label.setPixmap(self.pixmap)
        # self.label.setStyleSheet("border: 2px solid white; border-radius: 10px;")
        self.anim = QPropertyAnimation(self.label, b"pos")
        self.anim.setStartValue(QPoint(0, self.height() * 2))
        self.anim.setEndValue(QPoint(0, 0 - self.height() // 1))
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.setDuration(3000)
        self.anim.start()

        label_ktelecom = QLabel(self)
        pixmap = QPixmap('src/600x800-1-400x267.webp')
        label_ktelecom.setPixmap(pixmap)
        label_ktelecom.resize(pixmap.width(), pixmap.height())
        label_ktelecom.move(100, 100)

        self.label_text = QLabel(self)
        self.label_text.setText("GAY")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_text.setFont(font)
        self.label_text.setStyleSheet("color: black;")
        self.label_text.move(100, 200)


        self.setCentralWidget(self.label)

        QTimer.singleShot(8000, self.start_hide_animation)  # Start hide animation after 8 seconds

    def start_hide_animation(self):
        self.anim.setStartValue(QPoint(0, 0 - self.height() // 1.43))
        self.anim.setEndValue(QPoint(0, self.height() * 2))
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.setDuration(3000)
        self.anim.start()
        self.counter = True

    def render_svg(self, width, height):
        self.pixmap = QPixmap(width, height)
        self.pixmap.fill(Qt.transparent)

        painter = QPainter(self.pixmap)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        self.renderer.render(painter, QRectF(0, 0, width, height))
        painter.end()

        return self.pixmap


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())