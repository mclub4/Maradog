from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys
import keyboard

gif_file = "avatar_walk1_default.gif"
class GifPlayer(QWidget):
    def __init__(self, title, gif_file, parent=None):
        QWidget.__init__(self, parent)

        self.resize(1046, 3772) # original 1046 x 3772
        self.setWindowTitle("Forest of Patience")

        # background
        background_image = QImage('back_ground_1.png')
        modified_background_image = background_image.scaled(QSize(1046, 3772)) # original 1046 x 3772
        palette = QPalette()
        palette.setBrush(10, QBrush(modified_background_image))
        self.setPalette(palette)

        # character
        self.movie = QMovie(gif_file, QByteArray(), self)
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

        # button event test
        button = QPushButton('refresh gif', self)
        button.setToolTip('This is an example button')
        button.move(10,10)
        button.clicked.connect(self.on_click)
        main_layout.addWidget(button)


    def keyPressEvent(self, e):
        # right
        if e.key() == Qt.Key_D:
            self.character.move(self.character.pos().x() + 5, self.character.pos().y())
            # 오른쪽 으로 방향 돌린 gif 로 설정
        # left
        elif e.key() == Qt.Key_A:
            self.character.move(self.character.pos().x() - 5, self.character.pos().y())
        # up
        elif e.key() == Qt.Key_W:
            self.character.move(self.character.pos().x(), self.character.pos().y() - 5)

        # down
        elif e.key() == Qt.Key_S:
            self.character.move(self.character.pos().x(), self.character.pos().y() + 5)


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
