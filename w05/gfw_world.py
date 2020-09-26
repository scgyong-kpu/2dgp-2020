import gfw
from pico2d import *

objects = [[],[],[],[]]
trashcan = []

def add(layer_index, obj):
    objects[layer_index].append(obj)

def remove(obj):
    trashcan.append(obj)

def update():
    for layer_objects in objects:
        for obj in layer_objects:
            obj.update()
    if len(trashcan) > 0:
        empty_trashcan()
    counts = list(map(len, objects))
    print('total objects count =', counts)

def draw():
    for layer_objects in objects:
        for obj in layer_objects:
            obj.draw()

def empty_trashcan():
    global trashcan

    for obj in trashcan:
        for layer_objects in objects:
            # if obj in layer_objects:
            #     layer_objects.remove(obj)
            try:
                layer_objects.remove(obj)
            except ValueError:
                pass
    trashcan = []



