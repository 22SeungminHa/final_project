from pico2d import *

import background_mode
import stage
import stage_aim_mode


class Target:
    def __init__(self, mode):
        self.image = load_image('./resource/target.png')
        self.mode = mode
        self.size = 0.45
        self.x, self.y = 0, 0
        if stage.stage_num == 1 or stage.stage_num == 2:
            self.amount = 0.1
        elif stage.stage_num == 5 or stage.stage_num == 6:
            self.amount = 0.2
        else:
            self.amount = 0

    def update(self):
        if self.mode == 'aim':
            stage.move_target()
            if (stage_aim_mode.bow.animation == 'zoom in' or stage_aim_mode.bow.animation == 'zoom out') and self.size < 200 / 360:
                self.size += 0.0005
                background_mode.background.size += 0.0005
                for i in range(len(stage_aim_mode.arrow_mark)):
                    stage_aim_mode.arrow_mark[i].ratio += 0.0005


    def draw(self):
        if self.mode == 'aim':
            self.image.draw(711 + self.x, 400 + self.y, 360 * self.size, 360 * self.size)
        elif self.mode == 'launch':
            self.image.draw(711, 400, 300, 300)
