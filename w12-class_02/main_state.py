from pico2d import *
import gfw
import player
import bg
import generator
from collision import check_collision

SCORE_TEXT_COLOR = (255, 255, 255)
STATE_IN_GAME, STATE_GAME_OVER = range(2)

def enter():
    gfw.world.init(['bg', 'missile', 'item', 'player'])
    generator.init()

    bg.init()
    gfw.world.add(gfw.layer.bg, bg)
    player.init()
    gfw.world.add(gfw.layer.player, player)

    global game_over_image, font
    game_over_image = gfw.image.load('res/game_over.png')
    font = gfw.font.load('res/ConsolaMalgun.ttf', 35)

    global state, score
    state = STATE_IN_GAME
    score = 0

def end_game():
    global state
    state = STATE_GAME_OVER

def exit():
    pass

def update():
    global state, score
    if state != STATE_IN_GAME:
        return

    score += gfw.delta_time

    gfw.world.update()
    generator.update(score)
    dead, full = check_collision()
    if dead:
        end_game()
    if full:
        score += 5

def draw():
    gfw.world.draw()
    score_pos = 30, get_canvas_height() - 30
    font.draw(*score_pos, 'Score: %.1f' % score, SCORE_TEXT_COLOR)

    if state == STATE_GAME_OVER:
        x, y = get_canvas_width() // 2, get_canvas_height() // 2
        game_over_image.draw(x, y)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

if __name__ == '__main__':
    gfw.run_main()

