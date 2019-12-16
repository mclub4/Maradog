from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def initial(self, monster, movie):
    monster.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    monster.setAlignment(Qt.AlignCenter)
    monster.move(800, 820)
    movie.setCacheMode(QMovie.CacheAll)
    monster.setMovie(self.movie)
    movie.start()
    movie.loopCount()
