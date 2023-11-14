from pico2d import *


class StartTitle:
    def __init__(self):
        self.image = load_image('./resource/start_background.png')

        self.title_image = load_image('./resource/start_title.png')
        self.announcement_image = load_image('./resource/start_announcement.png')
        self.title_y = -100
        self.announcement_ani = 0

    def update(self):
        if self.title_y < 400:
            self.title_y += 1
        else:
            self.announcement_ani += 1
            if self.announcement_ani == 100:
                self.announcement_ani = -100

    def draw(self):
        self.image.draw(711, 400, 1422, 800)
        self.title_image.draw(711, self.title_y, 425, 161)
        if self.announcement_ani > 0:
            self.announcement_image.draw(711, 280, 682, 60)