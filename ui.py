from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys

gif_file = "avatar_walk1_default.gif"
class GifPlayer(QWidget):
    def __init__(self, title, gif_file, parent=None):
        QWidget.__init__(self, parent)

        self.resize(1000, 1000)
        self.movie = QMovie(gif_file, QByteArray(), self)
        # size = self.movie.scaledSize()
        # self.setGeometry(200, 200, size.width(), size.height())
        self.setWindowTitle(title)

        self.character = QLabel()
        self.character.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.character.setAlignment(Qt.AlignCenter)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.character)
        self.setLayout(main_layout)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.character.setMovie(self.movie)
        self.movie.start()
        self.movie.loopCount()
        self.character.show()

        button = QPushButton('refresh gif', self)
        button.setToolTip('This is an example button')
        button.move(10,10)
        button.clicked.connect(self.on_click)
        main_layout.addWidget(button)


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_A:
            self.character.move(self.character.pos().x() - 1, self.character.pos().y() - 10)

    @pyqtSlot()
    def on_click(self):
        self.movie = QMovie(gif_file,QByteArray(), self)
        self.character.setMovie(self.movie)
        self.movie.start()
        print("done")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = GifPlayer("update this gif", gif_file)
    player.show()
sys.exit(app.exec_())