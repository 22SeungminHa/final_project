from pico2d import *


class Arrow:
    def __init__(self):
        self.image = load_image('./resource/arrow.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(711, 400)

