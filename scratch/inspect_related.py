import re

with open('laser-hair-removal.html', 'r', encoding='utf-8') as f:
    lhr = f.read()

print("--- LASER HAIR REMOVAL ---")
for m in re.finditer(r'<section[^>]*id=["\']([^"\']*(?:related|services)[^"\']*)["\']', lhr, re.I):
    print("Found section id:", m.group(1))

idx = lhr.find('related-')
if idx != -1:
    print(lhr[idx-50:idx+1500])
else:
    # search for related
    idx2 = lhr.lower().find('related')
    if idx2 != -1:
        print(lhr[idx2-50:idx2+1500])

with open('under-eye-darkness.html', 'r', encoding='utf-8') as f:
    ued = f.read()

print("\n--- UNDER EYE DARKNESS ---")
idx3 = ued.find('related-')
if idx3 != -1:
    print(ued[idx3-50:idx3+1500])
