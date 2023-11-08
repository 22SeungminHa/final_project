from pico2d import *


class StageBackground:
    def __init__(self):
        self.image = load_image('./resource/start_background.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(711, 400, 1422, 800)
