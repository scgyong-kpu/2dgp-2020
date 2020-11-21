import random
from pico2d import *
from ext_pico2d import *
import gfw
import gobj
import board
from block import Block
from score import Score
import highscore

canvas_width = 520
canvas_height = 600

IN_GAME, GAME_OVER = range(2)
state = IN_GAME

def build_world():
    gfw.world.init(['bg', 'block', 'highscore', 'ui'])
    bg = gobj.ImageBackground('FF9F49.png')
    gfw.world.add(gfw.layer.bg, bg)

    global score
    score = Score(get_canvas_width() - 20, get_canvas_height() - 50)
    gfw.world.add(gfw.layer.ui, score)

    highscore.load()

def generate_block():
    if board.is_full(): return

    value = random.choice([2, 4])
    block = Block(value)
    x,y = board.generate_block(block)
    block.move_to(x, y, False)

    gfw.world.add(gfw.layer.block, block)

def move_board(convert):
    global state
    if state == GAME_OVER:
        return

    moved, score_inc = board.move(convert)
    if moved:
        generate_block()

    score.score += score_inc

    if board.is_full() and not board.can_reduce():
        end_game()

def start_game():
    global state
    if state != GAME_OVER:
        return

    board.reset()
    gfw.world.clear_at(gfw.layer.block)
    global score
    score.reset()
    gfw.world.remove(highscore)

    state = IN_GAME
    generate_block()

def end_game():
    global state
    if state != IN_GAME:
        return
    state = GAME_OVER
    print("Game Over")
    board.slow_down_animation()
    highscore.add(score.score)
    gfw.world.add(gfw.layer.highscore, highscore)

def enter():
    build_world()
    generate_block()

def update():
    gfw.world.update()
    board.update()

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
        elif e.key == SDLK_RETURN:
            start_game()
        elif e.key == SDLK_e:
            end_game()

def exit():
    pass

def pause():
    pass

def resume():
    build_world()

if __name__ == '__main__':
    gfw.run_main()
