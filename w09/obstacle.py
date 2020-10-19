import random
import json
from pico2d import *
import gfw
import gobj
from anim_obj import AnimObject

class JsonObject(AnimObject):
    def __init__(self, x, y):
        super(JsonObject, self).__init__(x, y)
        self.delay = 0
    def update(self):
        if self.delay > 0:
            # print(self.delay)
            self.delay -= gfw.delta_time
            return
        super(JsonObject, self).update()