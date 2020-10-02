import json
import gfw
from pico2d import *
from gobj import *
from galaga_sprite import Sprite

canvas_width = 500
canvas_height = 800

class ImageObject:
    def __init__(self, imageName, pos):
        self.image = gfw.image.load(res(imageName))
        self.pos = pos
    def draw(self):
        self.image.draw(*self.pos)
    def update(self):
        pass

def enter():
    gfw.world.init(['bg', 'enemy', 'player'])

    gfw.world.add(gfw.layer.bg, ImageObject('space.png', (250,400)))
    gfw.world.add(gfw.layer.player, Sprite('player', (250, 50)))

    with open(res('stage_01.json')) as f:
        data = json.load(f)
        for d in data:
            e = Sprite(d['name'], (d['x'], d['y']), True)
            gfw.world.add(gfw.layer.enemy, e)


def update():
    gfw.world.update()

def draw():
    gfw.world.draw()
    # gobj.draw_collision_box()

def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    if handle_mouse(e):
        return

# capture 가 설정되면 모든 마우스 이벤트는 capture 에게 전달된다
capture = None 

# 이벤트가 처리되었으면 True, 아니면 False 를 리턴한다
def handle_mouse(e):
    global capture
    if capture is not None:
        # capture 가 풀리기를 원하면 False 가 리턴된다
        holding = capture.handle_event(e)
        if not holding:
            capture = None
        return True

    for enemy in gfw.world.objects_at(gfw.layer.enemy):
        if enemy.handle_event(e):
            capture = enemy
            return True

    return False

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
