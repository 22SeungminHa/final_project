from pico2d import *
import os
from enum import Enum

import game_world

mode = ('start_background', 'thema_background')

class Background:
    def __init__(self):
        self.image = load_image("./resource/start_background.png")

        self.bgm = load_wav('./sound/title.wav')
        self.bgm.set_volume(50)
        self.bgm.repeat_play()
        self.on = load_wav('./sound/on.wav')
        self.on.set_volume(50)
        self.click = load_wav('./sound/click.wav')
        self.click.set_volume(50)
        self.wind = load_wav('./sound/wind.wav')
        self.wind.set_volume(50)

        self.size = 1.0
        self.mode = 'ready'

    def draw(self):
        self.image.draw(711, 400, 1422 * self.size, 800 * self.size)

    def change_image(self, t, i):
        if t == 'm':
            self.image = load_image("./resource/" + mode[i] + ".png")
            if self.mode != 'ready':
                print(self.mode)
                self.bgm = load_wav('./sound/title.wav')
                self.bgm.repeat_play()
                self.mode = 'ready'
        elif t == 'l':
            self.image = load_image("./resource/thema_background" + "%d" % (i + 1) + ".png")
            if self.mode != 'ready':
                self.bgm = load_wav('./sound/title.wav')
                self.bgm.repeat_play()
                self.mode = 'ready'
        elif t == 's':
            self.image = load_image("./resource/palace" + "%d" % (i + 1) + ".png")
            if self.mode != 'play':
                self.bgm = load_wav('./sound/play.wav')
                self.bgm.repeat_play()
                self.mode = 'play'
        elif t == 't':
            self.image = load_image("./resource/Tom_Yum_Goong" + "%d" % (i + 1) + ".png")
            self.mode = 'ready'

    def update(self):
        pass
