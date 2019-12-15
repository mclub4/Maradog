from PyQt5.QtCore import *
import skills.skill_crossing as crossing
import skills.skill_bind as bind

ch_stand = "resource/character_stand.gif"
ch_walk = "resource/character_walk.gif"
ch_attack1 = "resource/character_attack_1.gif"
ch_attack2 = "resource/character_attack_2.gif"

protect_1 = "resource/protect_1.gif"
protect_1_dead = "resource/protect_1_dead.gif"
protect_2 = "resource/protect_2.gif"
protect_2_dead = "resource/protect_2_dead.gif"

slime = "resource/monster_slime.gif"

background = ['resource/back_ground_4.png']

skill_1 = "resource/skill_1.gif"
skill_2 = "resource/skill_2.gif"
skill_obj_1 = crossing.crossing()
skill_obj_2 = bind.bind()
skill_dic = {Qt.Key_Q : skill_obj_1, Qt.Key_E : skill_obj_2}


machine_1 = "resource/machine.png"
machine_2 = "resource/machine2.gif"

