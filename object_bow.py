import random

from pico2d import *
import math

r = 1


class Bow:
    def __init__(self):
        self.image = load_image('./resource/bow.png')
        self.x = 275.0
        self.y = -182.5625
        self.size = 0.55
        self.animation = False

    def update(self):
        if self.animation == False:
            self.x -= 1
            self.y = 50 + -0.01 * (self.x - 122.5) ** 2
            if self.x <= 0:
                self.animation = True

    def draw(self):
        self.image.draw(711 + self.x, 400 + self.y, 1466 * self.size, 1866 * self.size)
