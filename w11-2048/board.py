import random

blocks = [ None for i in range(16) ]

def get_block(x, y):
    return blocks[y * 4 + x]
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

def move(converter):
    moved = False
    for y in range(4):
        for x in range(4):
            ox, oy = converter(x, y)
            b = get_block(ox, oy)
            if b is None:
                for x2 in range(x + 1, 4):
                    ox2, oy2 = converter(x2, y)
                    b = get_block(ox2, oy2)
                    # v = self.blocks[y * 4 + x2].getValue()
                    if b is not None:
                        set_block(ox, oy, b)
                        b.move_to(ox, oy)
                        set_block(ox2, oy2, None)
                        moved = True
                        break
                if b is None:
                    break

def test_board():
    for i in range(16):
        generate_block()
        print_blocks()

if __name__ == '__main__':
    test_board()
