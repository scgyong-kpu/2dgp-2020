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
    def __init__(self, imageName, width=0, height=0):
        super().__init__(imageName)
        self.boundary = (-sys.maxsize, -sys.maxsize, sys.maxsize, sys.maxsize)
        self.fix_x, self.fix_y = self.cw // 2, self.ch // 2
        if width == 0:
            width = self.image.w
        if height == 0:
            height = self.image.h
        self.w, self.h = width, height
    def set_fixed_pos(self, x, y):
        self.fix_x, self.fix_y = x, y
    def update(self):
        if self.target is None:
            return
        tx, ty = self.target.pos

        # quadrant 3
        q3l = round(tx - self.fix_x) % self.image.w
        q3b = round(ty - self.fix_y) % self.image.h
        q3w = clamp(0, self.image.w - q3l, self.image.w)
        q3h = clamp(0, self.image.h - q3b, self.image.h)
        self.q3rect = q3l, q3b, q3w, q3h
        # quadrant 2
        self.q2rect = q3l, 0, q3w, self.ch - q3h
        self.q2origin = 0, q3h
        # quadrant 4
        self.q4rect = 0, q3b, self.cw - q3w, q3h
        self.q4origin = q3w, 0
        # quadrant 1
        self.q1rect = 0, 0, self.cw - q3w, self.ch - q3h
        self.q1origin = q3w, q3h

    def draw(self):
        self.image.clip_draw_to_origin(*self.q3rect, 0, 0)
        self.image.clip_draw_to_origin(*self.q2rect, *self.q2origin)
        self.image.clip_draw_to_origin(*self.q4rect, *self.q4origin)
        self.image.clip_draw_to_origin(*self.q1rect, *self.q1origin)

    def to_screen(self, point):
        x, y = point
        tx, ty = self.target.pos
        return self.fix_x + x - tx, self.fix_y + y - ty

    def translate(self, point):
        x, y = point
        tx, ty = self.target.pos
        dx, dy = x - self.fix_x, y - self.fix_y
        return tx + dx, ty + dy

class HorzScrollBackground:
    def __init__(self, imageName):
        self.imageName = imageName
        self.image = gfw.image.load(res(imageName))
        self.cw, self.ch = get_canvas_width(), get_canvas_height()
        self.scroll = 0
        self.speed = 0

    def update(self):
        self.scroll += self.speed * gfw.delta_time

    def set_scroll(self, scroll):
        self.scroll = scroll

    def draw(self):
        left, bottom = 0, 0
        page = self.image.w * self.ch // self.image.h
        curr = int(-self.scroll) % page
        if curr > 0:
            sw = int(1 + self.image.h * curr / self.ch)
            sl = self.image.w - sw
            src = sl, 0, sw, self.image.h
            dw = int(sw * self.ch / self.image.h)
            dst = curr - dw, 0, dw, self.ch
            self.image.clip_draw_to_origin(*src, *dst)
        dst_width = round(self.image.w * self.ch / self.image.h)
        while curr + dst_width < self.cw:
            dst = curr, 0, dst_width, self.ch
            self.image.draw_to_origin(*dst)
            curr += dst_width
        if curr < self.cw:
            dw = self.cw - curr
            sw = int(1 + self.image.h * dw / self.ch)
            src = 0, 0, sw, self.image.h
            dw = int(sw * self.ch / self.image.h)
            dst = curr, 0, dw, self.ch
            self.image.clip_draw_to_origin(*src, *dst)

    def to_screen(self, point):
        x, y = point
        return x - self.scroll, y

    def translate(self, point):
        x, y = point
        return x + self.scroll, y

    def get_boundary(self):
        return (-sys.maxsize, -sys.maxsize, sys.maxsize, sys.maxsize)

    #     self.image.clip_draw_to_origin(*self.src_rect_1, *self.dst_rect_1)
    #     self.image.clip_draw_to_origin(*self.src_rect_2, *self.dst_rect_2)

    # private void drawHorizontal(Canvas canvas) {
    #     int left = 0;
    #     int top = 0;
    #     int right = UiBridge.metrics.size.x;
    #     int bottom = UiBridge.metrics.size.y;
    #     int pageSize = sbmp.getWidth() * (bottom - top) / sbmp.getHeight();

    #     canvas.save();
    #     canvas.clipRect(left, top, right, bottom);

    #     float curr = scrollX % pageSize;
    #     if (curr > 0) curr -= pageSize;
    #     curr += left;
    #     while (curr < right) {
    #         dstRect.set(curr, top, curr + pageSize, bottom);
    #         curr += pageSize;
    #         canvas.drawBitmap(sbmp.getBitmap(), srcRect, dstRect, null);
    #     }
    #     canvas.restore();
    # }

