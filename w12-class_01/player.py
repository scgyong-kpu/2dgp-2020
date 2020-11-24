from pico2d import *
import gfw

MOVE_PPS = 300
MAX_LIFE = 5
SCORE_TEXT_COLOR = (255, 255, 255)

class Player:
    def __init__(self):
        self.image = gfw.image.load('res/player.png')
        self.font = gfw.font.load('res/ConsolaMalgun.ttf', 35)
        self.radius = self.image.h // 2
        self.heart_red = gfw.image.load('res/heart_red.png')
        self.heart_white = gfw.image.load('res/heart_white.png')
        self.reset()

        global BOUNDARY_LEFT, BOUNDARY_RIGHT, BOUNDARY_DOWN, BOUNDARY_UP
        BOUNDARY_LEFT = self.image.w // 2
        BOUNDARY_DOWN = self.image.h // 2
        BOUNDARY_RIGHT = get_canvas_width() - BOUNDARY_LEFT
        BOUNDARY_UP = get_canvas_height() - BOUNDARY_DOWN

        Player.player = self

    def reset(self):
        self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.dx, self.dy = 0, 0
        self.life = MAX_LIFE
        self.score = 0

    def update(self):
        self.score += gfw.delta_time
        x,y = self.pos
        x += self.dx * MOVE_PPS * gfw.delta_time
        y += self.dy * MOVE_PPS * gfw.delta_time
        x = clamp(BOUNDARY_LEFT, x, BOUNDARY_RIGHT)
        y = clamp(BOUNDARY_DOWN, y, BOUNDARY_UP)
        self.pos = x,y
    def draw(self):
        self.image.draw(*self.pos)
        x = get_canvas_width() - 30
        y = get_canvas_height() - 30
        for i in range(MAX_LIFE):
            heart = self.heart_red if i < self.life else self.heart_white
            heart.draw(x, y)
            x -= heart.w
        pos = 30, get_canvas_height() - 30
        self.font.draw(*pos, 'Score: %.1f' % self.score, SCORE_TEXT_COLOR)
    def apply_item(self, item): # returns True if already full
        if self.life == MAX_LIFE:
            self.score += item.score
            return True
        self.life += 1
        return False
    def decreate_life(self): # returns True if dead
        self.life -= 1
        return self.life <= 0

    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                self.dx -= 1
            elif e.key == SDLK_RIGHT:
                self.dx += 1
            elif e.key == SDLK_DOWN:
                self.dy -= 1
            elif e.key == SDLK_UP:
                self.dy += 1
        elif e.type == SDL_KEYUP:
            if e.key == SDLK_LEFT:
                self.dx += 1
            elif e.key == SDLK_RIGHT:
                self.dx -= 1
            elif e.key == SDLK_DOWN:
                self.dy += 1
            elif e.key == SDLK_UP:
                self.dy -= 1
