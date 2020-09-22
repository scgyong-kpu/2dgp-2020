import gfw
from pico2d import *
from gobj import *

def enter():
    global grass, boy
    grass = Grass()
    boy = Boy()

def update():
    boy.update()

def draw():
    grass.draw()
    boy.draw()

def handle_event(e):
    global boy
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_LEFT:
            boy.dx -= 1
        elif e.key == SDLK_RIGHT:
            boy.dx += 1
        elif e.key == SDLK_DOWN:
            boy.dy -= 1
        elif e.key == SDLK_UP:
            boy.dy += 1
    elif e.type == SDL_KEYUP:
        if e.key == SDLK_LEFT:
            boy.dx += 1
        elif e.key == SDLK_RIGHT:
            boy.dx -= 1
        elif e.key == SDLK_DOWN:
            boy.dy += 1
        elif e.key == SDLK_UP:
            boy.dy -= 1

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
