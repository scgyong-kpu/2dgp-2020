from pico2d import *

# pivot or origin

open_canvas()

gra = load_image('grass.png')
ch = load_image('animation_sheet.png')


x = 0
frame_index = 0
action = 0
while x < 800:
	clear_canvas()
	gra.draw(400, 30)
	ch.clip_draw(100 * frame_index, 100 * action, 100, 100, x, 85)
	update_canvas()

	get_events()
	# for e in evts:
	# 	print(e)

	x += 2
	# frame_index += 1
	# if frame_index >= 8: frame_index = 0
	frame_index = (frame_index + 1) % 8

	if x % 100 == 0:
		action = (action + 1) % 4

	delay(0.02)

delay(1) # in seconds

close_canvas()

# turtle.onkey(some_function, 'w')
# turtle.onkey(other_function, 's')
# turtle.listen()


# game loop
# - logic = update()
# - render = draw()
