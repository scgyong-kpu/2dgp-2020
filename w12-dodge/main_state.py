from pico2d import *
import gfw
import player
import generator

def enter():
    gfw.world.init(['bg', 'missile', 'player'])
    player.init()
    gfw.world.add(gfw.layer.player, player)

def exit():
    pass

def update():
    gfw.world.update()
    generator.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

if __name__ == '__main__':
    gfw.run_main()
