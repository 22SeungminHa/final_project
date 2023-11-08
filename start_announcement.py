from pico2d import *


class Announcement:
    def __init__(self):
        self.image = load_image('./resource/start_announcement.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(711, 280, 682, 60)
