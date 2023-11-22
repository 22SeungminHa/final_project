from pico2d import *


class Target:
    def __init__(self):
        self.image = load_image('./resource/target.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(711, 400, 200, 200)

