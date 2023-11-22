from pico2d import *


class Background:
    def __init__(self):
        self.palace = []
        self.mode = []
        self.tyg = []
        self.index, self.type = 0, 'm'
        load_image(self)

    def load_image(self):
        for i in range(10):
            self.palace[i] = load_image("./resource/palace" + "%d" % (i + 1) + ".png")
        for i in range(3):
            self.tyg[i] = load_image("./resource/Tom_Yum_Goong" + "%d" % (i + 1) + ".png")
        self.mode.append(load_image("./resource/start_background"))
        self.mode.append(load_image("./resource/stage_background"))

    def update(self):
        pass

    def draw(self, image_type, index):
        if image_type == 'm':
            self.mode[index].draw(711, 400, 1422, 800)
        elif image_type == 'p':
            self.palace[index].draw(711, 400, 1422, 800)
        elif image_type == 't':
            self.tyg[index].draw(711, 400, 1422, 800)