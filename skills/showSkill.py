from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


def skill_activate(self, event):
    if event.key() == Qt.Key_Q:
        self.skill.setVisible(True)
        self.skill.resize(872,242)
        self.skill.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.skill.setAlignment(Qt.AlignCenter)
        self.movie = QMovie('resource/skill_6.gif', QByteArray(), self)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.skill.setMovie(self.movie)
        self.movie.start()
        self.movie.loopCount()
        self.skill.move(self.character.pos().x()+50,self.character.pos().y()-80)
        loop = QEventLoop()
        QTimer.singleShot(10000, loop.quit)
        loop.exec_()