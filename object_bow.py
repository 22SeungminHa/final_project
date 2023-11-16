import random

from pico2d import *


class Bow:
    def __init__(self):
        self.image = load_image('./resource/bow.png')
        self.x, self.y = random.randint(700, 720), random.randint(390, 410)
        self.size = 800

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, self.size, self.size)

