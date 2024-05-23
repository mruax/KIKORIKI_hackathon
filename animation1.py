import sys

from PySide6.QtCore import QPoint, QPropertyAnimation
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "Анимация картинки"
        self.setWindowTitle(self.title)

        self.label = QLabel(self)
        self.pixmap = QPixmap('cat.jpg')
        self.label.setPixmap(self.pixmap)
        self.label.setStyleSheet("border: 2px solid white; border-radius: 10px;")
        self.setCentralWidget(self.label)
        self.resize(1000,1000)

        self.anim = QPropertyAnimation(self.label, b"pos")
        self.anim.setStartValue(QPoint(0, 0))
        self.anim.setEndValue(QPoint(self.width() - self.pixmap.width(), self.height() - self.pixmap.height()))
        self.anim.setDuration(2000)
        self.anim.start()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
