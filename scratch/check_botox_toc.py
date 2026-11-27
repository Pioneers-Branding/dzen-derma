with open('botox.html', 'r', encoding='utf-8') as f:
    b = f.read()

idx = b.find('bxTocTrack')
if idx != -1:
    print(b[idx:idx+800])
else:
    print("bxTocTrack not in botox.html")
