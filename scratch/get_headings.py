with open('concerns.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
m = re.findall(r'<h[34][^>]*>(.*?)</h[34]>', c)
print("Headings in concerns.html:", m[:20])
