# postpone
# i will come back when i have time to fix it

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys


class Character(QLabel):
    def __init__(self):
        super().__init__()

    def setMovie(self, QMovie, x, y):
        super().setMovie(QMovie)
        self.move(x, y)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QVBoxLayout()
    char = Character("update this gif", "resource/avatar_walk1_default.gif", main)
    char.show()
    sys.exit(app.exec_())