import random
from pico2d import *
import gfw
import gobj

class Player:
    KEYDOWN_SPACE  = (SDL_KEYDOWN, SDLK_SPACE)
    RUNNING, FALLING = range(2)
    GRAVITY = 400

    #constructor
    def __init__(self):
        self.pos = 150, get_canvas_height() // 2
        self.delta = 0, 0
        self.image = gfw.image.load(gobj.res('cookie.png'))
        self.time = 0
        self.anim = [ 0x40, 0x41, 0x42, 0x43 ]
        self.FPS = 10
        self.state = Player.RUNNING

    def draw(self):
        fidx = round(self.time * self.FPS) % len(self.anim)
        sprite_num = self.anim[fidx]
        x, y = sprite_num % 0x10, sprite_num // 0x10
        x = x * 272 + 2
        y = y * 272 + 2
        self.image.clip_draw(x, y, 270, 270, *self.pos)

    def update(self):
        self.time += gfw.delta_time
        if self.state != Player.RUNNING:
            self.move((0, self.jump_speed * gfw.delta_time))
            self.jump_speed -= Player.GRAVITY * gfw.delta_time
        _,foot,_,_ = self.get_bb()
        platform = self.get_platform(foot)
        if platform is not None:
            l,b,r,t = platform.get_bb()
            if self.state == Player.RUNNING:
                print('running', t, foot)
                if foot > t:
                    self.state = Player.FALLING
                    self.jump_speed = 0
            elif self.state == Player.FALLING:
                print('falling', t, foot)
                if self.jump_speed < 0 and int(foot) <= t:
                    self.move((0, t - foot))
                    self.state = Player.RUNNING
                    self.jump_speed = 0
                    print('Stops')

    def get_platform(self, foot):
        selected = None
        sel_top = 0
        x,y = self.pos
        for platform in gfw.world.objects_at(gfw.layer.platform):
            l,b,r,t = platform.get_bb()
            if x < l or x > r: continue
            if foot < b: continue
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
            pass

    def get_bb(self):
        l,b,r,t = -60,-135,60,0
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
