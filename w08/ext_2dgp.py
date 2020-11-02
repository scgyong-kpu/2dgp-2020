from pico2d import *

def set_image_alpha(image, alpha):
    SDL_SetTextureAlphaMod(image.texture, int(alpha))
