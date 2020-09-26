import random
import gfw
import gfw_world
from pico2d import *
from enemy import Enemy

class EnemyGenerator:
    GEN_X = [ 50, 150, 250, 350, 450 ]
    def __init__(self):
        self.next_wave = 0
        self.wave_index = 0

    def update(self):
        self.next_wave -= gfw.delta_time
        if self.next_wave < 0:
            self.generate_wave()

    def generate_wave(self):
        for x in EnemyGenerator.GEN_X:
            e = Enemy(x, -1)
            gfw_world.add(gfw.layer.enemy, e)

        self.wave_index += 1
        self.next_wave = random.uniform(5, 6)
