import math

import stage_aim_mode
import stage_list_mode
import thema_list
import thema_list_mode

thema_num = -1
stage_num = -1

def init():
    global thema_num
    global stage_num

    thema_num = thema_list_mode.thema_list.select
    stage_num = stage_list_mode.stage_list.select


def stage_update():
    match stage_num + 1:
        case 2 | 6:
            if -75 > stage_aim_mode.target.x or stage_aim_mode.target.x > 75:
                stage_aim_mode.target.amount = -stage_aim_mode.target.amount

            stage_aim_mode.target.x += stage_aim_mode.target.amount
            for i in range(len(stage_aim_mode.arrow_mark)):
                stage_aim_mode.arrow_mark[i].mx += stage_aim_mode.target.amount

        case 3 | 7:
            if -75 > stage_aim_mode.target.y or stage_aim_mode.target.y > 75:
                stage_aim_mode.target.amount = -stage_aim_mode.target.amount

            stage_aim_mode.target.y += stage_aim_mode.target.amount
            for i in range(len(stage_aim_mode.arrow_mark)):
                stage_aim_mode.arrow_mark[i].my += stage_aim_mode.target.amount

        case 4 | 8:
            stage_aim_mode.target.amount += 0.002
            for i in range(len(stage_aim_mode.arrow_mark)):
                stage_aim_mode.arrow_mark[i].mx += math.cos(stage_aim_mode.target.amount) * 75 - stage_aim_mode.target.x
                stage_aim_mode.arrow_mark[i].my += math.sin(stage_aim_mode.target.amount) * 75 - stage_aim_mode.target.y

            stage_aim_mode.target.x = math.cos(stage_aim_mode.target.amount) * 75
            stage_aim_mode.target.y = math.sin(stage_aim_mode.target.amount) * 75
