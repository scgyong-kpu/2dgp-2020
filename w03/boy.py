import random
from pico2d import *
from gobj import *
from ball import Ball

class Boy:
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
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    image = None

    #constructor
    def __init__(self, rand_pos=False):
        if rand_pos:
            self.pos = (
                random.randint(100, 700),
                random.randint(100, 500)
            )
            self.action = random.randint(0, 3)
        else:
            self.pos = get_canvas_width() // 2, get_canvas_height() // 2
            self.action = 3
        self.delta = 0, 0
        self.fidx = random.randint(0, 7)
        if Boy.image == None:
            Boy.image = load_image(RES_DIR + '/animation_sheet.png')

    def draw(self):
        sx = self.fidx * 100
        sy = self.action * 100
        self.image.clip_draw(sx, sy, 100, 100, *self.pos)

    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        self.pos = x+dx, y+dy
        self.fidx = (self.fidx + 1) % 8

    def ballDelta(self):
        dxs = [ -3, 3, -1, 1 ]
        mag = dxs[self.action]
        dx,dy = self.delta
        return rand(mag+dx), rand(2+dy)

    def fire(self):
        big = random.choice([False, True])
        ball = Ball(self.pos, self.ballDelta(), big)
        Ball.balls.append(ball)
        print('Ball count = %d' % len(Ball.balls))

    def updateDelta(self, ddx, ddy):
        dx,dy = self.delta
        dx += ddx
        dy += ddy
        if ddx != 0:
            self.action = \
                0 if dx < 0 else \
                1 if dx > 0 else \
                2 if ddx > 0 else 3
        self.delta = dx, dy

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Boy.KEY_MAP:
            self.updateDelta(*Boy.KEY_MAP[pair])
        elif pair == Boy.KEYDOWN_SPACE:
            self.fire()
