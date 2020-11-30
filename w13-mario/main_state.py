from pico2d import *
import gfw
import map_loader

def enter():
    gfw.world.init(['bg', 'platform', 'item', 'player', 'ui'])
    map_loader.load()

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
