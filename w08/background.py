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

class InfiniteBackground(Background):
    def __init__(self, imageName):
        super().__init__(imageName)
        self.boundary = (-sys.maxsize, -sys.maxsize, sys.maxsize, sys.maxsize)
    def update(self):
        if self.target is None:
            return
        tx, ty = self.target.pos

        # quadrant 3
        q3l = round(tx - self.cw / 2) % self.image.w
        q3b = round(ty - self.ch / 2) % self.image.h
        q3w = clamp(0, self.image.w - q3l, self.image.w)
        q3h = clamp(0, self.image.h - q3b, self.image.h)
        self.q3rect = q3l, q3b, q3w, q3h

        # quadrant 2
        q2l = q3l
        q2b = 0
        q2w = q3w
        q2h = self.ch - q3h
        self.q2rect = q2l, q2b, q2w, q2h
        self.q2origin = 0, q3h

        # quadrant 4
        q4l = 0
        q4b = q3b
        q4w = self.cw - q3w
        q4h = q3h
        self.q4rect = q4l, q4b, q4w, q4h
        self.q4origin = q3w, 0

        # quadrant 1
        q1l = 0
        q1b = 0
        q1w = self.cw - q3w
        q1h = self.ch - q3h
        self.q1rect = q1l, q1b, q1w, q1h
        self.q1origin = q3w, q3h

    def draw(self):
        self.image.clip_draw_to_origin(*self.q3rect, 0, 0)
        self.image.clip_draw_to_origin(*self.q2rect, *self.q2origin)
        self.image.clip_draw_to_origin(*self.q4rect, *self.q4origin)
        self.image.clip_draw_to_origin(*self.q1rect, *self.q1origin)

    def to_screen(self, point):
        x, y = point
        tx, ty = self.target.pos
        return self.cw // 2 + x - tx, self.ch // 2 + y - ty

    def translate(self, point):
        x, y = point
        tx, ty = self.target.pos
        dx, dy = x - self.cw // 2, y - self.ch // 2
        return tx + dx, ty + dy

