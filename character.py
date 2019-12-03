# postpone
# i will come back when i have time to fix it

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys


class Character(QLabel):

    is_first_right = True
    is_first_left = True
    is_first_release_right = True
    is_first_release_left = True
    current_x = 0
    current_y = 0


    def __init__(self):
        super().__init__()
        self.movie = QMovie('resource/avatar_stand1_default.gif', QByteArray(), self)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setAlignment(Qt.AlignCenter)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.setMovie(self.movie, self.current_x, self.current_y)
        self.movie.start()
        self.movie.loopCount()


    def setMovie(self, QMovie, x, y):
        super().setMovie(QMovie)
        self.move(x, y)


    def keyPressEvent(self, e):
        self.move(self.current_x, self.current_y)
        # right
        if e.key() == Qt.Key_D:
            if self.is_first_right:
                # initial character
                self.setVisible(False)
                self.movie = QMovie('resource/avatar_walk1_default_flip.gif', QByteArray(), self)
                self.setMovie(self.movie, self.current_x, self.current_y)
                self.movie.start()
                self.movie.loopCount()
                self.current_x = self.pos().x()
                self.current_y = self.pos().y()
                self.is_first_right = False
                self.is_first_left = True
                self.is_first_release_right = True
                print('click')
            # self.character.move(self.current_x + 5, self.current_y)
            self.move(self.current_x + 1, self.current_y)
            self.setVisible(True)
            self.move(self.current_x + 4, self.current_y)
            self.current_x = self.pos().x()
            self.current_y = self.pos().y()


        # left
        elif e.key() == Qt.Key_A:
            if self.is_first_left:
                # initial character
                self.setVisible(False)
                self.movie = QMovie('resource/avatar_walk1_default.gif', QByteArray(), self)
                self.setMovie(self.movie, self.current_x, self.current_y)
                self.movie.start()
                self.movie.loopCount()
                self.current_x = self.pos().x()
                self.current_y = self.pos().y()
                self.is_first_right = True
                self.is_first_left = False
                self.is_first_release_left = True
            # self.character.move(self.current_x + 5, self.current_y)
            self.move(self.current_x - 1, self.current_y)
            self.setVisible(True)
            self.move(self.current_x - 4, self.current_y)
            self.current_x = self.pos().x()
            self.current_y = self.pos().y()


        # up
        elif e.key() == Qt.Key_W:
            self.move(self.current_x, self.current_y - 5)
            self.current_x = self.pos().x()
            self.current_y = self.pos().y()

        # down
        elif e.key() == Qt.Key_S:
            self.move(self.current_x, self.current_y + 5)
            self.current_x = self.pos().x()
            self.current_y = self.pos().y()


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