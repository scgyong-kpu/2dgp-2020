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
                sprite_rects[name] = tuple(data[name])

class Sprite:
    FPS = 3
    def __init__(self, name, pos, animates=False):
        load()
        self.name = name
        self.rect = sprite_rects[name]
        self.pos = pos
        self.animates = animates
        if animates:
            self.time = get_time()

    def draw(self):
        if self.animates:
            frame = round((get_time() - self.time) * Sprite.FPS)
            if frame % 2 == 0:
                galaga_image.clip_draw(*self.rect, *self.pos)
            else:
                l,b,w,h = self.rect
                galaga_image.clip_draw(l+w, b, w, h, *self.pos)
        else:
            galaga_image.clip_draw(*self.rect, *self.pos)
    def update(self):
        pass
