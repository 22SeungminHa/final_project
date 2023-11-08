from pico2d import *


class StageListBackground:
    def __init__(self):
        self.image = load_image('./resource/stage_background.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(711, 400, 1422, 800)

