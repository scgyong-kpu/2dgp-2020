import random
from pico2d import *

RES_DIR = '../res'

class Grass:
    def __init__(self):
        self.image = load_image(RES_DIR + '/grass.png')
    def draw(self):
        self.image.draw(400, 30)
    def update(self):
        pass

class Ball:
    balls = []
    def __init__(self, x, y, dx, dy):
        self.image = load_image(RES_DIR + '/ball21x21.png')
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        self.x += self.dx
        self.y += self.dy

class Boy:
    #constructor
    # def __init__(self, pos, delta):
    # 	self.x, self.y = pos
    # 	self.dx, self.dy = delta
    def __init__(self):
        self.x = get_canvas_width() // 2
        self.y = get_canvas_height() // 2
        self.dx, self.dy = 0, 0
        self.fidx = random.randint(0, 7)
        self.image = load_image(RES_DIR + '/animation_sheet.png')
        self.action = 3
    def draw(self):
        sx = self.fidx * 100
        sy = self.action * 100
        self.image.clip_draw(sx, sy, 100, 100, self.x, self.y)
    def update(self):
        # if self.dx < 0:
        # 	self.action = 0
        # elif self.dx > 0:
        # 	self.action = 1
        # else:
        # 	self.action = 3
        self.x += self.dx
        self.y += self.dy
        self.fidx = (self.fidx + 1) % 8
    def fire(self):
        ball = Ball(self.x, self.y, self.dx, self.dy)
        Ball.balls.append(ball)
        print('Ball count = %d' % len(Ball.balls))
    def handle_event(self, e):
        prev_dx = self.dx
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                self.dx -= 1
            elif e.key == SDLK_RIGHT:
                self.dx += 1
            elif e.key == SDLK_DOWN:
                self.dy -= 1
            elif e.key == SDLK_UP:
                self.dy += 1
            elif e.key == SDLK_SPACE:
                self.fire()
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                self.dx += 1
            elif e.key == SDLK_RIGHT:
                self.dx -= 1
            elif e.key == SDLK_DOWN:
                self.dy += 1
            elif e.key == SDLK_UP:
                self.dy -= 1

        if prev_dx != self.dx:
            if self.dx < 0:
                self.action = 0
            elif self.dx > 0:
                self.action = 1
            elif prev_dx < 0:
                self.action = 2
            elif prev_dx > 0:
                self.action = 3

if __name__ == "__main__":
	print("Running test code ^_^")
