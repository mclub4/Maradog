from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def skill_activate(self, event):
    if event.key() == Qt.Key_Q:
        start_timer()
        self.skill.setVisible(True)
        self.skill.resize(872, 242)
        self.skill.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.skill.setAlignment(Qt.AlignCenter)
        self.movie = QMovie('resource/skill_6.gif', QByteArray(), self)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.skill.setMovie(self.movie)
        self.movie.start()
        self.skill.move(self.character.pos().x()+50, self.character.pos().y()-80)


def start_timer():
    current_timer = QTimer()
    print('launch')
    current_timer.timeout.connect(print_hello)
    current_timer.setSingleShot(True)
    current_timer.start(3000)
    print('reach end')


def print_hello():
    print('hi')
