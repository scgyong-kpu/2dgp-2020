from pico2d import *
import gfw

MOVE_PPS = 300
MAX_LIFE = 5

mouse_control = False

def init():
    global image, pos, radius
    image = gfw.image.load('res/BattleCruiser.png')
    radius = 34

    global heart_red, heart_white
    heart_red = gfw.image.load('res/heart_red.png')
    heart_white = gfw.image.load('res/heart_white.png')

    reset()

def reset():
    global pos
    pos = get_canvas_width() // 2, get_canvas_height() // 2

    global delta_x, delta_y
    delta_x, delta_y = 0, 0

    global angle
    angle = 0

    global life
    life = MAX_LIFE

def increase_life():
    global life
    if life >= MAX_LIFE:
        return True
    life += 1
    return False

def decrease_life():
    global life
    life -= 1
    return life <= 0

def update():
    global pos
    if mouse_control:
        follow_mouse_target()
        x, y = pos
    else:
        x, y = pos
        x += delta_x * MOVE_PPS * gfw.delta_time
        y += delta_y * MOVE_PPS * gfw.delta_time

    x = clamp(radius, x, get_canvas_width() - radius)
    y = clamp(radius, y, get_canvas_height() - radius)
    pos = x, y


def follow_mouse_target():
    global pos, angle
    x,y = pos
    dx,dy = target_x-x, target_y-y
    distance = math.sqrt(dx**2+dy**2)
    if distance == 0:
        return
    dx,dy = dx / distance, dy / distance
    x += dx * MOVE_PPS * gfw.delta_time
    y += dy * MOVE_PPS * gfw.delta_time
    if dx > 0 and x > target_x: x = target_x
    if dx < 0 and x < target_x: x = target_x
    if dy > 0 and y > target_y: y = target_y
    if dy < 0 and y < target_y: y = target_y
    pos = x, y

    angle = math.atan2(dy, dx) - math.pi / 2
    print('Angle: %.3f' % angle)

def draw():
    global image, pos
    # image.draw(*pos)
    size = image.h
    fidx = round(-(angle / math.pi * 16)) % 32
    # print('Angle: %.3f' % angle, 'fidx:', fidx_)
    rect = fidx * size, 0, size, size
    # print(rect, pos)
    image.clip_draw(*rect, *pos)

    x,y = get_canvas_width() - 30, get_canvas_height() - 30
    for i in range(MAX_LIFE):
        heart = heart_red if i < life else heart_white
        heart.draw(x, y)
        x -= heart.w

def set_target(e):
    global target_x, target_y
    target_x, target_y = e.x, get_canvas_height() - e.y - 1

def handle_event(e):
    global mouse_control
    global delta_x, delta_y, angle

    if e.type == SDL_MOUSEBUTTONDOWN:
        mouse_control = True
        return set_target(e)
    elif e.type == SDL_MOUSEMOTION:
        if mouse_control:
            return set_target(e)

    if e.type == SDL_KEYDOWN and e.key == SDLK_RETURN:
        if mouse_control:
            mouse_control = False
            angle = 0

    if mouse_control:
        return

    if e.type == SDL_KEYDOWN:
        if e.key == SDLK_LEFT:
            delta_x -= 1
        elif e.key == SDLK_RIGHT:
            delta_x += 1
        elif e.key == SDLK_DOWN:
            delta_y -= 1
        elif e.key == SDLK_UP:
            delta_y += 1
    elif e.type == SDL_KEYUP:
        if e.key == SDLK_LEFT:
            delta_x += 1
        elif e.key == SDLK_RIGHT:
            delta_x -= 1
        elif e.key == SDLK_DOWN:
            delta_y += 1
        elif e.key == SDLK_UP:
            delta_y -= 1
