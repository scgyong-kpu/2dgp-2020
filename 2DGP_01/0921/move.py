from pico2d import *
from gobj import *

# pivot or origin


def handle_events():
	global running
	evts = get_events()
	for e in evts:
		if e.type == SDL_QUIT:
			running = False
		elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
			running = False

open_canvas()

grass = Grass()
team = [ Boy() for i in range(11) ] 
# for i in range(11):
# 	team.append(Boy())

# objects = [ grass, boy, b2 ]

running = True
while running:
	clear_canvas()
	grass.draw()
	for b in team: b.draw()
	update_canvas()

	handle_events()

	for b in team: b.update()

	# if boy.x > get_canvas_width():
	# 	running = False


	delay(0.02)

# delay(1) # in seconds

close_canvas()

# turtle.onkey(some_function, 'w')
# turtle.onkey(other_function, 's')
# turtle.listen()


# game loop
# - logic = update()
# - render = draw()
