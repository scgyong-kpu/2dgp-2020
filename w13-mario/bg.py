from pico2d import *
import gfw

scroll_x, scroll_y = 0, 0

def update():
    pass

def draw():
    pass

def to_screen(pos):
    x, y = pos
    return x - scroll_x, y - scroll_y

def to_logic(pos):
    x, y = pos
    return x + scroll_x, y + scroll_y

def scroll(dx, dy):
    global scroll_x, scroll_y
    scroll_x += dx
    scroll_y += dy
