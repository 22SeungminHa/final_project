from pico2d import *

import game_framework
import stage_aim_mode
import stage_launch_mode
import math

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 200.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


class Arrow:
    def __init__(self, x, y):
        self.image = load_image('./resource/arrow.png')
        self.x, self.y = stage_launch_mode.aim_x + 658, stage_launch_mode.aim_y - 594
        self.ax, self.ay = x, y
        self.angle = math.atan2(self.ay - self.y, self.ax - self.x)
        self.vx, self.vy = math.cos(self.angle), math.sin(self.angle)
        self.font = load_font('BMEULJIRO.otf', 70)
        self.size = 1.0
        self.wait_start_time = 0

    def update(self):
        self.size -= 0.005
        if self.size < 0.25:
            self.size = 0.25
        self.x += self.vx * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.vy * RUN_SPEED_PPS * game_framework.frame_time
        if self.wait_start_time > 0:
            if get_time() - self.wait_start_time >= 2.0:
                game_framework.pop_mode()
                game_framework.push_mode(stage_aim_mode)
        elif self.x < self.ax - math.cos(self.angle) * 1030 / 8:
            self.vx, self.vy = 0, 0
            self.wait_start_time = get_time()


    def draw(self):
        self.image.clip_composite_draw(0, 0, 1030, 73, self.angle, 'h', 711 + self.x, 400 + self.y, 1030 * self.size, 73 * self.size)
        if self.wait_start_time > 0:
            self.font.draw(711 + 200, 400, f'{stage_launch_mode.score}', (255, 255, 255))


