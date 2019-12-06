from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time

current_x = -832  # -832
current_y = 327

# def initial(self, skill):
#     self.movie = QMovie('resource/skill_6.gif', QByteArray(), self)
#     skill.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#     skill.setAlignment(Qt.AlignCenter)
#     skill.move(200, 720)
#     self.movie.setCacheMode(QMovie.CacheAll)
#     skill.setMovie(self.movie)
#     self.movie.start()
#     self.movie.loopCount()

def keyPressEvent3(self, event):
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


def keyReleaseEvent(self, event):
    key = event.key()
    print(key)
    # release right
    if key == 68 and not event.isAutoRepeat():
        if self.is_first_release_right:
            self.setVisible(False)
            print('released')
            self.current_x = self.pos().x()
            self.current_y = self.pos().y()
            self.move(self.current_x, self.current_y)
            self.movie = QMovie('resource/avatar_stand1_default_flip.gif', QByteArray(), self)
            self.setMovie(self.movie, self.current_x, self.current_y)
            self.movie.start()
            self.movie.loopCount()
            self.move(self.current_x - 2, self.current_y)
            self.setVisible(True)
            self.move(self.current_x + 2, self.current_y)
            self.current_x = self.pos().x()
            self.current_y = self.pos().y()
            self.is_first_release_right = False
            self.is_first_right = True

    elif key == 65 and not event.isAutoRepeat():
        if self.is_first_release_left:
            self.setVisible(False)
            print('released')
            self.current_x = self.pos().x()
            self.current_y = self.pos().y()
            self.move(self.current_x, self.current_y)
            self.movie = QMovie('resource/avatar_stand1_default.gif', QByteArray(), self)
            self.setMovie(self.movie, self.current_x, self.current_y)
            self.movie.start()
            self.movie.loopCount()
            self.move(self.current_x - 2, self.current_y)
            self.setVisible(True)
            self.move(self.current_x + 2, self.current_y)
            self.current_x = self.pos().x()
            self.current_y = self.pos().y()
            self.is_first_release_left = False
            self.is_first_left = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QVBoxLayout()
    char = Character()
    char.show()
    sys.exit(app.exec_())