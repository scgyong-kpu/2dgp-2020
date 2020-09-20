import gfw
from pico2d import *
from gobj import *

def enter():
    global grass, team
    grass = Grass()
    team = [ Boy() for i in range(11) ]

def update():
    for b in team: b.update()

def draw():
    grass.draw()
    for b in team: b.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        gfw.pop()

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
