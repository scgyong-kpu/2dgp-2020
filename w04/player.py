import random
from pico2d import *
import gfw
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
        self.time = 0
        self.fires = False
        self.image = gfw_image.load(RES_DIR + '/ryu.png')
        self.image2 = gfw_image.load(RES_DIR + '/ryu_1.png')

    def draw(self):
        if self.fires:
            width = 132
            sx = self.fidx * width
            x,y = self.pos
            self.image2.clip_draw(sx, 0, width, 100, x + 16,y)
        else:
            width = 100
            sx = self.fidx * width
            self.image.clip_draw(sx, 0, width, 100, *self.pos)

    def update(self):
        self.time += gfw.delta_time
        self.pos = point_add(self.pos, self.delta)

        if self.fires:
            frame = self.time * 5
            print(frame)
            if frame < 5:
                self.fidx = int(frame)
            else:
                self.time = 0
                self.fires = False
        else:
            frame = self.time * 15
            self.fidx = int(frame) % 5

    def fire(self):
        self.time = 0
        self.fires = True

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.delta = point_add(self.delta, Player.KEY_MAP[pair])
        elif pair == Player.KEYDOWN_SPACE:
            if not self.fires:
                self.fire()
