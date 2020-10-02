import json
import gfw
from pico2d import *

canvas_width = 500
canvas_height = 800

class ImageObject:
    def __init__(self, imageName, pos):
        self.image = gfw.image.load('./res/' + imageName)
        self.pos = pos
    def draw(self):
        self.image.draw(*self.pos)
    def update(self):
        pass

def enter():
    gfw.world.init(['bg', 'enemy', 'player'])

    gfw.world.add(gfw.layer.bg, ImageObject('space.png', (250,400)))

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
