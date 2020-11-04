import gfw
from pico2d import *
import gobj

class Card:
    WIDTH,HEIGHT = 100,100
    def __init__(self, index, pos):
        self.bg = gobj.ImageObject('back.png', pos)
        self.index = index
    def draw(self):
        self.bg.draw()
    def update(self):
        pass
    def get_bb(self):
        hw = Card.WIDTH // 2
        hh = Card.HEIGHT // 2
        x,y = self.bg.pos
        return x - hw, y - hh, x + hw, y + hh

    def remove(self):
        gfw.world.remove(self)

    # def __del__(self):
    #     print('Del:', self)