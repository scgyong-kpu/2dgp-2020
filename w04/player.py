import random
from pico2d import *
import gfw_image
from gobj import *

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
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    image = None

    #constructor
    def __init__(self):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.pos = 100, 100
        self.delta = 0, 0
        self.fidx = 0
        self.target = None
        self.targets = []
        self.speed = 0
        if Player.image == None:
            Player.image = gfw_image.load(RES_DIR + '/ryu.png')

    def draw(self):
        sx = self.fidx * 100
        self.image.clip_draw(sx, 0, 100, 100, *self.pos)

    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        self.pos = x+dx, y+dy
        self.fidx = (self.fidx + 1) % 5

    def fire(self):
        pass

    def updateDelta(self, ddx, ddy):
        dx,dy = self.delta
        self.delta = dx+ddx, dy+ddy

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            if self.target is not None:
                if e.type == SDL_KEYUP: return
                self.updateAction(0, -self.delta[0])
                self.target = None
                self.delta = 0,0
                self.targets = []
                self.speed = 0
            self.updateDelta(*Player.KEY_MAP[pair])
        elif pair == Player.KEYDOWN_SPACE:
            self.fire()
