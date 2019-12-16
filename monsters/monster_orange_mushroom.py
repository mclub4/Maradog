from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from monsters import initial_monster


class OrangeMushroom:
    def __init__(self):
        self.hp = 120
        self.__score = 20
        self.__gold = 40

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp

    def get_score(self):
        return self.__score