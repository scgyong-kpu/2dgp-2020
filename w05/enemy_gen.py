import random
import gfw
import gfw_world
from pico2d import *
from enemy import Enemy

class EnemyGenerator:
    def __init__(self):
        self.next_wave = random.uniform(1, 2)

    def update(self):
        self.next_wave -= gfw.delta_time
        if self.next_wave > 0: return

        x = random.randint(0, get_canvas_width())
        e = Enemy(x, -1)
        gfw_world.add(gfw.layer.enemy, e)
        self.next_wave = random.uniform(1, 2)
