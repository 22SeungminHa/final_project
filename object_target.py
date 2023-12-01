from pico2d import *

import background_mode
import stage_aim_mode


class Target:
    def __init__(self, mode):
        self.image = load_image('./resource/target.png')
        self.mode = mode
        self.size = 0.5

    def update(self):
        if self.mode == 'aim' and (stage_aim_mode.bow.animation == 'zoom in' or stage_aim_mode.bow.animation == 'zoom out') and self.size < 200 / 360:
            self.size += 0.001
            background_mode.background.size += 0.001


    def draw(self):
        if self.mode == 'aim':
            self.image.draw(711, 400, 360 * self.size, 360 * self.size)
        elif self.mode == 'launch':
            self.image.draw(711, 400, 300, 300)
