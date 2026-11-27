with open('laser-hair-removal.html', 'r', encoding='utf-8') as f:
    lhr = f.read()

idx = lhr.find('id="related-services"')
if idx != -1:
    print(lhr[idx-100:idx+2500])

import re
matches = re.findall(r'(\.hf-related[^{]+)\{([^}]+)\}', lhr)
for sel, body in matches:
    print(sel, "-->", body[:100])
