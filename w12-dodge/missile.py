from pico2d import *
import gfw
import random

MOVE_PPS = 200

class Missile:
    def __init__(self, pos, delta):
        self.init(pos, delta, 'res/missile.png')
        mag = random.uniform(0.3, 1.0)
        self.radius = mag * self.image.h // 2

    def init(self, pos, delta, imageName):
        self.pos = pos
        self.delta = delta
        self.image = gfw.image.load(imageName)
        self.radius = self.image.h // 2

    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx * MOVE_PPS * gfw.delta_time
        y += dy * MOVE_PPS * gfw.delta_time
        self.pos = x,y
        if not self.in_boundary():
            gfw.world.remove(self)

    def draw(self):
        diameter = 2 * self.radius
        self.image.draw(*self.pos, diameter, diameter)

    def in_boundary(self):
        x,y = self.pos
        if x < -self.radius: return False
        if y < -self.radius: return False
        if x > get_canvas_width() + self.radius: return False
        if y > get_canvas_height() + self.radius: return False
        return True

class PresentItem(Missile):
    def __init__(self, pos, delta):
        self.init(pos, delta, 'res/present_box.png')

class CoinItem(PresentItem):
    def __init__(self, pos, delta):
        self.init(pos, delta, 'res/coin.png')
        self.time = get_time()
        self.fps = 8
        self.fcount = 6
        self.radius = 30

    def draw(self):
        elapsed = get_time() - self.time
        fidx = round(elapsed * self.fps) % self.fcount
        src_size = self.image.h
        dst_size = self.radius * 2
        self.image.clip_draw(src_size * fidx, 0, src_size, src_size, *self.pos, dst_size, dst_size)
