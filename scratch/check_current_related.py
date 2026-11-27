with open('under-eye-darkness.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re

print("--- CSS for related in under-eye-darkness.html ---")
m = re.findall(r'[^{]*related[^{]*\{[^}]*\}', c, re.I)
for match in m:
    print(match)
    print("---")

print("\n--- HTML of #related-services in under-eye-darkness.html ---")
idx = c.find('id="related-services"')
if idx != -1:
    end = c.find('</section>', idx) + 10
    print(c[idx-50:end])

print("\n--- JS check for relatedTrack in under-eye-darkness.html ---")
print("relatedTrack in JS?", 'relatedTrack' in c[c.rfind('<script'):])
