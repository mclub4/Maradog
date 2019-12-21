from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from resource_path import *
#import skills.skill_crossing as sk
import skills.skill_crossing as crossing
import initial

def skill_activate(self, event, monster_list, monster_attribute, character):
    for key in skill_dic.keys():
        if event.key() == key and self.start:
            tmp_skill = skill_dic[key]
            if self.using_skill == False and tmp_skill.getCoolTime() > 0:
                self.using_skill = True

                # monster processing
                for i in range(len(monster_list)):
                    skill_range = tmp_skill.getRange()
                    skill_damage = tmp_skill.getDamage()
                    if skill_range > monster_list[i].pos().x() - character.pos().x() and character.pos().x() < monster_list[i].pos().x():
                        monster_attribute[i].hp -= skill_damage
                        print(monster_attribute[i].hp)


                def timer_func(count):
                    # print('Timer:', count)
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
                tmp_skill.setCoolTime()
                index = tmp_skill.getIndex()
                self.cooltime[index].setText(str(self.cooltime_value[index].getCoolTime()))
                if(tmp_skill.getCoolTime()<=0):
                    self.disabled_image = QPixmap("resource/skill_icon_" + str(index+1) + "_disabled.png")
                    self.disabled_image = self.disabled_image.scaled(100, 100)
                    self.skillicon[index].setPixmap(self.disabled_image)
                if(key == Qt.Key_L):
                    self.is_buff.setVisible(True)
                    self.show_buff.setVisible(True)
                    tmp_skill.buff += 1
                    self.show_buff.setText(str(tmp_skill.buff))
                start_timer(timer_func, tmp_skill.getTime())

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
