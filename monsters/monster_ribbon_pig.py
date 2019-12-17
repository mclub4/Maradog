from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class RibbonPig:
    def __init__(self):
        self.hp = 100
        self.__score = 20
        self.__gold = 30

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp

    def get_score(self):
        return self.__score
