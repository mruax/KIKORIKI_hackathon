import sys

from PySide6.QtCore import QRectF, Qt, QPropertyAnimation, QPoint, QTimer, QEasingCurve
from PySide6.QtGui import QPainter, QPixmap, QFont
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout
from PySide6.QtSvg import QSvgRenderer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Анимация картинки SVG"
        self.setWindowTitle(self.title)
        self.resize(1600, 900)

        self.layout = QVBoxLayout()

        self.font = QFont("Comic sans", 24, QFont.Bold)

        self.item_name = QLabel(self)
        self.item_name.setText("Продукт")
        self.item_name.setFont(self.font)
        self.item_name.setGeometry(200, 200, 200, 400)
        self.layout.addWidget(self.item_name)

        self.setLayout(self.layout)

        self.image_label2 = QLabel()
        pixmap3 = QPixmap("images/png/logo.png")

        self.image_label2.resize(pixmap3.width(), pixmap3.height())
        self.image_label2.setPixmap(pixmap3)
        self.image_label2.move(12, 12)

        self.layout.addWidget(self.image_label2)


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
