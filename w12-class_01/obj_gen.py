import random
from pico2d import *
import gfw
from missile import *
from player import Player

BORDER = 30
MAX_MISSILE_COUNT = 10
MAX_ITEM_COUNT = 2

def init():
    global BOUNDARY_LEFT, BOUNDARY_RIGHT, BOUNDARY_DOWN, BOUNDARY_UP
    BOUNDARY_LEFT = -BORDER
    BOUNDARY_DOWN = -BORDER
    BOUNDARY_RIGHT = get_canvas_width() + BORDER
    BOUNDARY_UP = get_canvas_height() + BORDER

def get_border_coords():
    cw, ch = get_canvas_width(), get_canvas_height()
    dx = random.random()
    if dx < 0.5: dx -= 1 # dx: -1.0~-0.5 +0.5~+1.0
    dy = random.random()
    if dy < 0.5: dy -= 1 # dy: -1.0~-0.5 +0.5~+1.0

    score = Player.player.score
    speed = 1 + score / 60
    dx *= speed
    dy *= speed

    side = random.randint(1, 4)
    if side == 1: # left
        x = -BORDER
        y = random.random() * ch
        if dx < 0: dx = -dx
    elif side == 2: # bottom
        x = random.random() * cw
        y = -BORDER
        if dy < 0: dy = -dy
    elif side == 3: # right
        x = cw + BORDER
        y = random.random() * ch
        if dx > 0: dx = -dx
    else: # side == 4, up
        x = random.random() * cw
        y = ch + BORDER
        if dy > 0: dy = -dy

    return x, y, dx, dy

def generate_missile():
    x, y, dx, dy = get_border_coords()
    mag = random.uniform(0.5, 1.0)
    m = Missile((x,y), (dx,dy), mag)
    gfw.world.add(gfw.layer.missile, m)

def generate_item():
    x, y, dx, dy = get_border_coords()
    Item = random.choice([PresentItem, CoinItem])
    m = Item((x,y), (dx,dy))
    gfw.world.add(gfw.layer.item, m)

def update():
    score = Player.player.score
    max_missile_count = MAX_MISSILE_COUNT + score // 10
    if gfw.world.count_at(gfw.layer.missile) < max_missile_count:
        generate_missile()

    if gfw.world.count_at(gfw.layer.item) < MAX_ITEM_COUNT:
        generate_item()
