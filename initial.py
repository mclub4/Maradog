from block import Block
from character import *


class Main(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # initial mainWindow
        self.resize(1440, 627)  # original 1046 x 3772
        self.setWindowTitle("Forest of Patience")

        # create main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # background
        background_image = QImage('resource/back_ground_4.png')
        modified_background_image = background_image.scaled(QSize(2000, 1080))  # original 3326 X 880
        palette = QPalette()
        palette.setBrush(10, QBrush(modified_background_image))
        self.setPalette(palette)

        # # blocks
        # block = Block(20000, 1000)
        # main_layout.addWidget(block)

        # character
        self.character = Character()
        self.character.setVisible(False)
        # self.character.move(100, 1000)
        # print(self.character.pos().x(), self.character.pos().y())
        main_layout.addWidget(self.character)


    def keyPressEvent(self, event):
        self.character.keyPressEvent(event)

        if event.key() == Qt.Key_Escape:
            self.close()

    def keyReleaseEvent(self, event):
        self.character.keyReleaseEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.showFullScreen()
    sys.exit(app.exec_())
