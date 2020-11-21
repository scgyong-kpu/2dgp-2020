import gfw
import player

def collides_distance(a, b):
    ax,ay = a.pos
    bx,by = b.pos
    radius_sum = a.radius + b.radius
    distance_sq = (ax-bx)**2 + (ay-by)**2
    return distance_sq < radius_sum**2

# returns hit, dead
def check_collision():
    hit, dead = False, False
    for m in gfw.world.objects_at(gfw.layer.missile):
        if collides_distance(player, m):
            hit = True
            gfw.world.remove(m)
            dead = player.decrease_life()
            break

    return hit, dead
