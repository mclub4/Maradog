# postpone
# i will come back when i have time to fix it

"""from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys



class GifPlayer(object):
    def __init__(self, title, gif_file, main_layout, parent=None):

        # character
        self.movie = QMovie(gif_file, QByteArray())
        self.character = QLabel()
        self.character.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.character.setAlignment(Qt.AlignCenter)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.character.setMovie(self.movie)
        self.movie.start()
        self.movie.loopCount()
        main_layout.addWidget(self.character)


class Character(QWidget, GifPlayer):
    def __init__(self, title, gif_file, main_layout, parent=None):
        super(Character, self).__init__()
        self.character = GifPlayer()
        self.character.setup(title, gif_file, main_layout)


    def keyPressEvent(self, e):
        # right
        if e.key() == Qt.Key_D:
            self.character.character.move(self.character.character.pos().x() + 5, self.character.character.pos().y())
            # 오른쪽 으로 방향 돌린 gif 로 설정
        # left
        elif e.key() == Qt.Key_A:
            self.character.character.move(self.character.character.pos().x() - 5, self.character.character.pos().y())
        # up
        elif e.key() == Qt.Key_W:
            self.character.character.move(self.character.character.pos().x(), self.character.character.pos().y() - 5)
        # down
        elif e.key() == Qt.Key_S:
            self.character.character.move(self.character.character.pos().x(), self.character.character.pos().y() + 5)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QVBoxLayout()
    char = Character("update this gif", "resource/avatar_walk1_default.gif", main)
    char.show()
    sys.exit(app.exec_())"""