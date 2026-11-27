with open('under-eye-darkness.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('pgFaqMore')
while idx != -1:
    print(c[idx-50:idx+200])
    print('---')
    idx = c.find('pgFaqMore', idx+1)
