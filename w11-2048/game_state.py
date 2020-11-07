import random
from pico2d import *
from ext_pico2d import *
import gfw
import gobj
import board
from block import Block
from score import Score

canvas_width = 520
canvas_height = 600

def build_world():
    gfw.world.init(['bg', 'block', 'ui'])
    bg = gobj.ImageBackground('FF9F49.png')
    gfw.world.add(gfw.layer.bg, bg)

    global score
    score = Score(get_canvas_width() - 20, get_canvas_height() - 50)
    gfw.world.add(gfw.layer.ui, score)

def generate_block():
    if board.is_full(): return

    value = random.choice([2, 4])
    block = Block(value)
    x,y = board.generate_block(block)
    block.move_to(x, y, False)

    gfw.world.add(gfw.layer.block, block)

def move_board(convert):
    moved, score_inc = board.move(convert)
    if moved:
        generate_block()

    score.score += score_inc

def enter():
    build_world()
    generate_block()

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()
    
def handle_event(e):
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.pop()
        # if e.key == SDLK_SPACE:
        #     generate_block()
        elif e.key == SDLK_LEFT:
            move_board(lambda x,y: (x,y))
        elif e.key == SDLK_RIGHT:
            move_board(lambda x,y: (3-x,y))
        elif e.key == SDLK_DOWN:
            move_board(lambda x,y: (y,x))
        elif e.key == SDLK_UP:
            move_board(lambda x,y: (3-y,3-x))

def exit():
    pass

def pause():
    pass

def resume():
    build_world()

if __name__ == '__main__':
    gfw.run_main()
