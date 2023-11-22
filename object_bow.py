import random

from pico2d import *
import math

r = 1


class Bow:
    def __init__(self):
        self.image = load_image('./resource/bow.png')
        self.x = 275.0
        self.y = -182.5625
        self.size = 0.7335
        self.animation = 'start'
        self.mx, my = 0, 0

    def update(self):
        if self.animation == 'start':
            self.size -= 0.0005
            self.x -= 0.75
            self.y = 50 + -0.01 * (self.x - 122.5) ** 2
            if self.x <= 0:
                self.animation = None
        elif self.animation == 'zoom in':
            if self.size < 0.65:
                self.size += 0.0005


    def draw(self):
        self.image.draw(711 + self.x, 400 + self.y, 1466 * self.size, 1866 * self.size)
