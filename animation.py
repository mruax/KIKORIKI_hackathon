from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl


class VideoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer(self)
        self.video_widget = QVideoWidget(self)
        self.player.setVideoOutput(self.video_widget)
        self.setCentralWidget(self.video_widget)
        self.player.setSource(QUrl.fromLocalFile("C:\\Users\\Адм\\Downloads\\Smoke_43___4K_res.mp4"))
        self.player.play()
if __name__ == "__main__":
    app = QApplication([])
    window = VideoWindow()
    window.show()
    app.exec()
