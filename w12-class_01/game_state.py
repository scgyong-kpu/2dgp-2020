from pico2d import *
import gfw
from player import Player

import random
from missile import Missile

import obj_gen
import bg
import highscore

STATE_IN_GAME, STATE_PAUSED, STATE_GAME_OVER = range(3)

def collides_distance(a, b):
    ax,ay = a.pos
    bx,by = b.pos
    dist_sq = (ax-bx)**2 + (ay-by)**2
    return dist_sq < (a.radius + b.radius)**2

def enter():
    gfw.world.init(['bg', 'missile', 'item', 'player', 'ui'])
    obj_gen.init()

    global player
    player = Player()
    gfw.world.add(gfw.layer.player, player)

    bg.init(player)
    gfw.world.add(gfw.layer.bg, bg)

    highscore.load()

    global music_bg, sound_item, sound_explosion
    music_bg = load_music('res/background.mp3')
    music_bg.set_volume(10)
    sound_item = load_wav('res/item.wav')
    sound_item.set_volume(10)
    sound_explosion = load_wav('res/explosion.wav')
    sound_explosion.set_volume(10)

    # music_bg.repeat_play()
    global game_state
    game_state = STATE_IN_GAME

    global game_over_image
    game_over_image = gfw.image.load('res/game_over.png')

    start_game()

def start_game():
    global game_state
    game_state = STATE_IN_GAME

    player.reset()
    gfw.world.clear_at(gfw.layer.missile)
    gfw.world.clear_at(gfw.layer.item)
    gfw.world.remove(highscore)

    music_bg.repeat_play()

def pause_game():
    global game_state
    game_state = STATE_PAUSED
    music_bg.pause()
    player.score = max(0, player.score - 2)

def resume_game():
    global game_state
    game_state = STATE_IN_GAME
    music_bg.resume()

def end_game():
    global game_state
    game_state = STATE_GAME_OVER
    music_bg.stop()
    highscore.add(player.score)
    gfw.world.add(gfw.layer.ui, highscore)

def exit():
    global music_bg, sound_item, sound_explosion
    del music_bg
    del sound_item
    del sound_explosion

def update():
    global game_state

    if game_state != STATE_IN_GAME:
        return

    gfw.world.update()
    obj_gen.update()

    for o in gfw.world.objects_at(gfw.layer.missile):
        if collides_distance(o, player):
            gfw.world.remove(o)
            sound_explosion.play()
            dead = player.decreate_life()
            if dead:
                # game over
                end_game()

    for o in gfw.world.objects_at(gfw.layer.item):
        if collides_distance(o, player):
            gfw.world.remove(o)
            sound_item.play()
            player.apply_item(o)

def draw():
    gfw.world.draw()
    if game_state == STATE_GAME_OVER:
        x = get_canvas_width() // 2
        y = get_canvas_height() * 2 // 3
        game_over_image.draw(x, y)

def handle_event(e):
    if e.type == SDL_QUIT:
        gfw.quit()
    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()
        elif e.key == SDLK_RETURN:
            if game_state == STATE_GAME_OVER:
                start_game()
            elif game_state == STATE_PAUSED:
                resume_game()
        elif e.key == SDLK_p:
            if game_state == STATE_IN_GAME:
                pause_game()

    player.handle_event(e)

if __name__ == '__main__':
    gfw.run_main()
