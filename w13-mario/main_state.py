from pico2d import *
import gfw
import map_loader
import bg

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
        elif e.key == SDLK_LEFT:
            bg.scroll(-100, 0)
        elif e.key == SDLK_RIGHT:
            bg.scroll(100, 0)
        elif e.key == SDLK_DOWN:
            bg.scroll(0, -100)
        elif e.key == SDLK_UP:
            bg.scroll(0, 100)


if __name__ == '__main__':
    gfw.run_main()
