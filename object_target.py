from pico2d import *


class Target:
    def __init__(self, mode):
        self.image = load_image('./resource/target.png')
        self.mode = mode
        self.size = 1.0

    def update(self):
        pass

    def draw(self):
        if self.mode == 'aim':
            self.image.draw(711, 400, 200, 200)
        elif self.mode == 'launch':
            self.image.draw(711, 400, 300, 300)
