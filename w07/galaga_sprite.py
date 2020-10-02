import json
import gfw
from pico2d import *
from gobj import *

galaga_image = None
sprite_rects = {}

def load():
    global galaga_image
    if galaga_image is None:
        galaga_image = gfw.image.load(res('all.png'))
        with open(res('all.json')) as f:
            data = json.load(f)
            for name in data:
                print(name)
                sprite_rects[name] = tuple(data[name])

class Sprite:
    def __init__(self, name, pos):
        load()
        self.name = name
        self.rect = sprite_rects[name]
        self.pos = pos
    def draw(self):
        galaga_image.clip_draw(*self.rect, *self.pos)
    def update(self):
        pass
