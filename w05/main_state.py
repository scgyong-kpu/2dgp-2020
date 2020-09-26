import random
import gfw
from pico2d import *
from player import Player
from bullet import LaserBullet
from enemy import Enemy

canvas_width = 500
canvas_height = 800

def enter():
    global grass, player
    player = Player()

    set_next_enemy_gen_time()

def set_next_enemy_gen_time():
    global enemy_gen_time
    enemy_gen_time = random.uniform(1, 2)

def generate_enemy_if_timed_out():
    global enemy_gen_time
    enemy_gen_time -= gfw.delta_time
    if enemy_gen_time > 0: return

    x = random.randint(0, get_canvas_width())
    e = Enemy(x, -1)
    Enemy.enemies.append(e)
    set_next_enemy_gen_time()

def update():
    player.update()
    for e in Enemy.enemies: e.update()
    for b in LaserBullet.bullets: b.update()
    generate_enemy_if_timed_out()


def draw():
    for e in Enemy.enemies: e.draw()
    for b in LaserBullet.bullets: b.draw()
    player.draw()

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
