import random
from pico2d import *

RES_DIR = '../res'

class Boy:
	def __init__(self):
		#self.x, self.y = get_canvas_width() // 2, 85
		self.x, self.y = random.randint(100, 700), random.randint(100, 500)
		self.image = load_image(RES_DIR + '/run_animation.png')
		self.dx = random.random()
		self.fidx = random.randint(0, 7)
	def draw(self):
		self.image.clip_draw(self.fidx * 100, 0, 100, 100, self.x, self.y)
	def update(self):
		self.x += self.dx * 5
		self.fidx = (self.fidx + 1) % 8

class Grass:
	def __init__(self):
		self.x, self.y = 400, 30
		self.image = load_image(RES_DIR + '/grass.png')
	def draw(self):
		self.image.draw(self.x, self.y)

# print("Hello. this is gobj.py")
# print("My name is:", __name__)
if __name__ == '__main__':
	print("Not imported")