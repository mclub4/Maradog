from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from block import Block
import sys



class Main(QWidget):
    def __init__(self, title, gif_file, parent=None):
        QWidget.__init__(self, parent)

        # initial mainWindow
        self.resize(1046, 3772) # original 1046 x 3772
        self.setWindowTitle("Forest of Patience")

        # create main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # background
        background_image = QImage('resource/back_ground_1.png')
        modified_background_image = background_image.scaled(QSize(1046, 3772)) # original 1046 x 3772
        palette = QPalette()
        palette.setBrush(10, QBrush(modified_background_image))
        self.setPalette(palette)

        # blocks
        block = Block(10, 10)
        main_layout.addWidget(block)

        # character
        self.movie = QMovie(gif_file, QByteArray(), self)
        self.character = QLabel()
        self.character.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.character.setAlignment(Qt.AlignCenter)
        self.movie.setCacheMode(QMovie.CacheAll)
        self.character.setMovie(self.movie)
        self.movie.start()
        self.movie.loopCount()
        main_layout.addWidget(self.character)



    def keyPressEvent(self, e):
        # right
        if e.key() == Qt.Key_D:
            self.character.move(self.character.pos().x() + 5, self.character.pos().y())
            # 오른쪽 으로 방향 돌린 gif 로 설정
        # left
        elif e.key() == Qt.Key_A:
            self.character.move(self.character.pos().x() - 5, self.character.pos().y())
        # up
        elif e.key() == Qt.Key_W:
            self.character.move(self.character.pos().x(), self.character.pos().y() - 5)
        # down
        elif e.key() == Qt.Key_S:
            self.character.move(self.character.pos().x(), self.character.pos().y() + 5)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main("update this gif", "resource/avatar_walk1_default.gif")
    main.show()
    sys.exit(app.exec_())
