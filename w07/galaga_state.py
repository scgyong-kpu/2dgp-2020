import json
import gfw
from pico2d import *
from gobj import *
from galaga_sprite import Sprite

canvas_width = 500
canvas_height = 800

class ImageObject:
    def __init__(self, imageName, pos):
        self.image = gfw.image.load(res(imageName))
        self.pos = pos
    def draw(self):
        self.image.draw(*self.pos)
    def update(self):
        pass

def enter():
    gfw.world.init(['bg', 'enemy', 'player'])

    gfw.world.add(gfw.layer.bg, ImageObject('space.png', (250,400)))
    gfw.world.add(gfw.layer.player, Sprite((0,640,60,64), (250, 50)))
    gfw.world.add(gfw.layer.enemy, Sprite((0,512,60,64), (90, 297)))
    gfw.world.add(gfw.layer.enemy, Sprite((0,344,52,40), (381, 469)))
    gfw.world.add(gfw.layer.enemy, Sprite((0,344,52,40), (281, 369)))
    gfw.world.add(gfw.layer.enemy, Sprite((0,408,52,40), (317, 602)))
    gfw.world.add(gfw.layer.enemy, Sprite((0,408,52,40), (217, 502)))

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()
    # gobj.draw_collision_box()

def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
