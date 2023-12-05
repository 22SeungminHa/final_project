import math
import random

import game_world
import stage_aim_mode
import stage_list_mode
import thema_list
import thema_list_mode
from obstacle_poop import Poop
from obstacle_sheep import Sheep

thema_num = -1
stage_num = -1
target_score = []
wind_angle = 0
poop_timer = 0
sheep = None
poop = None

def init_wind():
    global wind_angle

    # 바람
    if thema_num == 1 or thema_num == 4:
        wind_angle = math.atan2(random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0))
    else:
        wind_angle = 0


def init():
    global thema_num
    global stage_num
    global target_score
    global poop_timer

    thema_num = thema_list_mode.thema_list.select
    stage_num = stage_list_mode.stage_list.select

    if thema_num >= 3:
        poop_timer = random.randint(500, 1000)

    if stage_num < 4:
        target_score.append(22)
        target_score.append(30)
        target_score.append(33)
    else:
        target_score.append(25)
        target_score.append(33)
        target_score.append(36)

def move_target():
    match stage_num + 1:
        case 2 | 6:
            if -100 > stage_aim_mode.target.x or stage_aim_mode.target.x > 100:
                stage_aim_mode.target.amount = -stage_aim_mode.target.amount

            stage_aim_mode.target.x += stage_aim_mode.target.amount
            for i in range(len(stage_aim_mode.arrow_mark)):
                stage_aim_mode.arrow_mark[i].mx += stage_aim_mode.target.amount

        case 3 | 7:
            if -100 > stage_aim_mode.target.y or stage_aim_mode.target.y > 100:
                stage_aim_mode.target.amount = -stage_aim_mode.target.amount

            stage_aim_mode.target.y += stage_aim_mode.target.amount
            for i in range(len(stage_aim_mode.arrow_mark)):
                stage_aim_mode.arrow_mark[i].my += stage_aim_mode.target.amount

        case 4:
            stage_aim_mode.target.amount += 0.002
        case 8:
            stage_aim_mode.target.amount += 0.004

    if stage_num + 1 == 4 or stage_num + 1 == 8:
        for i in range(len(stage_aim_mode.arrow_mark)):
            stage_aim_mode.arrow_mark[i].mx += math.cos(stage_aim_mode.target.amount) * 100 - stage_aim_mode.target.x
            stage_aim_mode.arrow_mark[i].my += math.sin(stage_aim_mode.target.amount) * 100 - stage_aim_mode.target.y

        stage_aim_mode.target.x = math.cos(stage_aim_mode.target.amount) * 100
        stage_aim_mode.target.y = math.sin(stage_aim_mode.target.amount) * 100


def update():
    global poop_timer
    global poop, sheep

    # 장애물
    # 양
    if sheep == None and (thema_num == 2 or thema_num == 4) and random.randint(1, 1000) == 1:
        sheep = Sheep()
        game_world.add_object(sheep, 3)

    # 똥
    if thema_num >= 3:
        poop_timer -= 1
        if poop_timer == 0:
            poop = Poop()
            game_world.add_object(poop, 3)
