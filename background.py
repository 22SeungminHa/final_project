from pico2d import *
from enum import Enum

import game_world

mode = ('start_background', 'thema_background')

class Background:
    def __init__(self):
        self.image = load_image("./resource/start_background.png")
        self.size = 1.0

    def draw(self):
        self.image.draw(711, 400, 1422 * self.size, 800 * self.size)

    def change_image(self, t, i):
        if t == 'm':
            self.image = load_image("./resource/" + mode[i] + ".png")
        elif t == 'l':
            self.image = load_image("./resource/thema_background" + "%d" % (i + 1) + ".png")
        elif t == 's':
            self.image = load_image("./resource/palace" + "%d" % (i + 1) + ".png")
        elif t == 't':
            self.image = load_image("./resource/Tom_Yum_Goong" + "%d" % (i + 1) + ".png")

    def update(self):
        pass
