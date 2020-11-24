import random
from pico2d import *
import gfw

MOVE_PPS = 200

class Missile:
    def __init__(self, pos, delta):
        mag = random.uniform(0.3, 1.0)
        self.init(pos, delta, 'res/missile.png', mag)

    def init(self, pos, delta, imageName, mag=0):
        self.pos = pos
        self.delta = delta
        self.image = gfw.image.load(imageName)
        self.size = self.image.h
        if mag != 0:
            self.size = int(self.size * mag)
        self.radius = self.size // 2
        self.bb_l = -self.size
        self.bb_b = -self.size
        self.bb_r = get_canvas_width() + self.size
        self.bb_t = get_canvas_height() + self.size

    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx * MOVE_PPS * gfw.delta_time
        y += dy * MOVE_PPS * gfw.delta_time
        self.pos = x,y
        if self.out_of_screen():
            # print('removing', self)
            gfw.world.remove(self)
    def draw(self):
        self.image.draw(*self.pos, self.size, self.size)
    def out_of_screen(self):
        x,y = self.pos
        if x < self.bb_l: return True
        if x > self.bb_r: return True
        if y < self.bb_b: return True
        if y > self.bb_t: return True

        return False

class PresentItem(Missile):
    def __init__(self, pos, delta):
        self.init(pos, delta, 'res/present_box.png')

class CoinItem(PresentItem):
    FPS = 10
    def __init__(self, pos, delta):
        self.init(pos, delta, 'res/coin.png', 0.5)
        self.time = get_time()
        self.fcount = self.image.w // self.image.h
    def draw(self):
        elapsed = get_time() - self.time
        fidx = round(elapsed * CoinItem.FPS) % self.fcount
        size = self.image.h
        rect = fidx * size, 0, size, size
        self.image.clip_draw(*rect, *self.pos, self.size, self.size)

