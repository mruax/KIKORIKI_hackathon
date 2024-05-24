import json
import sys

from PySide6.QtCore import QRectF, Qt, QPropertyAnimation, QPoint, QTimer, QEasingCurve, QRect
from PySide6.QtGui import QPainter, QPixmap, QFont, QColor
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtSvg import QSvgRenderer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Кейс-задача "Social Media Optimizer"'
        self.setWindowTitle(self.title)
        self.resize(1600, 900)
        self.ico = QPixmap('images/logo.ico')
        self.setWindowIcon(self.ico)
        self.label = QLabel(self)

        # pixmapz = QPixmap("images/png/bg.png")
        # self.setStyleSheet(
        #     f"background-image: url({pixmapz}); background-repeat: no-repeat; background-position: center;")

        self.renderer = QSvgRenderer("images/svg/volna_mo.svg")

        self.pixmap = self.render_svg(1600, 900)
        self.label.setPixmap(self.pixmap)
        # self.label.setStyleSheet("border: 2px solid white; border-radius: 10px;")

        self.anim = QPropertyAnimation(self.label, b"pos")
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.start_anim()

        #self.label_ktelecom = QLabel(self)
        #self.pixmap = QPixmap('src/0233b510be29ef2f2f03f4d88b259c2f6744c61220cc1d73831c47dcf91fb702-400x400.webp')
        #self.label_ktelecom.setPixmap(self.pixmap)
        #self.label_ktelecom.resize(self.pixmap.width(), self.pixmap.height())
        #self.label_ktelecom.move(600, 250)

        #self.label_ktelecom.lower()

        # self.label_text = QLabel(self)
        # self.label_text.setText("Товар")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        # self.label_text.setFont(font)
        # self.label_text.setStyleSheet("color: black;")
        # self.label_text.setGeometry(400, 650, 200, 60)
        #
        # self.label_text.lower()

        label_price = QLabel(self)
        self.pixmap3 = QPixmap('images/png/price.png')
        self.pixmap3 = self.pixmap3.scaled(self.pixmap3.width() // 4, self.pixmap3.height() // 4)
        label_price.setPixmap(self.pixmap3)
        label_price.resize(self.pixmap3.width(), self.pixmap3.height())
        label_price.move(840, 540)

        self.setCentralWidget(self.label)

        QTimer.singleShot(8000, self.start_hide_animation)  # Start hide animation after 8 seconds

        self.names_index = 0
        self.names = []
        self.image_label = QLabel(self)
        self.image_label.move(600, 250)
        # self.names_label = QLabel(self)
        # self.names_label.move(50, 250)

        for filename in ["data_cctv.json", "data_popular.json", "data_routers.json", "data_tv.json"]:
            with open(filename, 'r', encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    self.names.append((item["name"], item["price"], item["source_path"]))


        self.names_label = QLabel(self)
        self.names_label.setStyleSheet("color: black;")
        self.names_label.setFont(font)

        # self.names_label.setAlignment(Qt.AlignCenter)
        self.names_label.setGeometry(QRect(200, self.height() - 270, self.width(), 100))

        self.price_label = QLabel(self)
        self.price_label.setStyleSheet("color: white;")
        self.price_label.setFont(font)
        # self.update_names_label()
        self.price_label.setGeometry(QRect(1100, self.height() - 270, self.width(), 100))

        self.update_names_label()

        self.image_label = QLabel(self)
        self.image_label.move(600, 250)

        label_LOGO = QLabel(self)
        self.pixmap4 = QPixmap('images/png/logo.png')
        self.pixmap4 = self.pixmap4.scaled(self.pixmap4.width() // 2, self.pixmap4.height() // 2)
        label_LOGO.setPixmap(self.pixmap4)
        label_LOGO.resize(self.pixmap4.width(), self.pixmap4.height())
        label_LOGO.move(20, -20)

        label_LOGO.lower()

        self.names_label.lower()
        self.price_label.lower()
        label_price.lower()
        self.image_label.lower()


    def pemolux(self, src):
        self.pixmap = QPixmap(src)
        self.label_ktelecom.setPixmap(self.pixmap)
        self.label_ktelecom.resize(self.pixmap.width(), self.pixmap.height())
        self.label_ktelecom.move(600, 250)

        self.label_ktelecom.lower()


    def start_hide_animation(self):
        self.anim.setStartValue(QPoint(0, 0))
        self.anim.setEndValue(QPoint(0, self.height() * 2))
        self.anim.setDuration(3000)
        self.anim.start()
        # self.anim.setLoopCount(-1)
        self.counter = True
        self.anim.finished.connect(self.start_anim)

    def start_anim(self):
        self.anim.setStartValue(QPoint(0, self.height() * 2))
        self.anim.setEndValue(QPoint(0, 0))
        self.anim.setDuration(8000)
        self.anim.start()
        self.anim.finished.connect(self.start_anim)

    def update_names_label(self):
        name, price, source_path = self.names[self.names_index]
        self.names_label.setText(name)
        self.names_label.setStyleSheet("color: #CB2156;")

        self.price_label.setText(price)
        self.price_label.setStyleSheet("color: white;")

        self.pixmap.load(source_path)
        self.image_label.setPixmap(self.pixmap)
        self.image_label.resize(self.pixmap.width(), self.pixmap.height())
        self.names_index = (self.names_index + 1) % len(self.names)
        self.image_label.update()
        self.image_label.lower()

        QTimer.singleShot(8000, self.update_names_label)

    def render_svg(self, width, height):
        self.pixmap = QPixmap(width, height)
        self.pixmap.fill(Qt.transparent)

        painter = QPainter(self.pixmap)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        self.renderer.render(painter, QRectF(0, 0, width, height))
        painter.end()

        return self.pixmap


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    # input()
    sys.exit(app.exec())
