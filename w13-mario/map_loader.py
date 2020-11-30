from pico2d import *
import gfw
import json

def load():
    with open('res/objects.json') as f:
        objects = json.load(f)

    for d in objects:
        clazz = CLASSES[d["type"]]
        obj = clazz(d)
        gfw.world.add(obj.layer(), obj)

    global sprite_image
    sprite_image = gfw.image.load('res/sprites.png')

class SpriteObj:
    def __init__(self, d):
        self.pos = d["x"], d["y"]
        self.size = d["width"], d["height"]
        self.name = d["name"]
        self.time = 0
    def layer(self): return gfw.layer.platform
    def draw(self):
        rect = self.getRect()
        sprite_image.clip_draw_to_origin(*rect, *self.pos, *self.size)
    def get_bb(self):
        l, b, w, h = self.getRect()
        return l, b, l+w, b+h
    def update(self):
        pass

class Platform(SpriteObj):
    def getRect(self):
        return ( 27, 233, 457, 93 )

class Stone(SpriteObj):
    def getRect(self):
        return ( 31, 551, 64, 55 )

class Rock(SpriteObj):
    def getRect(self):
        return ( 33, 344, 263, 190 )

class Ladder(SpriteObj):
    def getRect(self):
        return ( 453, 381, 39, 227 )

class Coin(SpriteObj):
    RECTS = [
        (582, 445, 31, 32),
        (615, 445, 30, 32),
        (652, 445, 21, 32),
        (690, 445, 10, 32),
        (718, 445, 21, 32),
        (747, 445, 30, 32),
    ]
    def getRect(self):
        return Coin.RECTS[0]

    def draw(self):
        rect = self.getRect()
        sprite_image.clip_draw(*rect, *self.pos)
    def layer(self):
        return gfw.layer.item

CLASSES = {
    "Platform": Platform,
    "Rock": Rock,
    "Ladder": Ladder,
    "Coin": Coin,
    "Stone": Stone,
}

