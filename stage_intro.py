from pico2d import *

import game_framework
import stage_aim_mode

class StageIntro:
    def __init__(self):
        self.image = load_image('./resource/stage_title.png')
        self.x = -475.0
        self.intro_start_time = get_time()
        self.font = load_font('ENCR10B.TTF', 16)


    def update(self):
        self.x += 8.3 * (get_time() - self.intro_start_time - 1) ** 2
        if get_time() - self.intro_start_time >= 2.0:
            game_framework.change_mode(stage_aim_mode)

    def draw(self):
        self.image.draw(self.x, 400)