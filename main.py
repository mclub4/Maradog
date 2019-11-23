from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from initial import Main

your_character = "resource/avatar_walk1_default.gif"

app = QApplication(sys.argv)
main = Main("update this gif", your_character)
main.show()
sys.exit(app.exec_())
