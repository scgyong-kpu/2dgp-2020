import json
import gfw
from pico2d import *
from gobj import *

galaga_image = None
sprite_rects = {}

LBTN_DOWN = (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT)
LBTN_UP   = (SDL_MOUSEBUTTONUP,   SDL_BUTTON_LEFT)
RBTN_DOWN = (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_RIGHT)
KEYDN_DEL = (SDL_KEYDOWN, SDLK_DELETE)
TEXT_COLOR = (255, 255, 255)

def load():
    global galaga_image
    if galaga_image is None:
        galaga_image = gfw.image.load(res('all.png'))
        with open(res('all.json')) as f:
            data = json.load(f)
            for name in data:
                sprite_rects[name] = tuple(data[name])

    global pos_font
    pos_font = gfw.font.load(res('ENCR10B.TTF'), 15)

class Sprite:
    FPS = 3
    def __init__(self, name, pos, animates=False):
        load()
        self.name = name
        self.rect = sprite_rects[name]
        self.pos = pos
        self.animates = animates
        self.mouse_point = None
        self.hw, self.hh = self.rect[2] // 2, self.rect[3] // 2
        if animates:
            self.time = get_time()

    def draw(self):
        if self.animates:
            frame = round((get_time() - self.time) * Sprite.FPS)
            if frame % 2 == 0:
                galaga_image.clip_draw(*self.rect, *self.pos)
            else:
                l,b,w,h = self.rect
                galaga_image.clip_draw(l+w, b, w, h, *self.pos)
        else:
            galaga_image.clip_draw(*self.rect, *self.pos)

    def draw_position(self):
        draw_rectangle(*self.get_bb())
        x,y = self.pos
        x -= 2 * self.hw
        y -= 2 * self.hh
        pos_font.draw(x, y, str(self.pos), TEXT_COLOR)


    def handle_event(self, e):
        pair = (e.type, e.button)
        if self.mouse_point is None:
            if pair == LBTN_DOWN:
                if pt_in_rect(mouse_xy(e), self.get_bb()):
                    self.mouse_point = mouse_xy(e)
                    return True
            return False

        if pair == LBTN_UP:
            self.mouse_point = None
            return False

        if e.type == SDL_MOUSEMOTION:
            x,y = self.pos
            mx,my = mouse_xy(e)
            px,py = self.mouse_point
            self.pos = x + mx - px, y + my - py
            # print((x,y), (mx,my), (px,py), self.pos)
            self.mouse_point = mx,my
        elif (e.type, e.key) == KEYDN_DEL or (e.type, e.button) == RBTN_DOWN:
            gfw.world.remove(self)
            return False

        return True

    def update(self):
        pass

    def get_bb(self):
        x,y = self.pos
        return x - self.hw, y - self.hh, x + self.hw, y + self.hh

    def dictionary(self):
        x,y = self.pos
        return { "name": self.name, "x": x, "y": y }
