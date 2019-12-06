from PyQt5.QtWidgets import *
import sys
from initial import Main


app = QApplication(sys.argv)
main = Main()
main.show()
sys.exit(app.exec_())
