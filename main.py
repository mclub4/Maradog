from ui import *
from block import *
from character import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


app = QApplication(sys.argv)

ui = Ui()
player = GifPlayer("update this gif", "resource/avatar_walk1_default.gif", ui.main_layout)
ui.show()


sys.exit(app.exec_())