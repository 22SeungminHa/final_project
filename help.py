from pico2d import *
from enum import Enum

import game_world


class Help:
    def __init__(self):
        self.image = load_image("./resource/advice.png")

    def draw(self):
        self.image.draw(711, 400)

    def update(self):
        pass
