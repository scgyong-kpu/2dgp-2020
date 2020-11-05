import random
from pico2d import *
import gfw
import gobj

class Card:
    WIDTH,HEIGHT = 100,100
    def __init__(self, index, pos, theme='.'):
        self.bg = gobj.ImageObject(theme + '/back.png', pos)
        fps = random.randrange(20, 30)
        self.fg = gobj.AnimObject(theme + '/f_%02d.png' % index, pos, fps)
        self.image = self.bg
        self.index = index
    def draw(self):
        self.image.draw()
    def update(self):
        pass
    def handle_event(self, e):
        if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
            pos = gobj.mouse_xy(e)
            if gobj.pt_in_rect(pos, self.get_bb()):
                self.toggle()
                return True
        return False
    def toggle(self):
        self.image = self.bg if self.image == self.fg else self.fg
    def get_bb(self):
        hw = Card.WIDTH // 2
        hh = Card.HEIGHT // 2
        x,y = self.bg.pos
        return x - hw, y - hh, x + hw, y + hh

    def remove(self):
        gfw.world.remove(self)

    def __del__(self):
        print('Del Card:', self)