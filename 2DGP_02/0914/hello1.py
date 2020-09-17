from pico2d import *

open_canvas()

ch = load_image('../res/character.png')

for y in range(100, 501, 100):
    for x in range(100, 701, 100):
        delay(0.05)
        print(x, y)
        ch.draw(x, y)

update_canvas()
delay(2) # in seconds

close_canvas()

# origin or pivot
