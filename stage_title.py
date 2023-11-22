from pico2d import *

import background_mode
import game_framework
import game_world
import stage
import stage_aim_mode
import stage_list_mode
from object_bow import Bow

# Boy Run Speed
PIXEL_PER_METER = (158.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

class StageTitle:
    def __init__(self):
        self.image = load_image('./resource/stage_title.png')
        self.x = -475.0
        self.intro_start_time = get_time()
        self.font = load_font('BMEULJIRO.otf', 120)
        background_mode.background.change_image('s', stage.num)

    def update(self):
        self.x += RUN_SPEED_PPS * game_framework.frame_time * (get_time() - self.intro_start_time - 1) ** 2
        if get_time() - self.intro_start_time >= 2.5:
            game_framework.pop_mode()
            stage_aim_mode.bow = Bow()
            game_world.add_object(stage_aim_mode.bow, 1)

    def draw(self):
        self.image.draw(self.x, 400)
        self.font.draw(self.x - 190, 400, f'stage {stage.num + 1:02d}', (0, 0, 0))