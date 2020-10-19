import random
from pico2d import *
import gfw
import gobj

class AnimObject:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.images = []
        self.fps = 1
        self.time = 0
        self.loops = False
    def set_anim(self, files, fps, loops=False):
        self.images = [ gfw.image.load(f) for f in files ]
        if len(self.images) > 0:
            self.image = self.images[0]
        self.fps = fps
        self.loops = loops
    def update(self):
        image_count = len(self.images)
        if image_count <= 1: return
        self.time += gfw.delta_time
        fidx = round(self.time * self.fps)
        if self.loops:
            fidx %= image_count
        elif fidx >= image_count:
            fidx = image_count - 1
        self.image = self.images[fidx]
        # print(fidx)
    def draw(self):
        self.image.draw(self.x, self.y)
    def move(self, dx):
        self.x += dx
        if self.x + self.image.w < 0:
            gfw.world.remove(self)

