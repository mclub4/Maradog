from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import resource_path


def monsters(self, monster, movie, x_pos):
    monster.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    monster.setAlignment(Qt.AlignCenter)
    monster.move(x_pos, 820)
    monster.setVisible(True)
    movie.setCacheMode(QMovie.CacheAll)
    monster.setMovie(movie)
    movie.start()
    movie.loopCount()


def slime(self, monster, movie, x_pos):
    monsters(self, monster, movie, x_pos)
    monster.resize(74, 92)


def orange_mushroom(self, monster, movie):
    monsters(self, monster, movie)
    monster.resize(64, 67)


def ribbonpig(self, monster, movie):
    monsters(self, monster, movie)
    monster.resize(67, 56)
