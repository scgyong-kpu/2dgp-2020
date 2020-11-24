from pico2d import *
import gfw
import player

def collides_distance(a, b):
    ax,ay = a.pos
    bx,by = b.pos
    distance_sq = (ax-bx)**2 + (ay-by)**2
    radius_sum = a.radius + b.radius
    return distance_sq < radius_sum ** 2

def check_collision():
    dead, full = False, False
    for m in gfw.world.objects_at(gfw.layer.missile):
        if collides_distance(player, m):
            gfw.world.remove(m)
            dead = player.decrease_life()

    for m in gfw.world.objects_at(gfw.layer.item):
        if collides_distance(player, m):
            gfw.world.remove(m)
            full = player.increase_life()

    return dead, full
