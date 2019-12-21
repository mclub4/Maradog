from PyQt5.QtCore import *
import skills.skill_crossing as crossing
import skills.skill_bind as bind
from PyQt5.QtCore import *
import skills.skill_crossing as crossing
import skills.skill_bind as bind
import skills.skill_buff as buff
import skills.skill_basic as basic
import skills.skill_critical as critical

ch_stand = "resource/character_stand.gif"
ch_walk = "resource/character_walk.gif"
ch_attack1 = "resource/character_attack_1.gif"
ch_attack2 = "resource/character_attack_2.gif"

protect_1 = "resource/protect_1.gif"
protect_1_dead = "resource/protect_1_dead.gif"
protect_2 = "resource/protect_2.gif"
protect_2_dead = "resource/protect_2_dead.gif"

slime = "resource/monster_slime.gif"
orange_mushroom = "resource/monster_orange_mushroom.gif"
ribbon_pig = "resource/monster_ribbon_pig.gif"
fox = "resource/monster_fox.gif"
bird = "resource/monster_bird.gif"

background = ['resource/back_ground_4.png']

skill_1 = "resource/skill_1.gif"
skill_2 = "resource/skill_2.gif"
skill_3 = "resource/skill_3.gif"
skill_4 = "resource/skill_4.gif"
skill_5 = "resource/skill_5.gif"

skill_obj_1 = crossing.crossing()
skill_obj_2 = bind.bind()
skill_obj_3 = buff.buff()
skill_obj_4 = critical.critical()
skill_obj_5 = basic.basic()

skill_dic = {Qt.Key_J : skill_obj_1, Qt.Key_K : skill_obj_2, Qt.Key_L : skill_obj_3, Qt.Key_I : skill_obj_4, Qt.Key_O : skill_obj_5}



machine_1 = "resource/machine.png"
machine_2 = "resource/machine2.gif"

