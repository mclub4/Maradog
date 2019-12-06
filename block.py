from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Block(QLabel):
    def __init__(self, x, y):
        super().__init__()
        block_image = QPixmap('resource/block.png')
        self.setPixmap(block_image)
        self.resize(10000, 10000)
        self.move(x, y)
