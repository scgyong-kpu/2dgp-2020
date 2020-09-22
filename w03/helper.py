import math

# arguments: pos, delta, target
# - pos = (x, y) tuple
# - delta = (dx, dy) tuple
# - target = (x, y) tuple
# returns: (pos, done)
# - pos = (x, y) tuple
# - done = True if arrived
def move_toward(pos, delta, target):
    done = False
    x,y = pos[0] + delta[0], pos[1] + delta[1]

    if delta[0] > 0 and x >= target[0] or delta[0] < 0 and x <= target[0]:
        done = True
    if delta[1] > 0 and y >= target[1] or delta[1] < 0 and y <= target[1]:
        done = True

    # pos = done ? target : (x,y) # in C language
    pos = target if done else (x,y)

    return (pos, done)

# arguments: pos, target, speed
# - pos = (x, y) tuple
# - target = (x, y) tuple
# - speed = pixels per frame
# returns: (dx, dy)
# - x/y pixels per frame
def delta(pos, target, speed):
    dx, dy = target[0] - pos[0], target[1] - pos[1]
    distance = math.sqrt(dx**2 + dy**2)
    if distance == 0: return 0, 0
    return dx * speed / distance, dy * speed / distance




# object version

def move_toward_obj(obj):
    if obj.target == None: return
    pos, done = move_toward(obj.pos, obj.delta, obj.target)
    if done:
        obj.target = None
        obj.delta = 0,0

    obj.pos = pos

def set_target(obj, target):
    obj.target = target
    obj.delta = (0,0) if target is None else delta(obj.pos, target, obj.speed)

