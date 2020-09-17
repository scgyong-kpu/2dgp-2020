from pico2d import *

open_canvas()

gra = load_image('../res/grass.png')
cha = load_image('../res/animation_sheet.png')

x = 0
frame_index = 0
action = 0
while x < 800:
    clear_canvas()
    gra.draw(400, 30)
    cha.clip_draw(100 * frame_index, 100 * action, 100, 100, x, 85)
    update_canvas()

    get_events()

    x += 2
    if x % 100 == 0:
        action = (action + 1) % 4

    frame_index = (frame_index + 1) % 8

    delay(0.03)

# delay(2) # in seconds
# frame animation
close_canvas()
