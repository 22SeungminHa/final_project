import random

from pico2d import *


class Bow:
    def __init__(self):
        self.image = load_image('./resource/bow.png')
        self.x, self.y = random.randint(711 - 30, 711 + 30), random.randint(400 - 30, 400 + 30)
        self.size = 800
        self.animation = False

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)

