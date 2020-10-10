import gfw
from pico2d import *
from gobj import *

class Background:
    def __init__(self, imageName):
        self.imageName = imageName
        self.image = gfw.image.load(res(imageName))
        self.target = None
        cw, ch = get_canvas_width(), get_canvas_height()
        self.win_rect = 0, 0, cw, ch
        self.center = self.image.w // 2, self.image.h // 2
    def set_target(self, target):
        self.target = target
        self.update()
    def draw(self):
        self.image.clip_draw_to_origin(*self.win_rect, 0, 0)
    def update(self):
        if self.target is None:
            return
        tx, ty = self.target.pos
        cw, ch = get_canvas_width(), get_canvas_height()
        sl = round(tx - cw / 2)
        sb = round(ty - ch / 2)
        self.win_rect = sl, sb, cw, ch