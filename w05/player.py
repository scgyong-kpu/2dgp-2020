import random
from pico2d import *
import gfw
import gfw_image
from gobj import *
from bullet import *

class Player:
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_LEFT):  -1,
        (SDL_KEYDOWN, SDLK_RIGHT):  1,
        (SDL_KEYUP, SDLK_LEFT):     1,
        (SDL_KEYUP, SDLK_RIGHT):   -1,
    }
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    LASER_INTERVAL = 0.25
    SPARK_INTERVAL = 0.05

    #constructor
    def __init__(self):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = 250, 80
        self.dx = 0
        self.speed = 3
        self.image = gfw_image.load(RES_DIR + '/fighter.png')
        self.spark = gfw_image.load(RES_DIR + '/laser_0.png')
        half = self.image.w // 2
        self.minx = half
        self.maxx = get_canvas_width() - half

        self.laser_time = 0

    def fire(self):
        self.laser_time = 0
        bullet = LaserBullet(self.x, self.y, 5)
        LaserBullet.bullets.append(bullet)

    def draw(self):
        self.image.draw(self.x, self.y)
        if self.laser_time < Player.SPARK_INTERVAL:
            self.spark.draw(self.x, self.y + 28)


    def update(self):
        self.x += self.dx * self.speed
        self.laser_time += gfw.delta_time
        if self.x < self.minx: self.x = self.minx
        elif self.x > self.maxx: self.x = self.maxx

        if self.laser_time >= Player.LASER_INTERVAL:
            self.fire()

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair in Player.KEY_MAP:
            self.dx += Player.KEY_MAP[pair]
