from pico2d import *
import gfw

MOVE_PPS = 300
MAX_LIFE = 5

def init():
    global image, heart_red, heart_white
    image = gfw.image.load('res/player.png')
    heart_red = gfw.image.load('res/heart_red.png')
    heart_white = gfw.image.load('res/heart_white.png')

    global pos, delta_x, delta_y, radius
    pos = get_canvas_width() // 2, get_canvas_height() // 2
    delta_x, delta_y = 0, 0
    radius = image.w // 2

    global life
    life = MAX_LIFE

def increase_life(): # returns True if already full
    global life
    if life == MAX_LIFE:
        return True

    life += 1
    return False

def decrease_life(): # returns True if dead
    global life
    life -= 1
    # print(life)
    return life <= 0

def update():
    global pos
    x,y = pos
    x += delta_x * MOVE_PPS * gfw.delta_time
    y += delta_y * MOVE_PPS * gfw.delta_time
    hw, hh = image.w // 2, image.h // 2
    x = clamp(hw, x, get_canvas_width() - hw)
    y = clamp(hh, y, get_canvas_height() - hh)
    pos = x,y

def draw():
    image.draw(*pos)
    x, y = get_canvas_width() - 30, get_canvas_height() - 30
    for i in range(MAX_LIFE):
        # heart = i < life ? red : white
        heart = heart_red if i < life else heart_white
        heart.draw(x, y)
        x -= heart.w

def handle_event(e):
    global delta_x, delta_y
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_LEFT:
            delta_x -= 1
        elif e.key == SDLK_RIGHT:
            delta_x += 1
        elif e.key == SDLK_DOWN:
            delta_y -= 1
        elif e.key == SDLK_UP:
            delta_y += 1
    elif e.type == SDL_KEYUP:
        if e.key == SDLK_LEFT:
            delta_x += 1
        elif e.key == SDLK_RIGHT:
            delta_x -= 1
        elif e.key == SDLK_DOWN:
            delta_y += 1
        elif e.key == SDLK_UP:
            delta_y -= 1
