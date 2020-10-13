import gfw
from platform import Platform
from jelly import Jelly
import gobj

UNIT_PER_LINE = 100
SCREEN_LINES = 10

lines = []

def load(file):
    global lines
    with open(file, 'r') as f:
        lines = f.readlines()

def count():
    return len(lines) // SCREEN_LINES * UNIT_PER_LINE

def get(x, y):
    col = x % UNIT_PER_LINE
    row = x // UNIT_PER_LINE * SCREEN_LINES + SCREEN_LINES - 1 - y
    return lines[row][col]

def test_gen():
    load(gobj.res('stage_01.txt'))
    print('count=', count())
    line = 0
    for x in range(200):
        s = ''
        for y in range(10):
            s += get(x,y)
        line += 1
        print('%03d:' % line, s)

if __name__ == '__main__':
    test_gen()