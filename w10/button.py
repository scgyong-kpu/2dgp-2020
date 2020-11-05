import gfw
from pico2d import *
from gobj import *

LBTN_DOWN = (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)
LBTN_UP   = (SDL_MOUSEBUTTONUP,   SDL_BUTTON_LEFT)

class BtnBg:
    def __init__(self, image):
        self.image = gfw.image.load(image)
        self.left = self.image.w // 2
        self.right = self.image.w - self.left - 1

    def draw(self, l, b, w, h):
        src_left = 0, 0, self.left, self.image.h
        dst_left = l, b, self.left, h
        self.image.clip_draw_to_origin(*src_left, *dst_left)

        center = w - self.left - self.right
        src_mid = self.left, 0, 1, self.image.h
        dst_mid = l + self.left, b, center, h
        self.image.clip_draw_to_origin(*src_mid, *dst_mid)

        src_right = self.image.w - self.right, 0, self.right, self.image.h
        dst_right = l + w - self.right, b, self.right, h
        self.image.clip_draw_to_origin(*src_right, *dst_right)

    btn_bg_cache = {}
    @staticmethod
    def get(name, state):
        key = name + '_' + str(state)
        if key in BtnBg.btn_bg_cache:
            return BtnBg.btn_bg_cache[key]

        file = name + '_' + state + '_btn3.png'
        btn_bg = BtnBg(res(file))
        BtnBg.btn_bg_cache[key] = btn_bg
        return btn_bg

class Button:
    def __init__(self, l, b, w, h, font, text, callback, btnClass=None):
        self.l, self.b, self.w, self.h = l, b, w, h
        self.callback = callback
        self.set_text(font, text)
        self.t_x = self.l + (self.w - self.t_w) / 2
        self.t_y = self.b + self.h // 2
        self.mouse_point = None
        self.bg = BtnBg.get('blue', 'normal')

    def set_text(self, font, text):
        self.text = text
        self.font = font
        self.t_w, self.t_h = get_text_extent(font, text)
        
    def draw(self):
        self.bg.draw(self.l, self.b, self.w, self.h)
        # self.font.draw(self.t_x, self.t_y, self.text)
        draw_centered_text(self.font, self.text, self.l, self.b, self.w, self.h)
        # draw_rectangle(self.l, self.b, self.l + self.w, self.b + self.h)

    def handle_event(self, e):
        pair = (e.type, e.button)
        if self.mouse_point is None:
            if pair == LBTN_DOWN:
                if pt_in_rect(mouse_xy(e), self.get_bb()):
                    self.mouse_point = mouse_xy(e)
                    self.backup = self.text
                    self.text = "Pressed"
                    self.bg = BtnBg.get('blue', 'pressed')
                    return True
            if e.type == SDL_MOUSEMOTION:
                mpos = mouse_xy(e)
                in_rect = pt_in_rect(mpos, self.get_bb())
                if in_rect:
                    self.bg = BtnBg.get('blue', 'hover')
                    return True
                else:
                    self.bg = BtnBg.get('blue', 'normal')
                    return False

            return False

        if pair == LBTN_UP:
            self.mouse_point = None
            self.text = self.backup
            mpos = mouse_xy(e)
            if pt_in_rect(mpos, self.get_bb()):
                self.callback()
            self.bg = BtnBg.get('blue', 'normal')
            return False

        if e.type == SDL_MOUSEMOTION:
            mpos = mouse_xy(e)
            in_rect = pt_in_rect(mpos, self.get_bb())
            if in_rect:
                self.text = "In Rect"
                self.bg = BtnBg.get('blue', 'pressed')
            else:
                self.text = "Out Rect"
                self.bg = BtnBg.get('blue', 'hover')

        return True

    def get_bb(self):
        return self.l, self.b, self.l + self.w, self.b + self.h

    def update(self):
        pass

    # def __del__(self):
    #     print('Del Button:', self)

def get_text_extent(font, text):
    w, h = c_int(), c_int()
    TTF_SizeText(font.font, text.encode('utf-8'), ctypes.byref(w), ctypes.byref(h))
    return w.value, h.value

def draw_centered_text(font, text, l, b, w, h):
    tw, th = get_text_extent(font, text)
    tx = l + (w - tw) // 2
    ty = b + h // 2
    font.draw(tx, ty, text)

