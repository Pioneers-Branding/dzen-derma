with open('concerns.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re
matches = re.findall(r'<a[^>]*href=["\']sagging-skin\.html["\'][^>]*>.*?</a>', c, re.DOTALL)
print("Found in concerns.html:", matches)

matches2 = re.findall(r'<img[^>]+(?:sag|lax)[^>]+>', c, re.I)
print("Laxity/sagging images in concerns.html:", matches2)
