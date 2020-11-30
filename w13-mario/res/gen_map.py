import json

with open('map.json') as f:
    data = json.load(f)

layer = data["layers"][2]
objs = layer["objects"]

for o in objs:
    o["y"] = 1200 - o["y"] - o["height"]

with open('objects.json', 'w') as f:
    json.dump(objs, f, indent=2)