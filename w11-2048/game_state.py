import random
from pico2d import *
from ext_pico2d import *
import gfw
import gobj
import board
from block import Block

def build_world():
    gfw.world.init(['bg', 'block', 'ui'])
    bg = gobj.ImageBackground('FF9F49.png')
    gfw.world.add(gfw.layer.bg, bg)

def generate_block():
    if board.is_full(): return

    value = random.choice([2, 4])
    block = Block(value)
    x,y = board.generate_block(block)

    x = x * 120 + 80
    y = y * 120 + 80
    fn = 'block_%05d.png' % value
    block = gobj.AnimObject(fn, (x,y), 10)
    gfw.world.add(gfw.layer.block, block)


def enter():
    build_world()

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()
    
def handle_event(e):
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.pop()
        if e.key == SDLK_SPACE:
            generate_block()

def exit():
    pass

def pause():
    pass

def resume():
    build_world()

if __name__ == '__main__':
    gfw.run_main()
