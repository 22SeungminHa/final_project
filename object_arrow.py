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
        self.font = load_font('BMEULJIRO.otf', 90)
        self.size = 1.0
        self.wait_start_time = 0
        self.angle_v = 0
        self.num = 0
        self.amplitude = 1.2
        self.score_image = load_image('./resource/score.png')
        self.score_y = 400 - 250 + 76

    def update(self):
        self.size -= 0.005
        if self.size < 0.25:
            self.size = 0.25
        self.x += self.vx * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.vy * RUN_SPEED_PPS * game_framework.frame_time
        if self.wait_start_time > 0:
            if self.score_y > 0:
                self.score_y -= 2.5
            if (stage_launch_mode.score == 0 and get_time() - self.wait_start_time >= 0.5) or get_time() - self.wait_start_time >= 1.0:
                game_framework.pop_mode()
                game_framework.push_mode(stage_aim_mode)
            elif self.amplitude < 2:
                self.num += 0.1
                self.amplitude += 0.002
                self.angle_v = math.sin(self.num)
                self.angle += self.angle_v * (math.pi / 180) ** self.amplitude
                self.x -= self.ax - math.cos(self.angle - self.angle_v * (math.pi / 180) ** self.amplitude) * 1030 / 8 - (self.ax - math.cos(self.angle) * 1030 / 8)
                self.y -= self.ax - math.sin(self.angle - self.angle_v * (math.pi / 180) ** self.amplitude) * 1030 / 8 - (self.ax - math.sin(self.angle) * 1030 / 8)

        elif stage_launch_mode.score > 0 and self.x < self.ax - math.cos(self.angle) * 1030 / 8:
            self.vx, self.vy = 0, 0
            self.wait_start_time = get_time()
        elif self.x < -711 + math.cos(self.angle) * 1030 / 8:
            self.wait_start_time = get_time()

    def draw(self):
        self.image.clip_composite_draw(0, 0, 1030, 73, self.angle, 'h', 711 + self.x, 400 + self.y, 1030 * self.size, 73 * self.size)

        if stage_launch_mode.score == 0:
            self.score_image.draw(711, 400 - 250 - self.score_y)
            self.font.draw(711 - 90, 400 - 250 - self.score_y, f'miss', (0, 0, 0))
        else:
            self.score_image.draw(711, 400 - 250 - self.score_y)
            if stage_launch_mode.score == 10:
                self.font.draw(711 - 80, 400 - 250 - self.score_y, f'{stage_launch_mode.score}', (0, 0, 0))
            else:
                self.font.draw(711 - 60, 400 - 250 - self.score_y, f'{stage_launch_mode.score}', (0, 0, 0))




