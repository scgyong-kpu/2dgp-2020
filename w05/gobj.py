import random
from pico2d import *

RES_DIR = './res'

def rand(val):
    return val * random.uniform(0.9, 1.1)

def point_add(point1, point2):
    x1,y1 = point1
    x2,y2 = point2
    return x1+x2, y1+y2

def move_obj(obj):
    obj.pos = point_add(obj.pos, obj.delta)
    
if __name__ == "__main__":
	print("This file is not supposed to be executed directly.")
