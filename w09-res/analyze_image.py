import pygame
import json
import sys

with open('out/cookies.json', 'r') as f:
    cookies = json.load(f)

transparent = (0, 0, 0, 0)

char_width = 0
char_height = 0

new_cookies = []
n = 0
for cookie in cookies:
    try:
        image = pygame.image.load('out/%s_sheet.png' % cookie['id'])
    except:
        continue
    w = image.get_width()
    cx = 0
    bx = 2
    for x in range(2, w):
        pixel = image.get_at((x, 2))
        border = pixel != transparent
        if border:
            if bx != 0:
                cx += 1
                frame_width = x - bx
                # print('char_width=', char_width, 'frame_width=', frame_width)
                if char_width < frame_width:
                    char_width = frame_width
                bx = 0
        else:
            if bx == 0:
                bx = x

    h = image.get_height()
    cy = 0
    by = 2
    for y in range(2, h):
        pixel = image.get_at((2, y))
        border = pixel != transparent
        if border:
            if by != 0:
                cy += 1
                frame_height = y - by
                # print('char_height=', char_height, 'frame_height=', frame_height)
                if char_height < frame_height:
                    char_height = frame_height
                by = 0
        else:
            if by == 0:
                by = y

    cookie["size"] = frame_width
    if frame_width != frame_height:
        cookie["width"] = frame_width
        cookie["height"] = frame_height
    cookie["xcount"] = cx
    cookie["ycount"] = cy
    print(cookie)
    sys.stdout.flush()

    if cy != 6: continue
    if cx < 11 or cx > 15: continue
    new_cookies.append(cookie)

    n += 1

with open('out/cookies_3.json', 'w') as f:
    json.dump(new_cookies, f, indent=2)

