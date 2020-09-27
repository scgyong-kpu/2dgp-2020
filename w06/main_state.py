import gfw
from pico2d import *
from player import Player
from zombie import Zombie
import gobj

canvas_width = 1280
canvas_height = 960

def enter():
    gfw.world.init(['bg', 'zombie', 'player'])
    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    bg = gobj.ImageObject('kpu_1280x960.png', (canvas_width // 2, canvas_height // 2))
    gfw.world.add(gfw.layer.bg, bg)

    global zombie_time
    zombie_time = 1

    Zombie.load_all_images()

def update():
    gfw.world.update()

    global zombie_time
    zombie_time -= gfw.delta_time
    if zombie_time <= 0:
        gfw.world.add(gfw.layer.zombie, Zombie())
        zombie_time = 5

def draw():
    gfw.world.draw()
    # gobj.draw_collision_box()
    
def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
