from pico2d import *

# pivot or origin

open_canvas()

gra = load_image('grass.png')
ch = load_image('character.png')

gra.draw_now(400, 30)
for y in range(0, 600+1, 100):
	for x in range(0, 800+1, 100):
		ch.draw_now(x, y)

delay(2) # in seconds

clear_canvas_now()

delay(2) # in seconds

close_canvas()
