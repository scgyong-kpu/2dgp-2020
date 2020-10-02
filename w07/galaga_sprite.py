import gfw
from pico2d import *
from gobj import *

galaga_image = None

def load():
    global galaga_image
    if galaga_image is None:
        galaga_image = gfw.image.load(res('all.png'))
class Sprite:
    def __init__(self, rect, pos):
        self.rect = rect
        self.pos = pos
        load()
    def draw(self):
        galaga_image.clip_draw(*self.rect, *self.pos)
    def update(self):
        pass
