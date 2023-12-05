from pico2d import *

import background_mode
import clear_state
import stage


class Result:
    def __init__(self, total_score):
        self.win_image = load_image('./resource/result_window.png')
        self.next_image = load_image('./resource/result_next.png')
        self.retry_image = load_image('./resource/result_retry.png')
        self.clear_image = load_image('./resource/result_clear.png')
        self.fail_image = load_image('./resource/result_fail.png')
        self.x = (-170, 0, 170)
        self.retry_size = 1.0
        self.next_size = 1.0
        self.total_score = total_score
        self.font = load_font('BMEULJIRO.otf', 150)
        self.size = [2.5, 3.5, 4.5]

        if stage.target_score[2] < self.total_score and clear_state.clear[stage.thema_num][stage.stage_num] < 3:
            clear_state.clear[stage.thema_num][stage.stage_num] = 3
        elif stage.target_score[1] < self.total_score and clear_state.clear[stage.thema_num][stage.stage_num] < 2:
            clear_state.clear[stage.thema_num][stage.stage_num] = 2
        elif stage.target_score[0] < self.total_score and clear_state.clear[stage.thema_num][stage.stage_num] < 1:
            clear_state.clear[stage.thema_num][stage.stage_num] = 1
        else:
            clear_state.clear[stage.thema_num][stage.stage_num] = 0


    def update(self):
        for i in range(3):
            if self.size[i] > 1.0:
                self.size[i] -= 0.015

    def draw(self):
        self.win_image.draw(711, 400)
        self.retry_image.draw(711 - 157, 400 - 155, 175 * self.retry_size, 181 * self.retry_size)
        self.next_image.draw(711 + 157, 400 - 155, 175 * self.next_size, 181 * self.next_size)

        if self.total_score > 10:
            self.font.draw(711 - 80, 400, f'{int(self.total_score)}', (0, 0, 0))
        else:
            self.font.draw(711 - 40, 400, f'{int(self.total_score)}', (0, 0, 0))

        for i in range(3):
            if self.size[i] <= 2.5 and stage.target_score[i] < self.total_score:
                self.clear_image.draw(711 - 170 + 170 * i, 400 + 190, 174 * self.size[i], 174 * self.size[i])
            elif self.size[i] <= 2.5:
                self.fail_image.draw(711 - 170 + 170 * i, 400 + 190, 174 * self.size[i], 174 * self.size[i])

