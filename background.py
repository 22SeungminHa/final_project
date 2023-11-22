from pico2d import *
from enum import Enum

import game_world


class Background:
    def __init__(self, t, i):
        self.palace = {}
        self.mode = {}
        self.tyg = {}
        self.type = t
        self.index = i

        self.mode[0] = load_image("./resource/start_background.png")
        self.mode[1] = load_image("./resource/stage_background.png")
        for i in range(10):
            self.palace[i] = load_image("./resource/palace" + "%d" % (i + 1) + ".png")
        for i in range(3):
            self.tyg[i] = load_image("./resource/Tom_Yum_Goong" + "%d" % (i + 1) + ".png")

    def draw(self):
        if self.type == 'm':
            self.mode[self.index].draw(711, 400, 1422, 800)
        elif self.type == 's':
            self.palace[self.index].draw(711, 400, 1422, 800)
        elif self.type == 't':
            self.tyg[self.index].draw(711, 400, 1422, 800)

    def change_image(self, t, i):
        self.type = t
        self.index = i

    def update(self):
        pass
