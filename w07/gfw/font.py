from pico2d import *

fonts = {}

def load(file, size):
    key = file + '_' + str(size)
    global fonts
    if key in fonts:
        return fonts[key]

    font = load_font(file, size)
    fonts[key] = font
    return font

def unload(file, size):
    key = file + '_' + str(size)
    global fonts
    if key in fonts:
        del fonts[key]
