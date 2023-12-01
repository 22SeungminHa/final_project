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
        self.score_image = load_image('./resource/score.png')
        self.font = load_font('BMEULJIRO.otf', 90)
        self.mark_image = load_image('./resource/mark.png')

        self.x, self.y = stage_launch_mode.aim_x + 658, stage_launch_mode.aim_y - 594
        self.ax, self.ay = x, y
        self.angle = math.atan2(self.ay - self.y, self.ax - self.x)
        self.vx, self.vy = math.cos(self.angle), math.sin(self.angle)
        self.size = 1.0

        self.angle_v = 0
        self.num = 0
        self.amplitude = 1.2

        self.wait_start_time = 0
        self.score_y = 400 - 250 + 76

    def update(self):
        # 화살 날아가기
        if self.size > 0.25:
            self.size -= 0.005
        self.x += self.vx * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.vy * RUN_SPEED_PPS * game_framework.frame_time

        # 과녁에 맞았을 때
        if self.wait_start_time > 0:
            # 점수판 애니메이션
            if self.score_y > 0:
                self.score_y -= 2.5

            # 모든 애니메이션이 끝나고 에임모드로 돌아가기
            if (stage_launch_mode.score == 0 and get_time() - self.wait_start_time >= 0.5) or get_time() - self.wait_start_time >= 1.0:
                game_framework.pop_mode()
                game_framework.push_mode(stage_aim_mode)

            # 화살 튕기는 애니메이션
            elif self.amplitude < 2:
                self.num += 0.1
                self.amplitude += 0.002
                self.angle_v = math.sin(self.num)
                self.angle += self.angle_v * (math.pi / 180) ** self.amplitude
                self.x -= self.ax - math.cos(self.angle - self.angle_v * (math.pi / 180) ** self.amplitude) * 1030 / 8 - (self.ax - math.cos(self.angle) * 1030 / 8)
                self.y -= self.ax - math.sin(self.angle - self.angle_v * (math.pi / 180) ** self.amplitude) * 1030 / 8 - (self.ax - math.sin(self.angle) * 1030 / 8)

        # 화살이 목표지점에 도달했을 때부터 시간 재기
        elif (stage_launch_mode.score > 0 and self.x < self.ax - math.cos(self.angle) * 1030 / 8) or self.x < -711 + math.cos(self.angle) * 1030 / 8:
            self.vx, self.vy = 0, 0
            self.wait_start_time = get_time()

    def draw(self):
        if stage_launch_mode.score == 0:
            self.mark_image.draw(711 + self.ax, 400 + self.ay, 431 / 2, 469 / 2)

        # 화살
        self.image.clip_composite_draw(0, 0, 1030, 73, self.angle, 'h', 711 + self.x, 400 + self.y, 1030 * self.size, 73 * self.size)

        # miss 출력
        if stage_launch_mode.score == 0:
            self.score_image.draw(711, 400 - 250 - self.score_y)
            self.font.draw(711 - 90, 400 - 250 - self.score_y, f'miss', (0, 0, 0))

        # 점수 출력
        else:
            self.score_image.draw(711, 400 - 250 - self.score_y)
            if stage_launch_mode.score == 10:
                self.font.draw(711 - 80, 400 - 250 - self.score_y, f'{stage_launch_mode.score}', (0, 0, 0))
            else:
                self.font.draw(711 - 60, 400 - 250 - self.score_y, f'{stage_launch_mode.score}', (0, 0, 0))




