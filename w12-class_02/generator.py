from pico2d import *
import gfw
from missile import *
import random

MISSILE_COUNT = 10
ITEM_COUNT = 2

def init():
    pass

def update(s):
    global score
    score = s
    print('count=', gfw.world.count_at(gfw.layer.item))
    max_missile_count = MISSILE_COUNT + score // 10
    while gfw.world.count_at(gfw.layer.missile) < max_missile_count:
        generate_missile()
    while gfw.world.count_at(gfw.layer.item) < ITEM_COUNT:
        generate_item()

def generate_missile():
    x,y,dx,dy = get_coords()
    m = Missile((x,y), (dx,dy))
    gfw.world.add(gfw.layer.missile, m)

def generate_item():
    x,y,dx,dy = get_coords()
    Item = random.choice([PresentItem, CoinItem])
    m = Item((x,y), (dx,dy))
    gfw.world.add(gfw.layer.item, m)

def get_coords():
    x = random.randrange(get_canvas_width())
    y = random.randrange(get_canvas_height())
    dx = random.random()
    if dx < 0.5: dx -= 1
    dy = random.random()
    if dy < 0.5: dy -= 1

    speed = 1 + score / 60
    dx *= speed
    dy *= speed

    side = random.randint(1,4)
    if side == 1: # left
        x = 0
    elif side == 2: # bottom
        y = 0
    elif side == 3: # right
        x = get_canvas_width()
    else:
        y = get_canvas_height()

    return x,y,dx,dy
