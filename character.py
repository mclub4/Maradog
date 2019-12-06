from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def initial(self, character, movie):
    character.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    character.setAlignment(Qt.AlignCenter)
    character.move(100, 820)
    movie.setCacheMode(QMovie.CacheAll)
    character.setMovie(self.movie)
    movie.start()
    movie.loopCount()
