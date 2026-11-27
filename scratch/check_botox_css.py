with open('botox.html', 'r', encoding='utf-8') as f:
    b = f.read()

import re
m = re.findall(r'(\.hf-why[^{]+)\{', b)
print('hf-why in botox:', m)
m2 = re.findall(r'(\.bx-why[^{]+)\{', b)
print('bx-why in botox:', m2)
