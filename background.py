from pico2d import *


class Background:

    def __init__(self):
        self.image = None
        load_image(self)

    def load_image(self):
        if self.image == None:
            self.image = {}
            for i in range(10):
                self.image[i] = load_image("./resource/palace" + " (%d)" % i + ".png")

    def update(self):
        pass

    def draw(self):
        self.image.draw(711, 400, 1422, 800)

