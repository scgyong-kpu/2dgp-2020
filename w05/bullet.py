from pico2d import *
import gfw
import gfw_image
from gobj import *

class LaserBullet:
    bullets = []
    SIZE = 40
    def __init__(self, x, y, speed):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = x, y
        self.dy = speed
        self.image = gfw_image.load(RES_DIR + '/laser_1.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y += self.dy

        if self.y > get_canvas_height() + LaserBullet.SIZE:
            self.remove()

    def remove(self):
        LaserBullet.bullets.remove(self)
        print('\t\t\t\t\t\tRemoving', self)
