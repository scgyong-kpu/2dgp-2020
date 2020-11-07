import pico2d

def set_image_alpha(image, alpha):
    pico2d.SDL_SetTextureAlphaMod(image.texture, int(alpha))

def get_text_extent(font, text):
    w, h = c_int(), c_int()
    pico2d.TTF_SizeText(font.font, text.encode('utf-8'), ctypes.byref(w), ctypes.byref(h))
    return w.value, h.value

def draw_centered_text(font, text, l, b, w, h):
    tw, th = get_text_extent(font, text)
    tx = l + (w - tw) // 2
    ty = b + h // 2
    font.draw(tx, ty, text)

# def clear_with_color(rgb):
#     r = (rgb >> 16) & 0xFF
#     g = (rgb >> 8) & 0xFF
#     b = (rgb) & 0xFF
#     print('has? [', hasattr(pico2d, 'lattice_on'), ']')
#     # pico2d.SDL_FillRect(pico2d.renderer, None, pico2d.MapRGB(r, g, b))
