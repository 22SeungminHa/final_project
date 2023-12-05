from pico2d import *

import background_mode
import game_framework
import stage


# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 100.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

animation = False

class StageTitle:
    def __init__(self):
        self.image = load_image('./resource/stage_title.png')
        self.x = -475.0
        self.vx = 0.0
        self.font = load_font('BMEULJIRO.otf', 75)
        background_mode.background.change_image('s', stage.thema_num)


    def update(self):
        global animation

        self.vx += 0.005
        self.x += RUN_SPEED_PPS * game_framework.frame_time * (self.vx - 1.55) ** 2
        if self.x >= 1422 + 943 / 2:
            animation = True
            game_framework.pop_mode()


    def draw(self):
        if animation == False:
            self.image.draw(self.x, 400, 943 / 2, 342 / 2)
            self.font.draw(self.x - 120, 400, f'stage {stage.stage_num + 1}', (0, 0, 0))
