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

def test_board():
    for i in range(16):
        generate_block()
        print_blocks()

if __name__ == '__main__':
    test_board()
