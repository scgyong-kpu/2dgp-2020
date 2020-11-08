import pickle
from pico2d import *
import time
import gfw
import gobj

FILENAME = 'data.pickle'
scores = []
MAX_SCORE_COUNT = 10
last_rank = -1

class Entry:
    def __init__(self, score):
        self.score = score
        self.time = time.time()

def load():
    global font, image
    font = gfw.font.load(gobj.res('ConsolaMalgun.ttf'), 20)
    image = gfw.image.load(gobj.res('game_over.png'))

    global scores
    try:
        f = open(FILENAME, "rb")
        scores = pickle.load(f)
        f.close()
        print("Scores:", scores)
    except:
        print("No highscore file")

def save():
    f = open(FILENAME, "wb")
    pickle.dump(scores, f)
    f.close()

def add(score):
    global scores, last_rank
    entry = Entry(score)
    inserted = False
    for i in range(len(scores)):
        e = scores[i]
        if e.score < entry.score:
            scores.insert(i, entry)
            inserted = True
            last_rank = i + 1
            break
    if not inserted:
        scores.append(entry)
        last_rank = len(scores)

    if (len(scores) > MAX_SCORE_COUNT):
        scores.pop(-1)
    if last_rank <= MAX_SCORE_COUNT:
        save()

def draw():
    global font, image, last_rank
    image.draw_to_origin(0, 0)
    no = 1
    y = 360
    for e in scores:
        str = "{:2d} {:10d}".format(no, e.score)
        color = (255, 255, 128) if no == last_rank else (223, 255, 223)
        font.draw(30, y, str, color)
        font.draw(220, y, time.asctime(time.localtime(e.time)), color)
        y -= 30
        no += 1

def update():
    pass
