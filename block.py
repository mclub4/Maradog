from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Block(QLabel):
    def __init__(self, x, y):
        super().__init__()
        block_image = QPixmap('block.png')
        self.setPixmap(block_image)
        self.resize(10, 10)
        self.move(x, y)
