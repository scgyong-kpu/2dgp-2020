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

class Boy:
	#constructor
	# def __init__(self, pos, delta):
	# 	self.x, self.y = pos
	# 	self.dx, self.dy = delta
	def __init__(self):
		self.x = random.randint(100, 300) 
		self.y = random.randint(100, 300)
		self.dx, self.dy = random.random(), random.random()
		self.fidx = random.randint(0, 7)
		self.image = load_image(RES_DIR + '/run_animation.png')
	def draw(self):
		self.image.clip_draw(self.fidx * 100, 0, 100, 100, self.x, self.y)
	def update(self):
		self.x += self.dx
		self.y += self.dy
		self.fidx = (self.fidx + 1) % 8

if __name__ == "__main__":
	print("Running test code ^_^")
