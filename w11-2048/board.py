
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


def test_board():
    set_block(2, 3, 16)
    set_block(1, 2, 4)
    set_block(0, 2, 8)
    set_block(3, 0, 32)
    print_blocks()

if __name__ == '__main__':
    test_board()
