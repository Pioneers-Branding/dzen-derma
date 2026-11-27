import re

with open('under-eye-darkness.html', 'r', encoding='utf-8') as f:
    c = f.read()

print('Sections in under-eye-darkness.html:')
for m in re.finditer(r'<section[^>]*id=["\']([^"\']+)["\']', c):
    print(f"  section id='{m.group(1)}'")

with open('pigmentation.html', 'r', encoding='utf-8') as f:
    p = f.read()

print('\nSections in pigmentation.html:')
for m in re.finditer(r'<section[^>]*id=["\']([^"\']+)["\']', p):
    print(f"  section id='{m.group(1)}'")
