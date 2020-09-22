from pico2d import *
from gobj import *
import gfw_image

class Ball:
    balls = []
    def __init__(self, pos, delta, big=False):
        imageName = '/ball41x41.png' if big else '/ball21x21.png'
        self.image = gfw_image.load(RES_DIR + imageName)
        self.pos = pos
        self.delta = delta
        self.radius = self.image.h // 2
        # print('Radius = %d' % self.radius)
    def draw(self):
        self.image.draw(*self.pos)
    def update(self):
        x,y = self.pos
        dx,dy = self.delta
        x += dx
        y += dy
        gravity = 0.1
        dy -= gravity

        bottom = y - self.radius
        if bottom < 50 and dy < 0:
            dy *= rand(-0.8)
            if dy <= 1:
                dy = 0

        if x < -100 or x > get_canvas_width() + 100:
            Ball.balls.remove(self)
            print('Ball count - %d' % len(Ball.balls))

        self.pos = x, y
        self.delta = dx, dy
    