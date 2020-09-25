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
        if Player.image == None:
            Player.image = gfw_image.load(RES_DIR + '/ryu.png')

    def draw(self):
        sx = self.fidx * 100
        self.image.clip_draw(sx, 0, 100, 100, *self.pos)

    def update(self):
        self.time += gfw.delta_time
        self.pos = point_add(self.pos, self.delta)
        frame = self.time * 10
        self.fidx = int(frame) % 5

    def fire(self):
        pass

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.delta = point_add(self.delta, Player.KEY_MAP[pair])
        elif pair == Player.KEYDOWN_SPACE:
            self.fire()
