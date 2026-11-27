import os

print('sagging-skin.html exists?', os.path.exists('sagging-skin.html'))
if os.path.exists('sagging-skin.html'):
    with open('sagging-skin.html', 'r', encoding='utf-8') as f:
        c = f.read()
    print('Length:', len(c))
    idx = c.find('id="overview"')
    print('id="overview" found at:', idx)
    if idx != -1:
        print(c[idx-50:idx+2500])
