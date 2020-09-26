import random
import gfw
import gfw_world
from pico2d import *
from enemy import Enemy

GEN_X = [ 50, 150, 250, 350, 450 ]
next_wave = 0
wave_index = 0

def update():
    global next_wave
    next_wave -= gfw.delta_time
    if next_wave < 0:
        generate_wave()

def generate_wave():
    global wave_index, next_wave
    for x in GEN_X:
        e = Enemy(x, -1)
        gfw_world.add(gfw.layer.enemy, e)

    wave_index += 1
    next_wave = random.uniform(5, 6)
