import gfw
from gobj import *

SPEED_PPS = 3000

class Block(AnimObject):
    def __init__(self, value):
        self.value = value
        fn = 'block_%05d.png' % value
        super(Block, self).__init__(fn, (0, 0), 10)
        self.target = None
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
    def update(self):
        if self.target is None: return
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