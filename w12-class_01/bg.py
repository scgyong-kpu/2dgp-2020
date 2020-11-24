from pico2d import *
import gfw

def init(p):
    global player, space, stars
    player = p
    space = gfw.image.load('res/outerspace.png')
    stars = gfw.image.load('res/stars.png')

def draw():
    x = get_canvas_width() // 2
    y = get_canvas_height() // 2
    px,py = player.pos
    dx,dy = x-px, y-py

    space.draw(x + dx * 0.02, y + dy * 0.02)
    stars.draw(x + dx * 0.05, y + dy * 0.05)

def update():
    pass
