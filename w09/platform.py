import random
from pico2d import *
import gfw
import gobj

UNIT = 60
INFO = [
    ( 10 * UNIT, 2 * UNIT, 'cookierun_platform_480x48.png'),
    (  2 * UNIT, 2 * UNIT, 'cookierun_platform_124x120.png'),
    (  3 * UNIT, 1 * UNIT, 'cookierun_platform_120x40.png'),
]

class Platform:
    T_10x2, T_2x2, T_3x1 = range(3)
    SIZES = [ (10,2), (2,2), (3,1) ]
    def __init__(self, type, left, bottom):
        self.left = left
        self.bottom = bottom
        self.can_pass = type >= Platform.T_3x1
        self.width, self.height, fn = INFO[type]
        self.image = gfw.image.load(gobj.res(fn))
    def update(self): pass
    def draw(self):
        self.image.draw_to_origin(self.left, self.bottom, self.width, self.height)
    def get_bb(self):
        return self.left, self.bottom, self.left + self.width, self.bottom + self.height
    def move(self, dx):
        self.left += dx
        if self.left + self.width < 0:
            # print('count was:', gfw.world.count_at(gfw.layer.platform))
            gfw.world.remove(self)
    @property
    def right(self):
        return self.left + self.width
