from pico2d import *
from enum import Enum

import game_world

image_name = ('retry', 'back', 'help')

class Pause:
    def __init__(self):
        self.image = [load_image("./resource/" + image_name[i] + ".png") for i in range(3)]
        self.size = [1.0, 1.0, 1.0]

    def draw(self):
        for i in range(3):
            self.image[i].draw(711, 400 + 125 - 125 * i, 300 * self.size[i], 100 * self.size[i])

    def update(self):
        pass
