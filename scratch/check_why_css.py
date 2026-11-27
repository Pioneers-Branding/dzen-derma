with open('under-eye-darkness.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'(\.hf-why[^{]+)\{', c)
print('hf-why CSS matches in under-eye-darkness.html:', matches[:10])

matches2 = re.findall(r'(\.bx-why[^{]+)\{', c)
print('bx-why CSS matches in under-eye-darkness.html:', matches2[:10])
