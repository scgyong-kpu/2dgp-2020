import gfw
from pico2d import *
from gobj import *
import title_state

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
        gfw.change(title_state)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
    