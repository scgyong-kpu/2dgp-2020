import random
from pico2d import *
import gfw
import gobj
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode

class Zombie:
    PAT_POSITIONS = [
        (43, 210), (1118, 210), (1050, 430), (575, 740), 
        (235, 927), (575, 740), (1050, 430), (1118, 210)
    ]
    ACTIONS = ['Attack', 'Dead', 'Idle', 'Walk']
    CHASE_DISTANCE_SQ = 250 ** 2
    IDLE_INTERVAL = 2.0
    images = {}
    FPS = 12
    # FCOUNT = 10
    def __init__(self):
        if len(Zombie.images) == 0:
            Zombie.load_all_images()

        self.pos = (
            random.randint(0, get_canvas_width()),
            random.randint(0, get_canvas_height())
        )
        self.delta = 0.1, 0.1
        # self.find_nearest_pos()
        char = random.choice(['male', 'female'])
        self.images = Zombie.load_images(char)
        self.action = 'Idle'
        self.speed = random.randint(100, 150)
        self.fidx = 0
        self.time = 0
        layer = list(gfw.world.objects_at(gfw.layer.player))
        self.player = layer[0]
        self.patrol_order = -1
        self.build_behavior_tree()

    def find_nearest_pos(self):
        x, y = self.pos
        nearest_dsq = 1000000000
        index = 0
        nearest_index = 0
        for (px, py) in Zombie.PAT_POSITIONS:
            dsq = (x-px)**2 + (y-py)**2
            # print(':', index, (x,y), '-', (px, py), dsq)
            if nearest_dsq > dsq:
                nearest_dsq = dsq
                nearest_index = index
                # print('nearest:', index)
            index += 1
        self.patrol_order = nearest_index
        self.set_patrol_target()

    def set_patrol_target(self):
        if self.patrol_order < 0:
            self.find_nearest_pos()
            return BehaviorTree.SUCCESS
        self.set_target(Zombie.PAT_POSITIONS[self.patrol_order])
        # print('pos=', self.pos, "patrol order = ", self.patrol_order, " target =", self.target)
        self.patrol_order = (self.patrol_order + 1) % len(Zombie.PAT_POSITIONS)
        return BehaviorTree.SUCCESS

    def set_target(self, target):
        x,y = self.pos
        tx,ty = target
        dx, dy = tx - x, ty - y
        distance = math.sqrt(dx**2 + dy**2)
        if distance == 0: return

        self.target = target
        self.delta = dx / distance, dy / distance
        # print(x,y, tx,ty, dx,dy, '/',distance, dx/distance, dy/distance, 'target=', self.target, ' delta=', self.delta)

    def find_player(self):
        dist_sq = gobj.distance_sq(self.player.pos, self.pos)
        if dist_sq < Zombie.CHASE_DISTANCE_SQ:
            if self.patrol_order >= 0:
                self.patrol_order = -1
                self.action = 'Attack'
            return BehaviorTree.SUCCESS
        else:
            if self.action == 'Attack':
                self.action = 'Idle'
                self.time = 0
            else:
                self.action = 'Walk'
            return BehaviorTree.FAIL

    def move_to_player(self):
        self.set_target(self.player.pos)
        self.update_position()

        collides = gobj.collides_box(self, self.player)
        if collides:
            self.action = 'Dead'
            self.time = 0
        return BehaviorTree.SUCCESS

    def follow_patrol_positions(self):
        if self.patrol_order < 0:
            self.find_nearest_pos()
        done = self.update_position()
        if done:
            self.set_patrol_target()

    def do_idle(self):
        if self.action != 'Idle':
            return BehaviorTree.FAIL
        self.time += gfw.delta_time
        self.fidx = round(self.time * Zombie.FPS)
        if self.time >= Zombie.IDLE_INTERVAL:
            self.action = 'Walk'
            return BehaviorTree.FAIL
        return BehaviorTree.SUCCESS

    def do_dead(self):
        if self.action != 'Dead':
            return BehaviorTree.FAIL
        self.time += gfw.delta_time
        self.fidx = round(self.time * Zombie.FPS)
        if self.fidx >= len(self.images['Dead']):
            self.remove()

        return BehaviorTree.SUCCESS

    @staticmethod
    def load_all_images():
        Zombie.load_images('male')
        Zombie.load_images('female')
        # Zombie.font = gfw.font.load(gobj.RES_DIR + '/ENCR10B.TTF', 20)

    @staticmethod
    def load_images(char):
        if char in Zombie.images:
            return Zombie.images[char]

        images = {}
        count = 0
        file_fmt = '%s/zombiefiles/%s/%s (%d).png'
        for action in Zombie.ACTIONS:
            action_images = []
            n = 0
            while True:
                n += 1
                fn = file_fmt % (gobj.RES_DIR, char, action, n)
                if os.path.isfile(fn):
                    action_images.append(gfw.image.load(fn))
                else:
                    break
                count += 1
            images[action] = action_images
        Zombie.images[char] = images
        print('%d images loaded for %s' % (count, char))
        return images

    def update(self):
        self.bt.run()

    def update_position(self):
        self.time += gfw.delta_time
        self.fidx = round(self.time * Zombie.FPS)

        x,y = self.pos
        dx,dy = self.delta
        x += dx * self.speed * gfw.delta_time
        y += dy * self.speed * gfw.delta_time

        # print(self.pos, self.delta, self.target, x, y, dx, dy)

        done = False
        tx,ty = self.target
        if dx > 0 and x >= tx or dx < 0 and x <= tx:
            x = tx
            done = True
        if dy > 0 and y >= ty or y < 0 and y <= ty:
            y = ty
            done = True

        self.pos = x,y

        return done

    def remove(self):
        gfw.world.remove(self)

    def draw(self):
        images = self.images[self.action]
        image = images[self.fidx % len(images)]
        flip = 'h' if self.delta[0] < 0 else ''
        image.composite_draw(0, flip, *self.pos, image.w // 5, image.h // 5)
        # x,y = self.pos
        # Zombie.font.draw(x-40, y+50, self.action + str(round(self.time * 100) / 100))

    def get_bb(self):
        x,y = self.pos
        return x - 40, y - 50, x + 40, y + 40

    def build_behavior_tree(self):
        # node_gnp = LeafNode("Get Next Position", self.set_patrol_target)
        # node_mtt = LeafNode("Move to Target", self.update_position)
        # patrol_node = SequenceNode("Patrol")
        # patrol_node.add_children(node_gnp, node_mtt)
        # self.bt = BehaviorTree(patrol_node)

        self.bt = BehaviorTree.build({
            "name": "PatrolChase",
            "class": SelectorNode,
            "children": [
                {
                    "class": LeafNode,
                    "name": "Idle",
                    "function": self.do_idle,
                },
                {
                    "class": LeafNode,
                    "name": "Dead",
                    "function": self.do_dead,
                },
                {
                    "name": "Chase",
                    "class": SequenceNode,
                    "children": [
                        {
                            "class": LeafNode,
                            "name": "Find Player",
                            "function": self.find_player,
                        },
                        {
                            "class": LeafNode,
                            "name": "Move to Player",
                            "function": self.move_to_player,
                        },
                    ],
                },
                {
                    "class": LeafNode,
                    "name": "Follow Patrol positions",
                    "function": self.follow_patrol_positions,
                },
            ],
        })
