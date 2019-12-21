from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from resource_path import *
import skills.Skill_Structure as sk

class bind(sk.Skill_Structure):
    def __init__ (self):
        # private
        import resource_path as rp
        self.skill_action_time = 1.5
        self.skill_damage = 40
        self.skill_range = 920
        self.skill_cool_time = 3
        self.skill_original_time = 3
        self.skill_image = rp.skill_2
        self.skill_position_x = 60
        self.skill_position_y = -430
        self.skill_index = 1
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
