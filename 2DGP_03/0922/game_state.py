import gfw
from pico2d import *
from gobj import *

def enter():
    global grass, boy
    grass = Grass()
    boy = Boy()

def update():
    boy.update()
    for b in balls: b.update()

def draw():
    grass.draw()
    boy.draw()
    for b in balls: b.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.pop()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
        boy.fire()

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
