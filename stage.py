from pico2d import *

image_names = ['basic', 'wind', 'sheep', 'poop', 'TomYumGoong']

class Stage:
    def __init__(self):
        self.image = [load_image('./resource/stage_' + image_names[i] + '.png') for i in range(5)]

    def update(self):
        pass

    def draw(self):
        self.image[0].draw(248, 800 - 320)
        self.image[1].draw(671, 800 - 348)
        self.image[2].draw(1170, 800 - 292)
        self.image[3].draw(466, 800 - 618)
        self.image[4].draw(1031, 800 - 618)

