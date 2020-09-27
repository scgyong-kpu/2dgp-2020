from pico2d import *
import gfw
from gobj import *

class Score:
    bullets = []
    trashcan = []
    def __init__(self, right, y):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.right, self.y = right, y
        self.image = gfw.image.load(RES_DIR + '/number_24x32.png')
        self.digit_width = self.image.w // 10
        self.reset()

    def reset(self):
        self.score = 0
        self.display = 0

    def draw(self):
        x = self.right
        score = self.display
        while score > 0:
            digit = score % 10
            sx = digit * self.digit_width
            # print(type(sx), type(digit), type(self.digit_width))
            x -= self.digit_width
            self.image.clip_draw(sx, 0, self.digit_width, self.image.h, x, self.y)
            score //= 10

    def update(self):
    	if self.display < self.score:
            self.display += 1
