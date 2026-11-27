with open('botox.html', 'r', encoding='utf-8') as f:
    b = f.read()

idx = b.find('id="why-dzen"')
if idx != -1:
    print(b[idx-50:idx+2500])
