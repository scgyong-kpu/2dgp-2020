from pico2d import *
import gfw
import gfw_image
import gfw_world
from gobj import *

class Enemy:
    SIZE = 96
    def __init__(self, x, speed):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, get_canvas_height()
        self.dx, self.dy = 0, speed
        self.image = gfw_image.load(RES_DIR + '/enemy_01.png')
        self.fidx = 0
        self.src_width = self.image.w // 8
        self.src_height = self.image.h
        self.time = 0
    def draw(self):
        sx = self.fidx * self.src_width
        self.image.clip_draw(sx, 0, self.src_width, self.src_height, self.x, self.y)
    def update(self):
        self.time += gfw.delta_time
        self.fidx = int(self.time * 10 + 0.5) % 8
        # self.x += self.dx
        self.y += self.dy

        if self.y < -Enemy.SIZE:
            self.remove()

    def remove(self):
        gfw_world.remove(self)

