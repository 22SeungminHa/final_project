from pico2d import *


class Stage1Background:
    def __init__(self):
        self.image = load_image('./resource/palace7.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(711, 400, 1422, 800)

