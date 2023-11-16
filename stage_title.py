from pico2d import *

import game_framework
import stage_aim_mode
import stage_list_mode


class StageTitle:
    def __init__(self):
        self.image = load_image('./resource/stage_title.png')
        self.x = -475.0
        self.intro_start_time = get_time()
        self.font = load_font('BMEULJIRO.otf', 120)

    def update(self):
        self.x += 10.0 * (get_time() - self.intro_start_time - 1) ** 2
        if get_time() - self.intro_start_time >= 2.5:
            game_framework.change_mode(stage_aim_mode)

    def draw(self):
        self.image.draw(self.x, 400)
        self.font.draw(self.x - 160, 400, f'stage{stage_list_mode.stage_list.select + 1}', (0, 0, 0))