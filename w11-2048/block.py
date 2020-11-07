from gobj import *

class Block(AnimObject):
    def __init__(self, value):
        self.value = value
        fn = 'block_%05d.png' % value
        super(Block, self).__init__(fn, (0, 0), 10)
    def move_to(self, x, y):
        x = x * 120 + 80
        y = y * 120 + 80
        self.pos = x, y

