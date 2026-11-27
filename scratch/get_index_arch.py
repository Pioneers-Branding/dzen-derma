with open('index.html', 'r', encoding='utf-8') as f:
    idx_c = f.read()

import re
matches = re.findall(r'<div class="service-arch-card[^"]*">.*?</div>\s*</div>\s*</article>', idx_c, re.DOTALL)
print("Index service-arch-cards count:", len(matches))
for m in matches[:10]:
    print(re.findall(r'<h[34][^>]*>(.*?)</h[34]>', m), re.findall(r'src=["\']([^"\']+)["\']', m))
