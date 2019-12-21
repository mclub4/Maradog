from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Skill_Structure:
    def __init__ (self):
        # private
        self.skill_action_time
        self.skill_damage
        self.skill_range
        self.skill_cool_time
        self.skill_original_time
        self.skill_index
        self.skill_image
        self.skill_position_x
        self.skill_position_y

    def change_image(self, skill):
        import resource_path as rp
        skill.setVisible(True)
        skill.resize(694, 400)
        skill.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        skill.setAlignment(Qt.AlignCenter)
        self.movie = QMovie(self.skill_image, QByteArray())
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
        skill.move(character.pos().x() - self.skill_position_x, character.pos().y() + self.skill_position_y)

    def getTime(self):
        return self.skill_action_time

    def getDamage(self):
        return self.skill_damage

    def getRange(self):
        return self.skill_range

    def getCoolTime(self):
        return self.skill_cool_time

    def setCoolTime(self):
        self.skill_cool_time -= 1

    def backCoolTime(self):
        self.skill_cool_time = self.skill_original_time

    def getIndex(self):
        return self.skill_index