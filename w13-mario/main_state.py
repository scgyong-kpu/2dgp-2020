from pico2d import *
import gfw

def enter():
    gfw.world.init(['bg', 'platform', 'item', 'player', 'ui'])

def exit():
    pass

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

if __name__ == '__main__':
    gfw.run_main()
