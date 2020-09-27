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

    def set_target(self, target):
        x,y = self.pos
        tx,ty = target
        dx, dy = tx - x, ty - y
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0: return

        self.target = target
        self.delta = dx / distance, dy / distance
        self.action = 0 if dx < 0 else 1

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

        done = False
        if self.target is not None:
            tx,ty = self.target
            if dx > 0 and x >= tx or dx < 0 and x <= tx:
                x = tx
                done = True
            if dy > 0 and y >= ty or y < 0 and y <= ty:
                y = ty
                done = True

        if done:
            self.target = None
            self.delta = 0, 0
            self.action = 2 if dx < 0 else 3
        self.pos = x,y

        self.time += gfw.delta_time
        frame = self.time * 15
        self.fidx = int(frame) % 5

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            if self.target is not None:
                self.target = None
                self.delta = 0, 0
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

        if e.type == SDL_MOUSEBUTTONDOWN:
            self.set_target((e.x, get_canvas_height() - e.y - 1))
        elif e.type == SDL_MOUSEMOTION:
            if self.target is not None:
                self.set_target((e.x, get_canvas_height() - e.y - 1))

    def get_bb(self):
        hw = 20
        hh = 40
        x,y = self.pos
        return x - hw, y - hh, x + hw, y + hh
