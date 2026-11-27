with open('pigmentation.html', 'r', encoding='utf-8') as f:
    p = f.read()

idx = p.find('bx-related-track')
print("bx-related-track in pigmentation.html:", idx != -1)
if idx != -1:
    print(p[idx-100:idx+300])
