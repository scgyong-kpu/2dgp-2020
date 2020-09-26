import random
from pico2d import *
import gfw
import gfw_image
from gobj import *

class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  -1,
        (SDL_KEYDOWN, SDLK_RIGHT):  1,
        (SDL_KEYUP, SDLK_LEFT):     1,
        (SDL_KEYUP, SDLK_RIGHT):   -1,
    }
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)

    #constructor
    def __init__(self):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = 250, 80
        self.dx = 0
        self.speed = 3
        self.image = gfw_image.load(RES_DIR + '/fighter.png')
        half = self.image.w // 2
        self.minx = half
        self.maxx = get_canvas_width() - half

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.dx * self.speed
        if self.x < self.minx: self.x = self.minx
        elif self.x > self.maxx: self.x = self.maxx

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.dx += Player.KEY_MAP[pair]
