import random
from pico2d import *
import gfw
import gobj
from card import Card

SCORE_HEIGHT = 30
PADDING = 10
canvas_width = PADDING + (Card.WIDTH + PADDING) * 5
canvas_height = PADDING + (Card.WIDTH + PADDING) * 4 + SCORE_HEIGHT

print("Canvas Size:", (canvas_width, canvas_height))

start_x = Card.WIDTH // 2 + PADDING
start_y = Card.HEIGHT // 2 + PADDING

def enter():
    gfw.world.init(['bg', 'card'])
    center = get_canvas_width()//2, get_canvas_height()//2
    gfw.world.add(gfw.layer.bg, gobj.ImageObject('bg.png', center))

    x,y = start_x, start_y
    idxs = [n + 1 for n in range(10)] * 2
    print('before:', idxs)
    random.shuffle(idxs)
    print('after: ', idxs)
    for i in idxs:
        c = Card(i, (x,y))
        gfw.world.add(gfw.layer.card, c)
        x += Card.WIDTH + PADDING
        if x > get_canvas_width():
            x = start_x
            y += Card.HEIGHT + PADDING

    global last_card
    last_card = None

def update():
    gfw.world.update()

def draw():
    gfw.world.draw()

def handle_event(e):
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.quit()

    global last_card
    for card in gfw.world.objects_at(gfw.layer.card):
        if card == last_card:
            continue
        if card.handle_event(e):
            if last_card is None:
                last_card = card
                break
            last_card.toggle()
            last_card = card

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
