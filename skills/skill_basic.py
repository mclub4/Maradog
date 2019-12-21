from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import skills.Skill_Structure as sk

class basic(sk.Skill_Structure):
    def __init__ (self):
        # private
        import resource_path as rp
        self.skill_action_time = 0.5
        self.skill_damage = 10
        self.skill_range = 380
        self.skill_cool_time = 10
        self.skill_original_time = 10
        self.skill_image = rp.skill_5
        self.skill_position_x = -70
        self.skill_position_y = -190
        self.skill_index = 4
