import random
from pico2d import *
import gfw
import gobj

class Player:
    KEYDOWN_SPACE  = (SDL_KEYDOWN, SDLK_SPACE)

    #constructor
    def __init__(self):
        self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.delta = 0, 0
        self.image = gfw.image.load(gobj.res('cookie.png'))
        self.time = 0
        self.anim = [ 0x40, 0x41, 0x42, 0x43 ]
        self.FPS = 10

    def draw(self):
        fidx = round(self.time * self.FPS) % len(self.anim)
        sprite_num = self.anim[fidx]
        x, y = sprite_num % 0x10, sprite_num // 0x10
        x = x * 272 + 2
        y = y * 272 + 2
        self.image.clip_draw(x, y, 270, 270, *self.pos)

    def update(self):
        self.time += gfw.delta_time

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair == Player.KEYDOWN_SPACE:
            pass

    def get_bb(self):
        hw = 20
        hh = 40
        x,y = self.pos
        return x - hw, y - hh, x + hw, y + hh

    def __getstate__(self):
        dict = self.__dict__.copy()
        del dict['image']
        return dict

    def __setstate__(self, dict):
        # self.__init__()
        self.__dict__.update(dict)
        self.image = gfw.image.load(gobj.RES_DIR + '/animation_sheet.png')
