from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import skills.Skill_Structure as sk

class buff(sk.Skill_Structure):
    def __init__ (self):
        import resource_path as rp
        self.skill_action_time = 1.2
        self.skill_damage = 0
        self.skill_range = 0
        self.skill_cool_time = 1
        self.skill_original_time = 1
        self.skill_index = 2
        self.buff = 0
        self.skill_image = rp.skill_3
        self.skill_width = 694
        self.skill_height = 400

    def place_skill(self,skill, character):
        import resource_path as rp
        character.resize(106, 75)
        character.move(character.pos().x(), 820)
        character.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        character.setAlignment(Qt.AlignCenter)
        self.movie = QMovie(rp.ch_stand, QByteArray())
        character.move(character.pos().x(), 820)
        self.movie.setCacheMode(QMovie.CacheAll)
        character.setMovie(self.movie)
        self.movie.start()
        self.movie.loopCount()
        skill.move(character.pos().x() - 300, character.pos().y() - 320)