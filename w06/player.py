import random
from pico2d import *
import gfw
import gobj


class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  (-1,  0),
        (SDL_KEYDOWN, SDLK_RIGHT): ( 1,  0),
        (SDL_KEYDOWN, SDLK_DOWN):  ( 0, -1),
        (SDL_KEYDOWN, SDLK_UP):    ( 0,  1),
        (SDL_KEYUP, SDLK_LEFT):    ( 1,  0),
        (SDL_KEYUP, SDLK_RIGHT):   (-1,  0),
        (SDL_KEYUP, SDLK_DOWN):    ( 0,  1),
        (SDL_KEYUP, SDLK_UP):      ( 0, -1),
    }
    KEYDOWN_SPACE  = (SDL_KEYDOWN, SDLK_SPACE)
    KEYDOWN_LSHIFT = (SDL_KEYDOWN, SDLK_LSHIFT)
    KEYUP_LSHIFT   = (SDL_KEYUP,   SDLK_LSHIFT)
    image = None

    #constructor
    def __init__(self):
        self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.delta = 0, 0
        self.target = None
        self.speed = 200
        self.image = gfw.image.load(gobj.RES_DIR + '/animation_sheet.png')
        self.time = 0
        self.fidx = 0
        self.action = 2
        self.mag = 1

    def draw(self):
        width,height = 100,100
        sx = self.fidx * width
        sy = self.action * height
        self.image.clip_draw(sx, sy, width, 100, *self.pos)

    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx * self.speed * self.mag * gfw.delta_time
        y += dy * self.speed * self.mag * gfw.delta_time
        self.pos = x,y

        if self.target is not None:
            helper.move_toward_obj(self)

        self.time += gfw.delta_time
        frame = self.time * 15
        self.fidx = int(frame) % 5

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            pdx = self.delta[0]
            self.delta = gobj.point_add(self.delta, Player.KEY_MAP[pair])
            dx = self.delta[0]
            self.action = \
                0 if dx < 0 else \
                1 if dx > 0 else \
                2 if pdx < 0 else 3
            # print(dx, pdx, self.action)
        elif pair == Player.KEYDOWN_LSHIFT:
            self.mag *= 2
        elif pair == Player.KEYUP_LSHIFT:
            self.mag //= 2
