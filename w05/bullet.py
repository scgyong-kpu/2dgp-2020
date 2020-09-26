from pico2d import *
import gfw
import gfw_image
import gfw_world
from gobj import *

class LaserBullet:
    bullets = []
    trashcan = []
    SIZE = 40
    def __init__(self, x, y, speed):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.dy = speed
        self.image = gfw_image.load(RES_DIR + '/laser_1.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y += self.dy * gfw.delta_time

        if self.y > get_canvas_height() + LaserBullet.SIZE:
            self.remove()

    def remove(self):
        gfw_world.remove(self)

    def get_bb(self):
        hw = self.image.w // 2
        hh = self.image.h // 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh
