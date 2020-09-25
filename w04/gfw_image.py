from pico2d import *

images = {}

def load(file):
    global images
    if file in images:
        return images[file]

    image = load_image(file)
    images[file] = image
    return image

def unload(file):
    global images
    if file in images:
        del images[file]
