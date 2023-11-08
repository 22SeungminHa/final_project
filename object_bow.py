from pico2d import *


class Bow:
    def __init__(self):
        self.image = load_image('./resource/bow.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(711, 400, 800, 800)

