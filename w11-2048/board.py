import random
import gfw

blocks = [ None for i in range(16) ]

def reset():
    global blocks
    blocks = [ None for i in range(16) ]

def get_block(x, y):
    return blocks[y * 4 + x]
def get_value(x, y):
    b = blocks[y * 4 + x]
    return 0 if b is None else b.value
def set_block(x, y, block):
    blocks[y * 4 + x] = block

def print_blocks():
    for y in range(3, -1, -1):
        line = ''
        for x in range(4):
            b = get_block(x, y)
            str = '[     ] ' if b == None else '[%5d] ' % b
            line += str
        print(line)

def is_full():
    for i in range(16):
        if blocks[i] == None: return False
    return True

def generate_block(block):
    if is_full(): return (-1, -1, 0)
    while True:
        i = random.randint(0, 15)
        # print(i, blocks[i])
        if blocks[i] is None: break
    blocks[i] = block
    x = i % 4
    y = i // 4
    return x, y

def can_reduce():
    for y in range(4):
        for x in range(4):
            v = get_value(x, y)
            if v == 0: continue
            if x < 3 and v == get_value(x + 1, y): return True
            if y < 3 and v == get_value(x, y + 1): return True
    return False

def move(converter):
    moved = False
    score = 0
    for y in range(4):
        for x in range(4):
            v = 0
            ox, oy = converter(x, y)
            b = get_block(ox, oy)
            if b is None:
                for x2 in range(x + 1, 4):
                    ox2, oy2 = converter(x2, y)
                    b = get_block(ox2, oy2)
                    # v = self.blocks[y * 4 + x2].getValue()
                    if b is not None:
                        v = b.value
                        set_block(ox, oy, b)
                        b.move_to(ox, oy)
                        set_block(ox2, oy2, None)
                        moved = True
                        break
                if b is None:
                    break
            else:
                v = b.value
            for x2 in range(x + 1, 4):
                ox2, oy2 = converter(x2, y)
                b2 = get_block(ox2, oy2)
                if b2 is not None:
                    v2 = b2.value
                    if v == v2:
                        score += 2 * v
                        b.remove()
                        set_block(ox, oy, b2)
                        b2.double()
                        b2.move_to(ox, oy)
                        set_block(ox2, oy2, None)
                        moved = True
                    break
    return moved, score

def slow_down_animation():
    for b in blocks:
        if b is None: continue
        b.fps = random.random()

def update():
    pass

def test_board():
    for i in range(16):
        generate_block()
        print_blocks()

if __name__ == '__main__':
    # test_board()
    pass
