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
    if capture is not None:
        capture.draw_position()

def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
        return
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
            return

    if handle_mouse(e):
        return

    if handle_command(e):
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

def handle_command(e):
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_s:
            save_enemies()
        elif e.key >= SDLK_1 and e.key <= SDLK_4:
            create_enemy(e.key - SDLK_1)

def exit():
    pass

SPRITE_NAMES = [ 
    "commander_green", 
    "commander_blue", 
    "butterfly", 
    "bee_yellow"
]

def create_enemy(index):
    name = SPRITE_NAMES[index]
    print(name)
    pos = get_canvas_width() // 2, get_canvas_height() // 2
    gfw.world.add(gfw.layer.enemy, Sprite(name, pos, True))

def save_enemies():
    enemies = gfw.world.objects_at(gfw.layer.enemy)
    js_enemies = [e.dictionary() for e in enemies]

    with open('enemies.json', 'w') as f:
        json.dump(js_enemies, f, indent=2)

if __name__ == '__main__':
    gfw.run_main()
