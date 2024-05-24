import os
import sys
import json
import time

from PySide6.QtCore import QRectF, Qt, QPropertyAnimation, QPoint, QTimer, QEasingCurve, QRect
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
        self.renderer = QSvgRenderer("../images/svg/volna_mo.svg")

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

        self.label_text = QLabel(self)
        self.label_text.setText("GAY")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label_text.setFont(font)
        self.label_text.setStyleSheet("color: black;")
        self.label_text.move(100, 200)

        QTimer.singleShot(8000, self.start_hide_animation)

        self.names_index = 0
        self.names = []
        for filename in ["data_cctv.json", "data_popular.json", "data_routers.json", "data_tv.json"]:
            with open(filename, 'r', encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    self.names.append(item["name"])
        self.names_label = QLabel(self)
        self.names_label.setStyleSheet("color: black;")
        self.names_label.setFont(font)
        self.update_names_label()
        self.names_label.setAlignment(Qt.AlignCenter)
        self.names_label.setGeometry(QRect(0, self.height() - 100, self.width(), 100))

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

        self.renderer.render(painter)
        painter.end()

        return self.pixmap

    def update_names_label(self):
        self.names_label.setText(self.names[self.names_index])
        self.names_index = (self.names_index + 1) % len(self.names)
        QTimer.singleShot(7000, self.update_names_label)


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())