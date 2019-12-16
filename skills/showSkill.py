from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from resource_path import *
#import skills.skill_crossing as sk
import skills.skill_crossing as crossing

def skill_activate(self, event):
    for key in skill_dic.keys():
        if event.key() == key and self.start:
            tmp_skill = skill_dic[key]
            if self.using_skill == False:
                self.using_skill = True
                def timer_func(count):
                    print('Timer:', count)
                    if count >= tmp_skill.getTime():
                        self.using_skill = False
                        self.skill.setVisible(False)
                        self.character.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                        self.character.setAlignment(Qt.AlignCenter)
                        self.character.resize(106, 75)
                        self.character.move(self.character.pos().x(), 820)
                        self.movie = QMovie(ch_stand, QByteArray(), self)
                        self.movie.setCacheMode(QMovie.CacheAll)
                        self.character.setMovie(self.movie)
                        self.movie.start()
                        self.movie.loopCount()
                tmp_skill.change_image(self.skill)
                tmp_skill.place_skill(self.skill, self.character)
                start_timer(timer_func, tmp_skill.getTime())

    # elif event.key() == Qt.Key_E :
    #     # global check
    #     if check == True:
    #         check = False
    #         def timer_func(count):
    #             global check
    #             # print('Timer:', count)
    #             if count >= 1.3:
    #                 check = True
    #                 self.skill.setVisible(False)
    #
    #         self.movie = QMovie(ch_attack1, QByteArray(), self)
    #         ch.initial(self, self.character, self.movie)
    #         self.skill.setVisible(True)
    #         self.skill.resize(872, 242)
    #         self.skill.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    #         self.skill.setAlignment(Qt.AlignCenter)
    #         self.movie = QMovie('resource/skill_bind.gif', QByteArray(), self)
    #         self.movie.setCacheMode(QMovie.CacheAll)
    #         self.skill.setMovie(self.movie)
    #         self.movie.start()
    #         self.movie.loopCount()
    #         self.skill.move(self.character.pos().x() + 50, self.character.pos().y() - 80)
    #         start_timer(timer_func, 1.3)
        # loop = QEventLoop()
        # QTimer.singleShot(10000, loop.quit)
        # loop.exec_()

def start_timer(slot, count=1, interval=100):
    counter = 0
    def handler():
        nonlocal counter
        counter += 0.1
        slot(counter)
        if counter >= count:
            timer.stop()
            timer.deleteLater()
    timer = QTimer()
    timer.timeout.connect(handler)
    timer.start(interval)


# def skill_activate(self, event):
#     if event.key() == Qt.Key_Q:
#         start_timer()
#         self.skill.setVisible(True)
#         self.skill.resize(872, 242)
#         self.skill.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#         self.skill.setAlignment(Qt.AlignCenter)
#         self.movie = QMovie('resource/skill_6.gif', QByteArray(), self)
#         self.movie.setCacheMode(QMovie.CacheAll)
#         self.skill.setMovie(self.movie)
#         self.movie.start()
#         self.skill.move(self.character.pos().x()+50, self.character.pos().y()-80)
#
#
# def start_timer():
#     current_timer = QTimer()
#     print('launch')
#     current_timer.timeout.connect(print_hello)
#     current_timer.setSingleShot(True)
#     current_timer.start(3000)
#     print('reach end')
#
#
# def print_hello():
#     print('hi')