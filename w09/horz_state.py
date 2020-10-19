import random
import gfw
from pico2d import *
import gobj
from player import Player
from background import HorzScrollBackground
from platform import Platform
from jelly import Jelly
import stage_gen

canvas_width = 1120
canvas_height = 630

def enter():
    gfw.world.init(['bg', 'platform', 'enemy', 'item', 'player'])

    center = get_canvas_width() // 2, get_canvas_height() // 2

    for n, speed in [(1,10), (2,100), (3,150)]:
        bg = HorzScrollBackground('cookie_run_bg_%d.png' % n)
        bg.speed = speed
        gfw.world.add(gfw.layer.bg, bg)

    global player
    player = Player()
    player.bg = bg
    gfw.world.add(gfw.layer.player, player)

    stage_gen.load(gobj.res('stage_01.txt'))

paused = False
def update():
    if paused:
        return
    gfw.world.update()

    dx = -300 * gfw.delta_time

    for layer in range(gfw.layer.platform, gfw.layer.item + 1):
        for obj in gfw.world.objects_at(layer):
            obj.move(dx)

    check_items()
    check_obstacles()

    stage_gen.update(dx)

def check_items():
    for item in gfw.world.objects_at(gfw.layer.item):
        if gobj.collides_box(player, item):
            gfw.world.remove(item)
            break

def check_obstacles():
    for enemy in gfw.world.objects_at(gfw.layer.enemy):
        if enemy.hit: continue
        if gobj.collides_box(player, enemy):
            print('Hit', enemy)
            enemy.hit = True

def draw():
    gfw.world.draw()
    gobj.draw_collision_box()

def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
        return
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
            return
        elif e.key == SDLK_a:
            # player.pos = 150,650
            # for x, y in [(100,400),(400,300),(650,250),(900,200)]:
            for i in range(10):
                x = random.randint(100, 900)
                y = random.randint(200, 400)
                pf = Platform(Platform.T_3x1, x, y)
                gfw.world.add(gfw.layer.platform, pf)
        elif e.key == SDLK_p:
            global paused
            paused = not paused

    if player.handle_event(e):
        return

def exit():
    pass



if __name__ == '__main__':
    gfw.run_main()
