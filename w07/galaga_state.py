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

    gfw.world.add(gfw.layer.player, Sprite('player', (250, 50)))

    e = Sprite('commander_green', (180, 740), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('commander_green', (250, 740), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('commander_green', (320, 740), True)
    gfw.world.add(gfw.layer.enemy, e)

    e = Sprite('butterfly', (70, 670), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('butterfly', (130, 670), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('butterfly', (190, 670), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('butterfly', (250, 670), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('butterfly', (310, 670), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('butterfly', (370, 670), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('butterfly', (430, 670), True)
    gfw.world.add(gfw.layer.enemy, e)

    e = Sprite('butterfly', (70, 610), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('butterfly', (130, 610), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('butterfly', (190, 610), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('butterfly', (250, 610), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('butterfly', (310, 610), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('butterfly', (370, 610), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('butterfly', (430, 610), True)
    gfw.world.add(gfw.layer.enemy, e)

    e = Sprite('bee_yellow', (70, 550), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('bee_yellow', (130, 550), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('bee_yellow', (190, 550), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('bee_yellow', (250, 550), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('bee_yellow', (310, 550), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('bee_yellow', (370, 550), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('bee_yellow', (430, 550), True)
    gfw.world.add(gfw.layer.enemy, e)

    e = Sprite('bee_yellow', (70, 490), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('bee_yellow', (130, 490), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('bee_yellow', (190, 490), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('bee_yellow', (250, 490), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('bee_yellow', (310, 490), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('bee_yellow', (370, 490), True)
    gfw.world.add(gfw.layer.enemy, e)
    e = Sprite('bee_yellow', (430, 490), True)
    gfw.world.add(gfw.layer.enemy, e)
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
