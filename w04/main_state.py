import gfw
from pico2d import *
from boy import Boy

def enter():
    global grass, boy
    boy = Boy()

def update():
    boy.update()

def draw():
    boy.draw()

def handle_event(e):
    global boy
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    boy.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
