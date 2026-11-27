with open('styles.css', 'r', encoding='utf-8') as f:
    s = f.read()

import re
matches = re.findall(r'(\.hf-related[^{]+)\{([^}]+)\}', s)
print("Found in styles.css:", len(matches))
for sel, b in matches:
    print(sel, "-->", b[:80])
