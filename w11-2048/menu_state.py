from pico2d import *
from ext_pico2d import *
import gfw
import gobj

def build_world():
    gfw.world.init(['bg', 'ui'])
    bg = gobj.ImageBackground('FF9F49.png')
    gfw.world.add(gfw.layer.bg, bg)

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

def exit():
    pass

def pause():
    pass

def resume():
    build_world()

if __name__ == '__main__':
    gfw.run_main()
