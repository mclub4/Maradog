from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import skills.Skill_Structure as sk

class critical(sk.Skill_Structure):
    def __init__ (self):
        # private
        import resource_path as rp
        self.skill_action_time = 0.8
        self.skill_damage = 300
        self.skill_range = 600
        self.skill_cool_time = 2
        self.skill_original_time = 2
        self.skill_image = rp.skill_4
        self.skill_position_x = 35
        self.skill_position_y = -150
        self.skill_index = 3

