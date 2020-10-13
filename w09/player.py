import random
from pico2d import *
import gfw
import gobj

class Player:
    KEYDOWN_SPACE  = (SDL_KEYDOWN, SDLK_SPACE)
    KEYDOWN_ENTER  = (SDL_KEYDOWN, SDLK_RETURN)
    RUNNING, FALLING, JUMPING, DOUBLE_JUMP, SLIDING = range(5)
    ANIMS = [
        [ 0x40, 0x41, 0x42, 0x43 ], # RUNNING
        [ 0x50 ],                   # FALLING
        [ 0x57, 0x58 ],             # JUMPING
        [ 0x51, 0x52, 0x53, 0x54 ], # DOUBLE_JUMP
        [ 0x59, 0x5A ],             # SLIDING
    ]
    BB_DIFFS = [
        (-60,-135,60,0),   # RUNNING
        (-60,-135,60,10),  # FALLING
        (-60,-135,60,-20), # JUMPING
        (-60,-135,60,-20), # DOUBLE_JUMP
        (-80,-135,80,-68), # SLIDING
    ]
    SLIDE_DURATION = 1.0

    GRAVITY = 3000
    JUMP = 1000

    #constructor
    def __init__(self):
        self.pos = 150, get_canvas_height() // 2
        self.delta = 0, 0
        self.image = gfw.image.load(gobj.res('cookie.png'))
        self.time = 0
        self.FPS = 10
        self.state = Player.RUNNING

    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state):
        self.__state = state
        self.anim = Player.ANIMS[state]
    def draw(self):
        fidx = round(self.time * self.FPS) % len(self.anim)
        sprite_num = self.anim[fidx]
        x, y = sprite_num % 0x10, sprite_num // 0x10
        x = x * 272 + 2
        y = y * 272 + 2
        self.image.clip_draw(x, y, 270, 270, *self.pos)

    def jump(self):
        if self.state in [Player.FALLING, Player.DOUBLE_JUMP, Player.SLIDING]: 
            return
        if self.state == Player.RUNNING:
            self.state = Player.JUMPING
        elif self.state == Player.JUMPING:
            self.state = Player.DOUBLE_JUMP
        self.jump_speed = Player.JUMP
    def slide(self):
        if self.state != Player.RUNNING: return
        self.state = Player.SLIDING
        self.time = 0.0
    def update(self):
        self.time += gfw.delta_time
        if self.state == Player.SLIDING and self.time > Player.SLIDE_DURATION:
            self.state = Player.RUNNING
        if self.state in [Player.JUMPING, Player.DOUBLE_JUMP, Player.FALLING]:
            # print('jump speed:', self.jump_speed)
            self.move((0, self.jump_speed * gfw.delta_time))
            self.jump_speed -= Player.GRAVITY * gfw.delta_time
        _,foot,_,_ = self.get_bb()
        platform = self.get_platform(foot)
        if platform is not None:
            l,b,r,t = platform.get_bb()
            if self.state in [Player.RUNNING, Player.SLIDING]:
                if foot > t:
                    self.state = Player.FALLING
                    self.jump_speed = 0
            else:
                # print('falling', t, foot)
                if self.jump_speed < 0 and int(foot) <= t:
                    self.move((0, t - foot))
                    self.state = Player.RUNNING
                    self.jump_speed = 0
                    # print('Now running', t, foot)

    def get_platform(self, foot):
        selected = None
        sel_top = 0
        x,y = self.pos
        for platform in gfw.world.objects_at(gfw.layer.platform):
            l,b,r,t = platform.get_bb()
            if x < l or x > r: continue
            mid = (b + t) // 2
            if foot < mid: continue
            if selected is None:
                selected = platform
                sel_top = t
            else:
                if t > sel_top:
                    selected = platform
                    sel_top = t
        # if selected is not None:
        #     print(l,b,r,t, selected)
        return selected

    def move(self, diff):
        self.pos = gobj.point_add(self.pos, diff)

    def handle_event(self, e):
        pair = (e.type, e.key)
        if pair == Player.KEYDOWN_SPACE:
            self.jump()
        elif pair == Player.KEYDOWN_ENTER:
            self.slide()

    def get_bb(self):
        l,b,r,t = Player.BB_DIFFS[self.state]
        x,y = self.pos
        return x + l, y + b, x + r, y + t

    def __getstate__(self):
        dict = self.__dict__.copy()
        del dict['image']
        return dict

    def __setstate__(self, dict):
        # self.__init__()
        self.__dict__.update(dict)
        self.image = gfw.image.load(gobj.RES_DIR + '/animation_sheet.png')
