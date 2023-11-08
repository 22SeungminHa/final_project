from pico2d import *

image_names = ('basic', 'wind', 'sheep', 'poop', 'TomYumGoong')

class Stage:
    def __init__(self):
        self.image = [load_image('./resource/stage_' + image_names[i] + '.png') for i in range(5)]
        self.x = (248, 671, 1170, 466, 1031)
        self.y = (320, 348, 292, 618, 618)
        self.w = (340, 346, 296, 298, 314)
        self.h = (322, 218, 332, 236, 294)
        self.select = -1

    def update(self):
        pass

    def draw(self):
        for i in range(5):
            if self.select == i:
                self.image[i].draw(self.x[i], 800 - self.y[i], self.w[i] * 1.1, self.h[i] * 1.1)
            else:
                self.image[i].draw(self.x[i], 800 - self.y[i], self.w[i], self.h[i])
            # draw_rectangle(self.x[i] - self.w[i] / 2, 800 - (self.y[i] - self.h[i] / 2), self.x[i] + self.w[i] / 2, 800 - (self.y[i] + self.h[i] / 2))

