with open('laser-hair-removal.html', 'r', encoding='utf-8') as f:
    lhr = f.read()

import re
matches = [m.start() for m in re.finditer(r'relatedTrack', lhr)]
print("Occurrences of relatedTrack:", matches)
for pos in matches:
    print(lhr[pos-50:pos+800])
    print("="*40)
