from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

gif_file = "avatar_walk1_default.gif"
class GifPlayer(QWidget):
    def __init__(self, title, gif_file, parent=None):
        QWidget.__init__(self, parent)

        self.resize(1046, 3772) # original 1046 x 3772
        self.setWindowTitle("Forest of Patience")

        # background
        background_image = QImage('back_ground_1.png')
        modified_background_image = background_image.scaled(QSize(1046, 3772)) # original 1046 x 3772
        palette = QPalette()
        palette.setBrush(10, QBrush(modified_background_image))
        self.setPalette(palette)

        # create main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)


        # block
        self.block = Block(10, 10)
        main_layout.addWidget(self.block)
        self.block2 = Block(10, 20)
        main_layout.addWidget(self.block2)

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


    @pyqtSlot()
    def on_click(self):
        self.movie = QMovie(gif_file,QByteArray(), self)
        self.character.setMovie(self.movie)
        self.movie.start()
        print("done")



class Block(QLabel):
    def __init__(self, x, y):
        super().__init__()
        block_image = QPixmap('block.png')
        self.setPixmap(block_image)
        self.resize(10, 10)
        self.move(x, y)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = GifPlayer("update this gif", gif_file)
    player.show()
sys.exit(app.exec_())
