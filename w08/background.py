import gfw
from pico2d import *
from gobj import *

class Background:
    def __init__(self, imageName):
        self.imageName = imageName
        self.image = gfw.image.load(res(imageName))
        self.target = None
        self.cw, self.ch = get_canvas_width(), get_canvas_height()
        self.win_rect = 0, 0, self.cw, self.ch
        self.center = self.image.w // 2, self.image.h // 2
        hw, hh = self.cw // 2, self.    ch // 2
        self.boundary = hw, hh, self.image.w - hw, self.image.h - hh
    def set_target(self, target):
        self.target = target
        self.update()
    def draw(self):
        self.image.clip_draw_to_origin(*self.win_rect, 0, 0)
    def update(self):
        if self.target is None:
            return
        tx, ty = self.target.pos
        sl = round(tx - self.cw / 2)
        sb = round(ty - self.ch / 2)
        self.win_rect = sl, sb, self.cw, self.ch
    def get_boundary(self):
        return self.boundary
    def translate(self, point):
        x, y = point
        l, b, r, t = self.win_rect
        return l + x, b + y
    def to_screen(self, point):
        # return self.cw // 2, self.ch // 2
        x, y = point
        l, b, r, t = self.win_rect
        return x - l, y - b

    # def to_screen(self, point):
    #     hw, hh = self.cw // 2, self.ch // 2
    #     x, y = point

    #     if x > self.image.w - hw:
    #         x = self.cw - (self.image.w - x)
    #     elif x > hw:
    #         x = self.cw // 2

    #     if y > self.image.h - hh:
    #         y = self.ch - (self.image.h - y)
    #     elif y > hh:
    #         y = self.ch // 2

    #     return x, y

class FixedBackground(Background):
    MARGIN_L, MARGIN_B, MARGIN_R, MARGIN_T = 20, 40, 20, 40
    def __init__(self, imageName):
        super().__init__(imageName)
        self.boundary = (
            FixedBackground.MARGIN_L, 
            FixedBackground.MARGIN_B,
            self.image.w - FixedBackground.MARGIN_R, 
            self.image.h - FixedBackground.MARGIN_T
        )
    def update(self):
        if self.target is None:
            return
        tx, ty = self.target.pos
        sl = clamp(0, round(tx - self.cw / 2), self.image.w - self.cw)
        sb = clamp(0, round(ty - self.ch / 2), self.image.h - self.ch)
        self.win_rect = sl, sb, self.cw, self.ch

