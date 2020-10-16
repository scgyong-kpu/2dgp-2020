import re
import json

pat = re.compile(r'\s+<img src="/resources/sheet_icons/(\d+)/(\d+).png" alt="([^"]+)">\s*$')
icon_cmd = "curl 'https://www.spriters-resource.com/resources/sheet_icons/%s/%s.png' > out/%s_icon.png"
sheet_cmd = "curl 'https://www.spriters-resource.com/resources/sheets/%s/%s.png' > out/%s_sheet.png"

chars = []
with open('out/cookierun.html', 'r') as f:
    while True:
        str = f.readline()
        if not str: break
        m = pat.match(str)
        if not m: continue
        grade, number, name = m.groups()
        char = { "id": number, "name": name }
        chars.append(char)
        print(icon_cmd % (grade, number, number))
        print(sheet_cmd % (grade, number, number))
        # print(grade, number, name)

with open('out/cookies.json', 'w') as f:
    json.dump(chars, f, indent=2)

