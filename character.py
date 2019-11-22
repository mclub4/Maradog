from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Character(QWidget):
    pass


class GifPlayer(QWidget):
    def __init__(self, title, gif_file, main_layout, parent=None):
        QWidget.__init__(self, parent)

        # character
        self.movie = QMovie(gif_file, QByteArray(), self)
        self.character = QLabel()
        self.character.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.character.setAlignment(Qt.AlignCenter)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.character.setMovie(self.movie)
        self.movie.start()
        self.movie.loopCount()
        main_layout.addWidget(self.character)


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
