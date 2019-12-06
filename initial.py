import character
from skills.showSkill import *
import skills.showSkill


class Main(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        # initial mainWindow
        self.resize(1440, 627)  # original 1046 x 3772
        self.setWindowTitle("Forest of Patience")

        # background
        background_image = QImage('resource/back_ground_4.png')
        modified_background_image = background_image.scaled(QSize(2000, 1080))  # original 3326 X 880
        palette = QPalette()
        palette.setBrush(10, QBrush(modified_background_image))
        self.setPalette(palette)

        # character
        self.movie = QMovie("resource/avatar_walk1_default.gif", QByteArray(), self)
        self.character = QLabel('asd', self)
        character.initial(self, self.character, self.movie)

        # skill
        self.movie = self.movie = QMovie("resource/skill_6.gif", QByteArray(), self)
        self.skill = QLabel(self)
        skills.showSkill.initial(self, self.skill, self.movie)

    def keyPressEvent(self, event):
        character.keyPressEvent2(self, event)

        if event.key() == Qt.Key_Escape:
            self.close()
    #
    # def keyReleaseEvent(self, event):
    #     self.character.keyReleaseEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.showFullScreen()
    sys.exit(app.exec_())
