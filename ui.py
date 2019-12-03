from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui(QWidget):

    main_layout = QVBoxLayout()

    def __init__(self):
        super().__init__()
        self.resize(1046, 3772)  # original 1046 x 3772
        self.setWindowTitle("Forest of Patience")

        # background
        background_image = QImage('resource/back_ground_1.png')
        modified_background_image = background_image.scaled(QSize(1046, 3772))  # original 1046 x 3772
        palette = QPalette()
        palette.setBrush(10, QBrush(modified_background_image))
        self.setPalette(palette)

        # create main layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

