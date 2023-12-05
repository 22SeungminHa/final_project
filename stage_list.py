from pico2d import *

import background_mode
import clear_state
import stage
import thema_list_mode


class StageList:
    def __init__(self):
        self.image = [load_image('./resource/stage_' + "%d" % i + '.png') for i in range(1, 9)]
        self.star_true_image = load_image('./resource/star_true.png')
        self.star_fail_image = load_image('./resource/star_fail.png')
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
                for j in range(3):
                    if clear_state.clear[thema_list_mode.thema_list.select][i] > j:
                        self.star_true_image.draw(self.x[i] - 50 * 1.1 + 50 * j, 800 - self.y[i] - 50 * 1.1, 75 * 1.1, 73 * 1.1)
                    else:
                        self.star_fail_image.draw(self.x[i] - 50 * 1.1 + 50 * j * 1.1, 800 - self.y[i] - 50 * 1.1, 75 * 1.1, 73 * 1.1)
            else:
                self.image[i].draw(self.x[i], 800 - self.y[i], 200, 200)
                for j in range(3):
                    if clear_state.clear[thema_list_mode.thema_list.select][i] > j:
                        self.star_true_image.draw(self.x[i] - 50 + 50 * j, 800 - self.y[i] - 50)
                    else:
                        self.star_fail_image.draw(self.x[i] - 50 + 50 * j, 800 - self.y[i] - 50)
            # draw_rectangle(self.x[i] - self.w[i] / 2, 800 - (self.y[i] - self.h[i] / 2), self.x[i] + self.w[i] / 2, 800 - (self.y[i] + self.h[i] / 2))

