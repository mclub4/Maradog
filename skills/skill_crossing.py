from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import skills.Skill_Structure as sk

class crossing(sk.Skill_Structure):
    def __init__ (self):
        # private
        import resource_path as rp
        self.skill_action_time = 0.75
        self.skill_damage = 50
        self.skill_range = 700
        self.skill_cool_time = 3
        self.skill_original_time = 3
        self.skill_image = rp.skill_1
        self.skill_position_x = 50
        self.skill_position_y = -250
        self.skill_index = 0
