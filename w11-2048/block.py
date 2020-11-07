import gfw
from gobj import *

SPEED_PPS = 3000
MAG_SPEED = 0.15

class Block(AnimObject):
    def __init__(self, value):
        self.value = value
        fn = 'block_%05d.png' % value
        super(Block, self).__init__(fn, (0, 0), 10)
        self.target = None
        self.being_born = True
        self.mag = 0
    def double(self):
        self.value *= 2
        fn = 'block_%05d.png' % self.value
        self.image = gfw.image.load(res(fn))
    def move_to(self, x, y, animates=True):
        x = x * 120 + 80
        y = y * 120 + 80
        if animates:
            self.target = x,y
            # print('target = ', self.target)
        else:
            self.pos = x, y
    def draw(self):
        elapsed = get_time() - self.time
        fidx = round(elapsed * self.fps) % self.fcount
        sx = self.width * fidx
        size = self.width * self.mag, self.height * self.mag
        self.image.clip_draw(sx, 0, self.width, self.height, *self.pos, *size)
    def update(self):
        if self.target is not None: 
            self.head_to_target()
        if self.being_born:
            self.mag += (1.0/MAG_SPEED) * gfw.delta_time
            if self.mag >= 1.0:
                self.mag = 1.0
                self.being_born = False
    def head_to_target(self):
        dist = SPEED_PPS * gfw.delta_time
        x,y = self.pos
        tx,ty = self.target
        if x < tx:
            x = min(x + dist, tx)
        elif x > tx:
            x = max(tx, x - dist)
        if y < ty:
            y = min(y + dist, ty)
        elif y > ty:
            y = max(ty, y - dist)

        self.pos = x,y
        if self.pos == self.target:
            self.target = None

    def remove(self):
        gfw.world.remove(self)



    def __del__(self):
        print("Removing", self)