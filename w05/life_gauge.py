from pico2d import *
import gfw
import gobj

def load():
    global bg, fg
    bg = gfw.image.load(gobj.RES_DIR + '/gauge_bg.png')
    fg = gfw.image.load(gobj.RES_DIR + '/gauge_fg.png')

def draw(x, y, width, rate):
    bg.draw(x, y, width, bg.h)
    w = round(width * rate) - 4
    fg.draw(x, y, w, fg.h)
