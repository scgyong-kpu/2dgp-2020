from pico2d import *

open_canvas()

gra = load_image('../res/grass.png')
cha = load_image('../res/character.png')

x = 0
while x < 800:
    clear_canvas()
    gra.draw(400, 30)
    cha.draw(x, 85)
    update_canvas()

    get_events()

    x += 2

    delay(0.01)

# delay(2) # in seconds
# frame animation
close_canvas()

# game loop:
#   - update() - logic
#   - draw() - render

# game loop:
#   - update() - logic
#   - event handling
#   - draw() - render