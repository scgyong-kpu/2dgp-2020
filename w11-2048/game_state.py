from pico2d import *
from ext_pico2d import *
import gfw
import gobj
import board

def build_world():
    gfw.world.init(['bg', 'block', 'ui'])
    bg = gobj.ImageBackground('FF9F49.png')
    gfw.world.add(gfw.layer.bg, bg)

def generate_block():
    x,y,n = board.generate_block()
    if n == 0: return

    x = x * 120 + 80
    y = y * 120 + 80
    fn = 'block_%05d.png' % n
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
