import gfw
from pico2d import *

objects = []
trashcan = []

def add(obj):
    objects.append(obj)

def remove(obj):
    trashcan.append(obj)

def update():
    for obj in objects:
        obj.update()
    if len(trashcan) > 0:
        empty_trashcan()

def draw():
    for obj in objects:
        obj.draw()

def empty_trashcan():
    global trashcan

    for obj in trashcan:
        objects.remove(obj)

    trashcan = []

    print('total objects count =', len(objects))

