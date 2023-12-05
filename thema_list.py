from pico2d import *

import background_mode
import clear_state

image_names = ('basic', 'wind', 'sheep', 'poop', 'TomYumGoong')

class ThemaList:
    def __init__(self):
        self.image = [load_image('./resource/thema_' + image_names[i] + '.png') for i in range(5)]
        self.crown_image = load_image('./resource/crown.png')

        self.x = (161 + 150, 566 + 150, 959 + 150, 341 + 150, 746 + 150)
        self.y = (223 + 150, 223 + 150, 223 + 150, 471 + 150, 471 + 150)
        self.select = -1
        background_mode.background.change_image('m', 1)

    def update(self):
        pass

    def draw(self):
        for i in range(5):
            cnt = 0
            for j in range(8):
                if clear_state.clear[i][j] == 3:
                    cnt += 1

            if self.select == i:
                self.image[i].draw(self.x[i], 800 - self.y[i], 300 * 1.1, 300 * 1.1)
                if cnt == 8:
                    self.crown_image.draw(self.x[i], 800 - self.y[i] + 100 * 1.1, 105 * 1.1, 80 * 1.1)
            else:
                self.image[i].draw(self.x[i], 800 - self.y[i], 300, 300)
                if cnt == 8:
                    self.crown_image.draw(self.x[i], 800 - self.y[i] + 100)
            # draw_rectangle(self.x[i] - self.w[i] / 2, 800 - (self.y[i] - self.h[i] / 2), self.x[i] + self.w[i] / 2, 800 - (self.y[i] + self.h[i] / 2))

