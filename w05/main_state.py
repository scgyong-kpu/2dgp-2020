import gfw
from pico2d import *
from player import Player
from bullet import LaserBullet
from score import Score
import gobj
import enemy_gen
import life_gauge

canvas_width = 500
canvas_height = 800

def enter():
    gfw.world.init(['bg', 'enemy', 'bullet', 'player', 'ui'])
    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    global score
    score = Score(canvas_width - 20, canvas_height - 50)
    gfw.world.add(gfw.layer.ui, score)

    global font
    font = gfw.font.load(gobj.RES_DIR + '/segoeprb.ttf', 40)

    life_gauge.load()

def check_enemy(e):
    if gobj.collides_box(player, e):
        print('Player Collision', e)
        e.remove()
        return

    for b in gfw.gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(b, e):
            # print('Collision', e, b)
            dead = e.decrease_life(b.power)
            if dead:
                score.score += e.level * 10
                e.remove()
            b.remove()
            return

def update():
    gfw.world.update()
    enemy_gen.update()

    for e in gfw.world.objects_at(gfw.layer.enemy):
        check_enemy(e)

def draw():
    gfw.world.draw()
    # gobj.draw_collision_box()
    font.draw(20, canvas_height - 45, 'Wave: %d' % enemy_gen.wave_index)

def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
