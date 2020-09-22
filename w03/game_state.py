import gfw
from pico2d import *
from gobj import *
from ball import Ball
from boy import Boy

def enter():
    global grass, boy
    grass = Grass()
    boy = Boy()

def update():
    boy.update()
    for b in Ball.balls: b.update()

def draw():
    grass.draw()
    for b in Ball.balls: b.draw()
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
    #Boy.handle_event(boy, e)

    # print(balls)
def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
