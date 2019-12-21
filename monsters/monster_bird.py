from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from monsters import initial_monster


class Bird:
    def __init__(self):
        self.hp = 180
        self.__score = 20
        self.__gold = 200
        self.killed = False
        self.original_hp = 120

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp

    def get_score(self):
        return self.__score

    def back_hp(self):
        self.hp = self.original_hp

    def get_gold(self):
        return self.__gold
