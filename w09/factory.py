import json
import gobj
from anim_obj import AnimObject
from obstacle import JsonObject

class Factory:
    def __init__(self):
        with open(gobj.res('objs.json'), 'r') as f:
            data = json.load(f)
        self.__dict__.update(data)
        self.map = {}
        for obj in self.objs:
            self.map[obj["char"]] = obj
    def create(self, char, x, y):
        if char not in self.map:
            return None
        obj = self.map[char]
        if y <= 150: y -= 28
        if "offset" in obj:
            y += obj["offset"]
        # print(char, py, y)
        ao = JsonObject(x, y)
        if "attr" in obj:
            ao.__dict__.update(obj["attr"])
        if "name" in obj:
            ao.name = obj["name"]
        ao.set_anim(gobj.resl(obj['files']), obj['fps'])
        return ao
