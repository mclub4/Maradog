from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from resource_path import *

class bind:
    def __init__ (self):
        # private
        self.__skill_action_time = 1.5
        self.__skill_damage = 40
        self.__skill_range = 920
        self.__skill_cool_time = 3
        self.__is_bind = True

    def change_image(self, skill):
        skill.setVisible(True)
        skill.resize(920, 548)
        skill.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        skill.setAlignment(Qt.AlignCenter)
        self.movie = QMovie("resource/skill_2", QByteArray())
        self.movie.setCacheMode(QMovie.CacheAll)
        skill.setMovie(self.movie)
        self.movie.start()
        self.movie.loopCount()

    def place_skill(self,skill, character):
        character.resize(146, 71)
        character.move(character.pos().x(), 820)
        character.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        character.setAlignment(Qt.AlignCenter)
        self.movie = QMovie("resource/character_attack_2", QByteArray())
        character.move(character.pos().x(), 820)
        self.movie.setCacheMode(QMovie.CacheAll)
        character.setMovie(self.movie)
        self.movie.start()
        self.movie.loopCount()
        skill.move(character.pos().x() + 60, character.pos().y() - 430)

    def getTime(self):
        return self.__skill_action_time

    def getDamage(self):
        return self.__skill_damage

    def IsBind(self):
        return self.__is_bind

    def getRange(self):
        return self.__skill_range

    def getCoolTime(self):
        return self.__skill_cool_time

    def setCoolTime(self):
        pass

    def getIndex(self):
        return 0