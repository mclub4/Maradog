from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from initial import Main


app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())
