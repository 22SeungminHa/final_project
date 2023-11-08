from pico2d import *


class Title:
    def __init__(self):
        self.image = load_image('./resource/start_title.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(711, 400, 425, 161)
