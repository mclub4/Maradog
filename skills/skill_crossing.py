from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class crossing:
    def __init__ (self):
        # private
        self.__skill_action_time = 0.75
        self.__skill_damage = 50
        self.__skill_range = 700
        self.__skill_cool_time = 3

    def change_image(self, skill):
        import resource_path as rp
        skill.setVisible(True)
        skill.resize(694, 400)
        skill.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        skill.setAlignment(Qt.AlignCenter)
        self.movie = QMovie(rp.skill_1, QByteArray())
        self.movie.setCacheMode(QMovie.CacheAll)
        skill.setMovie(self.movie)
        self.movie.start()
        self.movie.loopCount()

    def place_skill(self,skill, character):
        import resource_path as rp
        character.resize(146, 71)
        character.move(character.pos().x(), 820)
        character.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        character.setAlignment(Qt.AlignCenter)
        self.movie = QMovie(rp.ch_attack2, QByteArray())
        character.move(character.pos().x(), 820)
        self.movie.setCacheMode(QMovie.CacheAll)
        character.setMovie(self.movie)
        self.movie.start()
        self.movie.loopCount()
        skill.move(character.pos().x() + 50, character.pos().y() - 250)

    def getTime(self):
        return self.__skill_action_time

    def getDamage(self):
        return self.__skill_damage

    def getRange(self):
        return self.__skill_range

    def getCoolTime(self):
        return self.__skill_cool_time