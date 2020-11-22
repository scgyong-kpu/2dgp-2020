import gfw
from pico2d import *
import json

class Layer:
    def __init__(self, dict):
        self.__dict__.update(dict)

class Tileset:
    def __init__(self, dict):
        self.__dict__.update(dict)
        self.rows = math.ceil(self.tilecount / self.columns)
        print('rows:', self.rows)
    def getRectForTile(self, tile):
        x = (tile - 1) % self.columns;
        y = (tile - 1) // self.columns;
        l = x * (self.tilewidth + self.spacing) + self.margin;
        t  = (self.rows - y - 1) * (self.tileheight + self.spacing) + self.margin;
        return l, t, self.tilewidth, self.tileheight

class Map:
    def __init__(self, dict):
        self.__dict__.update(dict)
        self.layers = list(map(Layer, self.layers))
        self.tilesets = list(map(Tileset, self.tilesets))

class Background:
    def __init__(self, json_fn, tile_fn):
        with open(json_fn) as f:
            self.map = Map(json.load(f))
        self.image = gfw.image.load(tile_fn)
        self.width = self.map.tilewidth * self.map.width
        self.height = self.map.tileheight * self.map.height
        self.scroll_x, self.scroll_y = 0, 0
        self.tileset = self.map.tilesets[0]
        self.layer = self.map.layers[0]
        self.wraps = True
        self.speed_x, self.speed_y = 0, 0
    def get_boundary(self):
        return 0, 0, self.width, self.height
    def to_screen(self, x, y):
        return x - self.scroll_x, y - self.scroll_y
    def translate(self, x, y):
        return x + self.scroll_x, y + self.scroll_y
    def update(self):
        self.scroll_x += self.speed_x * gfw.delta_time
        self.scroll_y += self.speed_y * gfw.delta_time
    def draw(self):
        sx, sy = round(self.scroll_x), round(self.scroll_y)
        if self.wraps:
            sx %= self.width;
            if sx < 0:
                sx += self.width;
            sy %= self.height;
            if sy < 0:
                sy += self.height;

        cw,ch = get_canvas_width(), get_canvas_height()

        tile_x = sx // self.map.tilewidth;
        tile_y = sy // self.map.tileheight;
        beg_x = -(sx % self.map.tilewidth);
        beg_y = -(sy % self.map.tileheight);
        db = beg_y;
        ty = tile_y;
        while ty < self.layer.height and db < ch:
            if ty >= 0:
                dl = beg_x;
                dr = beg_x + self.map.tilewidth;
                tx = tile_x;
                # print(tx, ty, self.map.height - ty - 1)
                ti = (self.map.height - ty - 1) * self.map.width + tx;
                # babo = []
                while tx < self.layer.width and dl < cw:
                    tile = self.layer.data[ti];
                    # babo.append(tile)
                    rect = self.tileset.getRectForTile(tile);
                    # babo.append(rect)
                    # print(rect, dl, db)
                    self.image.clip_draw_to_origin(*rect, dl, db)
                    dl += self.map.tilewidth
                    ti += 1;
                    tx += 1;
                # print(babo)
            db += self.map.tileheight
            ty += 1;
            if self.wraps and ty >= self.layer.height:
                ty -= self.layer.height;

def test():
    open_canvas()
    b = Background('res/earth.json', 'res/forest_tiles.png')
    print(b.map.width, b.map.height, b.map.tilewidth, b.map.tileheight)
    b.draw()
    update_canvas()
    running = True
    while running:
        for e in get_events():
            if e.type == SDL_KEYDOWN:
                if e.key == SDLK_ESCAPE:
                    running = False
                elif e.key == SDLK_DOWN:
                    b.scroll_y += 10
                    b.draw()
                    update_canvas()
        delay(0.1)
    close_canvas()
    pass

if __name__ == "__main__":
    test()
