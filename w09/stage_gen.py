import gfw
from pico2d import *
from platform import Platform
from jelly import Jelly
import gobj
from factory import Factory

UNIT_PER_LINE = 100
SCREEN_LINES = 10
BLOCK_SIZE = 60

factory = None
lines = []

def load(file):
    global factory
    if factory is None:
        factory = Factory()

    global lines, current_x, create_at, map_index
    with open(file, 'r') as f:
        lines = f.readlines()
    current_x = 0
    map_index = 0
    create_at = get_canvas_width() + 2 * BLOCK_SIZE

def count():
    return len(lines) // SCREEN_LINES * UNIT_PER_LINE

def update(dx):
    global current_x, create_at
    current_x += dx
    while current_x < create_at:
        create_column()

def create_column():
    global current_x, map_index
    y = BLOCK_SIZE // 2;
    for row in range(SCREEN_LINES):
        ch = get(map_index, row)
        create_object(ch, current_x, y)
        y += BLOCK_SIZE
    current_x += BLOCK_SIZE
    map_index += 1
    # print('map_index:', map_index)
ignore_char_map = set()
def create_object(ch, x, y):
    if ch in ['1','2','3','4']:
        obj = Jelly(ord(ch) - ord('1'), x, y)
        gfw.world.add(gfw.layer.item, obj)
        # print('creating Jelly', x, y)
    elif ch in ['O','P','Q']:
        dy = 1 if ch == 'Q' else 3.8
        y -= int(dy * BLOCK_SIZE) // 2
        x -= BLOCK_SIZE // 2
        obj = Platform(ord(ch) - ord('O'), x, y)
        gfw.world.add(gfw.layer.platform, obj)
        # print('creating Platform', x, y)
    else:
        ao = factory.create(ch, x, y)
        if ao is None:
            global ignore_char_map
            if ch not in ignore_char_map:
                print("Error? I don't know about: '%s'" % ch)
                ignore_char_map |= {ch}
            return
        gfw.world.add(gfw.layer.enemy, ao)


def get(x, y):
    col = x % UNIT_PER_LINE
    row = x // UNIT_PER_LINE * SCREEN_LINES + SCREEN_LINES - 1 - y
    return lines[row][col]

def test_gen():
    load(gobj.res('stage_01.txt'))
    # print('count=', count())
    line = 0
    for x in range(200):
        s = ''
        for y in range(10):
            s += get(x,y)
        line += 1
        # print('%03d:' % line, s)

def test_gen_2():
    open_canvas()
    gfw.world.init(['item', 'platform'])
    load(gobj.res('stage_01.txt'))
    for i in range(100):
        update(0.1)
    close_canvas()

if __name__ == '__main__':
    test_gen_2()