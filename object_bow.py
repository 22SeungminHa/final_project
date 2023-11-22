import random

from pico2d import *
import math

r = 1

class Bow:
    def __init__(self):
        self.image = load_image('./resource/bow.png')
        self.coord = (0.0, 0.0)
        self.start = (random.randint(-30, 30), random.randint(-30, 30))
        self.size = 0.5
        self.angle = math.atan2(self.start[1], self.start[0])
        self.value = (math.cos(self.angle) * r, math.sin(self.angle) * r)

    def animation(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.image.draw(711 + self.coord[0], 400 + self.coord[1], 1466 * self.size, 1866 * self.size)