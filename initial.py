import character
import skills.showSkill as showSkill
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from resource_path import *
import sys

global check
check = True

class Main(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.is_first_right = True
        self.is_first_left = True
        self.is_first_release_right = True
        self.is_first_release_left = True
        self.current_x = 0
        self.current_y = 0

        # initial mainWindow
        self.resize(1440, 627)
        self.setWindowTitle("Forest of Patience")

        # background
        background_image = QImage(background)
        modified_background_image = background_image.scaled(QSize(2000, 1080))
        palette = QPalette()
        palette.setBrush(10, QBrush(modified_background_image))
        self.setPalette(palette)

        # skill
        # self.movie = self.movie = QMovie("resource/skill_6.gif", QByteArray(), self)
        self.skill = QLabel(self)
        self.skill.setVisible(False)

        # character
        self.movie = QMovie(ch_stand, QByteArray(), self)
        self.character = QLabel('', self)
        character.initial(self, self.character, self.movie)



    def keyPressEvent(self, event):
        showSkill.skill_activate(self, event)
        # initial skill key event
        # character.keyPressEvent2(self, event)
        global check

        self.current_x = self.character.pos().x()
        self.current_y = self.character.pos().y()
        # right
        if event.key() == Qt.Key_D:
            if self.is_first_right and check == True:
                # initial character
                print(check)
                self.movie = QMovie(ch_walk, QByteArray(), self)
                character.initial(self, self.character, self.movie)
                self.is_first_right = False
                self.is_first_left = True
                self.is_first_release_right = True
            self.character.move(self.current_x + 5, self.current_y)

        # left
        elif event.key() == Qt.Key_A:
            if self.is_first_left:
                # initial character
                self.movie = QMovie(ch_walk, QByteArray(), self)
                character.initial(self, self.character, self.movie)
                self.is_first_right = True
                self.is_first_left = False
                self.is_first_release_left = True
            self.character.move(self.current_x - 5, self.current_y)

        if event.key() == Qt.Key_Escape:
            self.close()

    def keyReleaseEvent(self, event):
        self.current_x = self.character.pos().x()
        self.current_y = self.character.pos().y()
        global check
        key = event.key()
        # release right
        if key == 68 and not event.isAutoRepeat():
            if self.is_first_release_right:
                self.movie = QMovie(ch_stand, QByteArray(), self)
                character.initial(self, self.character, self.movie)
                self.is_first_release_right = False
                self.is_first_right = True
                self.character.move(self.current_x, self.current_y)

        # release left
        elif key == 65 and not event.isAutoRepeat():
            if self.is_first_release_left:
                self.movie = QMovie(ch_stand, QByteArray(), self)
                character.initial(self, self.character, self.movie)
                self.is_first_release_left = False
                self.is_first_left = True
                self.character.move(self.current_x, self.current_y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.showFullScreen()
    sys.exit(app.exec_())
