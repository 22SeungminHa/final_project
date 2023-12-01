from pico2d import *

import background_mode
import thema_list_mode


class StageList:
    def __init__(self):
        self.image = [load_image('./resource/stage_' + "%d" % i + '.png') for i in range(1, 9)]
        self.x = (224 + 100, 482 + 100, 740 + 100, 998 + 100, 224 + 100, 482 + 100, 740 + 100, 998 + 100)
        self.y = (264 + 100, 264 + 100, 264 + 100, 264 + 100, 514 + 100, 514 + 100, 514 + 100, 514 + 100)
        self.select = -1
        background_mode.background.change_image('l', thema_list_mode.thema_list.select)

    def update(self):
        pass

    def draw(self):
        for i in range(8):
            if self.select == i:
                self.image[i].draw(self.x[i], 800 - self.y[i], 200 * 1.1, 200 * 1.1)
            else:
                self.image[i].draw(self.x[i], 800 - self.y[i], 200, 200)
            # draw_rectangle(self.x[i] - self.w[i] / 2, 800 - (self.y[i] - self.h[i] / 2), self.x[i] + self.w[i] / 2, 800 - (self.y[i] + self.h[i] / 2))

