with open('laser-hair-removal.html', 'r', encoding='utf-8') as f:
    lhr = f.read()

import re
matches = re.findall(r'[^{]*#related-services[^{]*\{[^}]*\}', lhr)
print("Matches in laser-hair-removal.html:")
for m in matches:
    print(m)
    print("---")
