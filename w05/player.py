import random
from pico2d import *
import gfw
import gfw_image
from gobj import *

class IdleState:
    @staticmethod
    def get(player):
        if not hasattr(IdleState, 'singleton'): 
            IdleState.singleton = IdleState()
            IdleState.singleton.player = player
        return IdleState.singleton

    def __init__(self):
        self.image = gfw_image.load(RES_DIR + '/ryu.png')

    def enter(self):
        self.time = 0
        self.fidx = 0
    def exit(self):
        pass
    def draw(self):
        width = 100
        sx = self.fidx * width
        self.image.clip_draw(sx, 0, width, 100, *self.player.pos)

    def update(self):
        self.time += gfw.delta_time
        # self.player.pos = point_add(self.player.pos, self.player.delta)
        move_obj(self.player)
        frame = self.time * 15
        self.fidx = int(frame) % 5

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.player.delta = point_add(self.player.delta, Player.KEY_MAP[pair])
        elif pair == Player.KEYDOWN_SPACE:
            self.player.set_state(FireState)

class FireState:
    @staticmethod
    def get(player):
        if not hasattr(FireState, 'singleton'): 
            FireState.singleton = FireState()
            FireState.singleton.player = player
        return FireState.singleton

    def __init__(self):
        self.image = gfw_image.load(RES_DIR + '/ryu_1.png')

    def enter(self):
        self.time = 0
        self.fidx = 0
    def exit(self):
        pass
    def draw(self):
        width = 132
        sx = self.fidx * width
        x,y = self.player.pos
        self.image.clip_draw(sx, 0, width, 100, x + 16, y)

    def update(self):
        self.time += gfw.delta_time
        frame = self.time * 5
        print(frame)
        if frame < 5:
            self.fidx = int(frame)
        else:
            self.player.set_state(IdleState)

    def handle_event(self, e):
        pass

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
        self.state = None
        self.set_state(IdleState)
        self.image = gfw_image.load(RES_DIR + '/ryu.png')
        self.image2 = gfw_image.load(RES_DIR + '/ryu_1.png')

    def set_state(self, clazz):
        if self.state != None:
            self.state.exit()
        self.state = clazz.get(self)
        self.state.enter()

    def draw(self):
        self.state.draw()

    def update(self):
        self.state.update()

    def fire(self):
        self.time = 0
        self.set_state(FireState)

    def handle_event(self, e):
        self.state.handle_event(e)
