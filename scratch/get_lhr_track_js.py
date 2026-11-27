with open('laser-hair-removal.html', 'r', encoding='utf-8') as f:
    lhr = f.read()

idx = lhr.find("track = document.querySelector('.hf-related-track')")
if idx == -1:
    idx = lhr.find("relatedTrack")
if idx != -1:
    print(lhr[idx-50:idx+1500])
