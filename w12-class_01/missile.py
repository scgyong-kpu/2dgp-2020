from pico2d import *
import gfw

MOVE_PPS = 200

class Missile:
    def __init__(self, pos, delta, mag):
        self.init(pos, delta, 'res/missile.png', mag)

    def init(self, pos, delta, imageName, mag=0):
        self.pos = pos
        self.delta = delta
        self.image = gfw.image.load(imageName)
        if mag != 0:
            self.radius = self.image.h // 2 * mag
            self.size = (self.radius * 2, self.radius * 2)
        else:
            self.radius = self.image.h // 2
            self.size = (self.image.h, self.image.h)

    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx * MOVE_PPS * gfw.delta_time
        y += dy * MOVE_PPS * gfw.delta_time
        if x < -self.image.w or \
          x > get_canvas_width() + self.image.w or \
          y < -self.image.h or \
          y > get_canvas_height() + self.image.h:
            gfw.world.remove(self)
        self.pos = x, y
    def draw(self):
        self.image.draw(*self.pos, *self.size)

class PresentItem(Missile):
    def __init__(self, pos, delta):
        self.init(pos, delta, 'res/present_box.png')
        self.score = 5

class CoinItem(PresentItem):
    FPS = 10
    def __init__(self, pos, delta):
        self.init(pos, delta, 'res/coin.png', 0.5)
        self.time = get_time()
        self.fcount = self.image.w // self.image.h
        self.score = 8
    def draw(self):
        elapsed = get_time() - self.time
        fidx = round(elapsed * CoinItem.FPS) % self.fcount
        size = self.image.h
        rect = fidx * size, 0, size, size
        self.image.clip_draw(*rect, *self.pos, *self.size)
