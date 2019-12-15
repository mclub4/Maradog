from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import threading


def ch_initial(self, character, movie):
    character.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    character.setAlignment(Qt.AlignCenter)
    movie.setCacheMode(QMovie.CacheAll)
    character.setMovie(self.movie)
    character.resize(106,75)
    movie.start()
    movie.loopCount()

def ob_initial(self, object, movie):
    object.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    object.setAlignment(Qt.AlignCenter)
    object.move(100, 820)
    movie.setCacheMode(QMovie.CacheAll)
    object.setMovie(self.movie)
    object.resize(106, 75)
    movie.start()
    movie.loopCount()

def mc_initial(self, object, movie):
    object.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    object.setAlignment(Qt.AlignCenter)
    object.move(1600, 740)
    movie.setCacheMode(QMovie.CacheAll)
    object.setMovie(self.movie)
    object.resize(286, 186)
    movie.start()
    movie.loopCount()

