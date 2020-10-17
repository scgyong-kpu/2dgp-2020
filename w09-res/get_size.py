from pico2d import *
import json

with open('out/cookies.json', 'r') as f:
    cookies = json.load(f)

open_canvas()

cookies_2 = []
for cookie in cookies:
    if 'size' in cookie: continue
    try:
        image = load_image('out/%s_sheet.png' % cookie['id'])
    except IOError:
        continue
    size = (image.w - 2) // 11 - 2
    cookie['size'] = size
    cookies_2.append(cookie)
    print(cookie)

close_canvas()

with open('out/cookies_2.json', 'w') as f:
    json.dump(cookies_2, f, indent=2)

