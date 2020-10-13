import random
from pico2d import *
import gfw
import gobj

JELLY_BORDER = 2
JELLY_SIZE = 66
BB_RADIUS = 30

def get_jelly_rect(index):
    ix, iy = index % 30, index // 30
    x = ix * (JELLY_BORDER + JELLY_SIZE) + JELLY_BORDER
    y = iy * (JELLY_BORDER + JELLY_SIZE) + JELLY_BORDER
    return x, y, JELLY_SIZE, JELLY_SIZE


class Jelly:
    TYPE_1, TYPE_2, TYPE_3, TYPE_R = range(4)
    def __init__(self, type, x, y):
        self.x, self.y = x, y
        self.image = gfw.image.load(gobj.res('jelly.png'))
        index = random.randint(3, 60) if type == Jelly.TYPE_R else type
        self.rect = get_jelly_rect(index)
    def update(self): pass
    def draw(self):
        self.image.clip_draw(*self.rect, self.x, self.y)
    def move(self, dx):
        self.x += dx
        if self.x + JELLY_SIZE < 0:
            gfw.world.remove(self)
    def get_bb(self):
        return (
            self.x - BB_RADIUS, self.y - BB_RADIUS, 
            self.x + BB_RADIUS, self.y + BB_RADIUS
        )

