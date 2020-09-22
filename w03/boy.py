import random
from pico2d import *
import gfw_image
from gobj import *
from ball import Ball
import helper

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
        self.target = None
        self.targets = []
        self.speed = 0
        if Boy.image == None:
            Boy.image = gfw_image.load(RES_DIR + '/animation_sheet.png')

    def draw(self):
        sx = self.fidx * 100
        sy = self.action * 100
        self.image.clip_draw(sx, sy, 100, 100, *self.pos)

    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        self.pos = x+dx, y+dy

        if self.target is not None:
            ddx = -self.delta[0]
            helper.move_toward_obj(self)
            if self.target == None:
                print("Removing target: ", self.targets[0], " from %d target(s)." % len(self.targets))
                del self.targets[0]
                if len(self.targets) > 0:
                    helper.set_target(self, self.targets[0])
                    self.updateAction(self.delta[0],0)
                else:
                    self.speed = 0
                    self.updateAction(0, ddx)
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
            self.updateAction(dx, ddx)
        self.delta = dx, dy

    def updateAction(self, dx, ddx):
        self.action = \
            0 if dx < 0 else \
            1 if dx > 0 else \
            2 if ddx > 0 else 3

    def appendTarget(self, target):
        if target == self.pos: return
        for t in self.targets:
            if t == target: return

        # helper.set_target(self, target)

        self.targets.append(target)
        self.speed += 1
        print('speed =', self.speed, 'to', self.targets[0], 'adding target:', target)
        helper.set_target(self, self.targets[0])
        self.updateAction(self.delta[0],0)

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Boy.KEY_MAP:
            if self.target is not None:
                if e.type == SDL_KEYUP: return
                self.updateAction(0, -self.delta[0])
                self.target = None
                self.delta = 0,0
                self.targets = []
                self.speed = 0
            self.updateDelta(*Boy.KEY_MAP[pair])
        elif pair == Boy.KEYDOWN_SPACE:
            self.fire()
        elif e.type == SDL_MOUSEBUTTONDOWN:
            self.appendTarget((e.x, get_canvas_height() - e.y - 1))
