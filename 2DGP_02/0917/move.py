from pico2d import *

# angle = 30
# length = 0.1
# dx = 0.1 * cos(30 * 3.14592 / 180)
# dy = 0.1 * sin(30 * 3.14592 / 180)
# dx = 0.1
# dy = 0.05


# x = 100
# y = 200
# dx = 0

while True:
	x += dx
	y += dy
	if jump:
		dy = 100
	dy -= 1
	if y < 85:
		dy = 0


def handle_events():
	global running, x, y, dx
	events = get_events()
	for e in events:
		if e.type == SDL_QUIT:
			running = False
		elif e.type == SDL_KEYDOWN:
			if e.key == SDLK_ESCAPE:
				running = False
			elif e.key == SDLK_LEFT:
				dx -= 1
			elif e.key == SDLK_RIGHT:
				dx += 1
		elif e.type == SDL_KEYUP:
			if e.key == SDLK_LEFT:
				dx += 1
			elif e.key == SDLK_RIGHT:
				dx -= 1
		elif e.type == SDL_MOUSEMOTION:
			x,y = e.x,get_canvas_height() - e.y - 1

open_canvas()

gra = load_image('../../res/grass.png')
ch = load_image('../../res/run_animation.png')

x,y = get_canvas_width() // 2, 85
dx = 0
fidx = 0
running = True
while running:
	clear_canvas()
	gra.draw(400, 30)
	ch.clip_draw(fidx * 100, 0, 100, 100, x, y)
	update_canvas()

	handle_events()
	# print(events)

	x += dx * 5
	fidx = (fidx + 1) % 8

	# x += 2
	# if x >= get_canvas_width():
	# 	break	

	delay(0.01)

close_canvas()
